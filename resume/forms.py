from django import forms
from .models import Contact, Comment, Newslatter


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for kalit, qiymat in self.fields.items():
            qiymat.widget.attrs['class'] = 'form-control'
            qiymat.widget.attrs['placeholder'] = kalit.title()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['blog']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        for kalit, qiymat in self.fields.items():
            qiymat.widget.attrs['class'] = 'form-control'
            # qiymat.widget.attrs['placeholder'] = kalit.title()


class NewslatterForm(forms.ModelForm):
    class Meta:
        model = Newslatter
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(NewslatterForm, self).__init__(*args, **kwargs)
        for kalit, qiymat in self.fields.items():
            qiymat.widget.attrs['class'] = 'form-control'
            qiymat.widget.attrs['placeholder'] = kalit.title()
