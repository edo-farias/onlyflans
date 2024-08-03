from django import forms
from .models import ContactForm

'''class ContactFormForm(forms.ModelForm):

    customer_email = forms.EmailField(label='Correo')
    customer_name = forms.CharField(max_length=64, label='Nombre')
    message = forms.CharField(
        label='Mensaje',
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 40, 'class': 'form-control'})
    )

    class Meta:
         model = ContactForm
         fields = ['customer_email', 'customer_name', 'message']
'''

class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email', 'customer_name', 'message']
        labels = {
            'customer_email': 'Correo',
            'customer_name': 'Nombre',
            'message': 'Mensaje',
        }
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5, 'cols': 40, 'class': 'form-control'}),
        }
           
