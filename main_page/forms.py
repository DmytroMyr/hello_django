from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'type' : 'text',
        'name' : 'name',
        'class' : 'form-control',
        'id' : 'name',
        'placeholder' : 'YourName',
        'data-rule' : 'minlen:4',
        'data-msg' : 'Pleaseenteratleast4chars',
    }))
    phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'type' : 'text',
        'class' : 'form-control',
        'name' : 'phone',
        'id' : 'phone',
        'placeholder' : 'YourPhone',
        'data-rule' : 'minlen:4',
        'data-msg' : 'Pleaseenteratleast4chars',
    }))
    persons = forms.IntegerField(widget=forms.NumberInput(attrs={
        'type' : 'number',
        'class' : 'form-control',
        'name' : 'people',
        'id' : 'people',
        'placeholder' : '#ofpeople',
        'data-rule' : 'minlen:1',
        'data-msg' : 'Please enter at least 1 chars',
    }))
    message = forms.CharField(max_length=255, widget=forms.Textarea(attrs={
        'class' : 'form-control',
        'name' : 'message',
        'rows' : '5',
        'placeholder' : 'Message',
    }))

    class Meta:
        model = Reservation
        fields = ('name', 'phone', 'persons', 'message')