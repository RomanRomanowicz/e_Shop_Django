from django import forms
from django.forms import ModelForm

from store.models.products import *


class EmailPostForm(forms.Form):
    your_name = forms.CharField(max_length=25)
    your_email = forms.EmailField()
    question = forms.CharField(required=False, widget=forms.Textarea)


# class ContactForm(forms.Form):
#     subject = forms.CharField(label='Тема', widget=forms.TextInput(attrs={'class':'form-control'}))
#     content = forms.CharField(label='tekst', widget=forms.Textarea(attrs={'class':'form-control', "rows": 5}))




class ProductForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Product's name"}))
    main_image = forms.ImageField(widget=forms.FileInput(attrs={"class":"form-control"}))
    description = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", "placeholder":"Product's description"}))
    price = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Product's price"}))

    class Meta:
        model = Product
        exclude = ['vendor',]
        fields = ['vendor', 'name', 'main_image', 'size', 'price', 'description']


class ImageForm(ModelForm):
    images = forms.ImageField(widget=forms.FileInput(attrs={"class":"form-control", "multiple":True}))

    class Meta:
        model = Image
        fields = ['images',]