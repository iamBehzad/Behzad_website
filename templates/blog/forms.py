from django import forms
from website.models import Contact,Newsletter
from django import forms
from captcha.fields import CaptchaField

class ContactForm(forms.ModelForm):
    captcha = CaptchaField()

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name:
            name = 'ناشناس'
        return name
    class Meta:
        model = Contact
        fields = '__all__'