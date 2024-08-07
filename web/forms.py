from django import forms
from .models import ContactForm, Comment

class ContactFormForm(forms.ModelForm):

    customer_email = forms.EmailField(label='Correo')
    customer_name = forms.CharField(max_length=64, label='Nombre')
    message = forms.CharField(
        label='Mensaje',
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 40, 'class': 'form-control'})
    )

    class Meta:
         model = ContactForm
         fields = ['customer_email', 'customer_name', 'message']
         

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'cols': 40, 'class': 'form-control'}),
        }        
