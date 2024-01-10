from django import forms
from .models import Author, Comment
from captcha.fields import CaptchaField


class AuthorRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = CaptchaField()



    class Meta:
        model = Author
        fields = ['name', 'email', 'homepage', 'password']

    def __init__(self, *args, **kwargs):
        super(AuthorRegistrationForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['placeholder'] = 'Your Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Your Email'
        self.fields['homepage'].widget.attrs['placeholder'] = 'Your Homepage'
        self.fields['password'].widget.attrs['placeholder'] = 'Your Password'


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)
    parent_comment_id = forms.IntegerField(required=False, widget=forms.HiddenInput)
    comment_file = forms.FileField(required=False)  # Додано поле для файлів

    class Meta:
        model = Comment
        fields = ['content', 'parent_comment_id', 'comment_file']