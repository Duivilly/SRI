from django import forms

# from pages.forms import FormBaseImage
# form= FormBaseImage()
# print(form.as_p())

class FormBaseImage(forms.Form):
    search_text= forms.CharField(label='', max_length=150, required=False)
    search_image= forms.ImageField(label='', required=False)

