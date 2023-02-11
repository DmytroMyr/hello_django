from django.db import models
from django.core.validators import FileExtensionValidator, RegexValidator


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.title}'

    class Meta:
        ordering = ('position',)

    def __iter__(self):
        for item in self.dishes.all():
            yield item

class Dish(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField()
    is_visible = models.BooleanField(default=True)
    ingredients = models.CharField(max_length=255)
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.ImageField(upload_to='dishes/%Y_%m_%d', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes')
    is_special = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.title}'

    class Meta:
        ordering = ('category', 'position')

class About(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    paragraph = models.TextField(max_length=500, blank=False)
    video = models.FileField(upload_to='videos', null=True, 
                            validators=[FileExtensionValidator(allowed_extensions=['mov','avi','mp4','webm','mkv'])])

    def __str__(self) -> str:
        return f'{self.title}'

class WhyUs(models.Model):
    position = models.SmallIntegerField()
    title = models.CharField(max_length=50, unique=True, db_index=True)
    paragraph = models.TextField(max_length=255, blank=False)

    def __str__(self) -> str:
        return f'{self.title}'

    class Meta:
        ordering = ('position',)

        
class Events(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.TextField(max_length=255, blank=False)
    photo = models.ImageField(upload_to='events/%Y_%m_%d', blank=True)

    def __str__(self) -> str:
        return f'{self.title}'

    class Meta:
        ordering = ('position',)


class Reservation(models.Model):
    phone_validator = RegexValidator(regex=r'^\+?3?8?0\d{2}[- ]?(\d[- ]?){7}$', message='Error phone number')

    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, validators=[phone_validator])
    persons = models.SmallIntegerField()
    message = models.TextField(max_length=255, blank=True)

    date = models.DateField(auto_now_add=True)
    date_processing = models.DateField(auto_now=True)
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}: {self.phone}'

    class Meta:
        ordering = ('-date',)
