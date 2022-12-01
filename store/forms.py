from django import forms


class EmailPostForm(forms.Form):
    your_name = forms.CharField(max_length=25)
    your_email = forms.EmailField()
    question = forms.CharField(required=False, widget=forms.Textarea)


# class ContactForm(forms.Form):
#     subject = forms.CharField(label='Тема', widget=forms.TextInput(attrs={'class':'form-control'}))
#     content = forms.CharField(label='tekst', widget=forms.Textarea(attrs={'class':'form-control', "rows": 5}))