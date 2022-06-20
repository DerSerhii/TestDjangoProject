from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

CEFR_CHOICES = (
    ("A1", "Beginner"),
    ("A2", "Elementary"),
    ("B1", "Intermediate"),
    ("B2", "Upper-Intermediate"),
    ("C1", "Advanced"),
    ("C2", "Proficiency")
)

SEX_CHOICES = (
    ("M", "Male"),
    ("F", "Female")
)


class CandidateCefrForm(forms.Form):
    name = forms.CharField(label="Name",
                           max_length=30,
                           min_length=2)
    sex = forms.ChoiceField(label="Sex",
                            choices=SEX_CHOICES)
    age = forms.IntegerField(label="Age",
                             min_value=16)
    eng_level = forms.ChoiceField(label="English level according to the CEFR scale",
                                  choices=CEFR_CHOICES)

    def clean(self):
        cleaned_data = super().clean()
        sex = cleaned_data.get("sex")
        age = cleaned_data.get("age")
        eng_level = cleaned_data.get("eng_level")

        admission_male = sex == "M" and age >= 20 and eng_level in ["C1", "C2"]
        # "и уровнем английского B2 выше" - принял как "выше B2", а не как - "B2 (и) выше"
        admission_female = sex == "F" and age > 22 and eng_level in ["B2", "C1", "C2"]

        if not (admission_male or admission_female):
            self.add_error(None, "Sorry, your questionnaire does not match the search criteria")


class RegistrationBloggerForm(forms.Form):
    username = forms.CharField(label=_("Username"),
                               max_length=30,
                               min_length=2)
    first_name = forms.CharField(label=_("First name"),
                                 max_length=30,
                                 required=False)
    last_name = forms.CharField(label=_("Last name"),
                                max_length=30,
                                required=False)
    email = forms.EmailField(max_length=30,
                             required=False)
    password = forms.CharField(label=_("Password"),
                               max_length=30,
                               widget=forms.PasswordInput)
    password_confirm = forms.CharField(label=_("Password confirmation"),
                                       widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError('Sorry, but a user with that username is already registered :(')
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 4:
            raise ValidationError('Make the password more secure, at least 4 characters')
        return password

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password and password != password_confirm:
            raise ValidationError('Passwords do not match')
        return password_confirm


class AuthenticationBloggerForm(forms.Form):
    username = forms.CharField(label=_("Username"))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        if username and password:
            self.user = authenticate(username=username, password=password)
            if self.user is None:
                message = "Сheck the correctness of the entered data"
                raise forms.ValidationError(message)


class PasswordChangeForm(forms.Form):
    current_password = forms.CharField(label=_("Current password"),
                                       widget=forms.PasswordInput)
    current_password_confirm = forms.CharField(label=_("Current password confirmation"),
                                               widget=forms.PasswordInput)
    new_password = forms.CharField(label=_("New password"),
                                   max_length=30,
                                   widget=forms.PasswordInput)
    new_password_confirm = forms.CharField(label=_("New password confirmation"),
                                           widget=forms.PasswordInput)

    def __init__(self, user=None, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        self.user = user

    def clean_current_password_confirm(self):
        current_password = self.cleaned_data.get('current_password')
        current_password_confirm = self.cleaned_data.get('current_password_confirm')

        if current_password != current_password_confirm:
            raise ValidationError('Current passwords do not match')

        return current_password_confirm

    def clean_new_password(self):
        new_password = self.cleaned_data.get('new_password')
        is_current_password_confirm = 'current_password_confirm' in self.cleaned_data
        if len(new_password) < 4 and is_current_password_confirm:
            raise ValidationError('Make the password more secure, at least 4 characters')
        return new_password

    def clean_new_password_confirm(self):
        new_password = self.cleaned_data.get('new_password')
        new_password_confirm = self.cleaned_data.get('new_password_confirm')

        if new_password and new_password != new_password_confirm:
            raise ValidationError('New passwords do not match')

        return new_password_confirm

    def clean(self):
        cleaned_data = super().clean()
        valid = self.user.check_password(cleaned_data["current_password"])

        if not valid:
            raise ValidationError("The current password entered does not match "
                                  "the password for this profile")


class SearchCommentForm(forms.Form):
    search = forms.CharField(label=_("Search text in comments"),
                             max_length=50)
    only_current_user = forms.BooleanField(label=_("Only in my comments"),
                                           required=False)
