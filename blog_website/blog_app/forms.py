from django import forms
from blog_app.models import UserProfileInfo, Newpost
from django.contrib.auth.models import User

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female')
)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']


class UserProfileInfoForm(forms.ModelForm):
    sex = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect(), required=False)

    class Meta():
        model = UserProfileInfo
        fields = ['profile_pic', 'sex']


class NewpostForm(forms.ModelForm):
    post = forms.CharField(widget=forms.Textarea)

    class Meta():
        model = Newpost
        exclude = ['author', 'published_date']
