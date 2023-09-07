from django import forms

class ContactForm(forms.Form):
    name=forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class':'form-floating','rows':3, 'placeholder':'Escribe tu nombre'}
    ), min_length=3, max_length=100)
    email=forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={'class':'form-floating','placeholder':'Escribe tu email'}
    ))
    subject=forms.CharField(label="Asunto", required=True, widget=forms.Textarea(
        attrs={'class':'form-floating','rows':2,'placeholder':'Escribe tu asunto'}
    ), min_length=10, max_length=1000)
    message=forms.CharField(label="Mensaje", required=True, widget=forms.Textarea(
        attrs={'class':'form-floating','rows':3,'placeholder':'Escribe tu mensaje'}
    ), min_length=10, max_length=1000)