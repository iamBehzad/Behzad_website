from django import forms
from website.models import Contact
from django import forms
from captcha.fields import CaptchaField

class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        return name
    
    class Meta:
        model = Contact
        fields = '__all__'
        