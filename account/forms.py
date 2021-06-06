from django import forms
from django.contrib.auth.models import User
from django.db.models import fields
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()

    # Note that you use the PasswordInput widget to render the password HTML element.
    # This will include type="password" in the HTML.
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    # You have created a model form for the user model.

    # These fieldswill be validated based on their corresponding model fields.
    # For example, if the user chooses a username that already exists,
    # they will get a validation error because username is afield defined with unique=True

    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User

        # In your form, you includeonly the username, first_name, and email fields of the model.
        fields = ('username', 'first_name', 'email',)

    def clean_password2(self):
        # Check the second password against the first one and not let the form validate
        # if the passwords don't match.
        # This check is done when you validate the form by calling its is_valid() method.

        # You can provide a clean_<fieldname>() method
        # to any of your form fields in order to clean the value or raise form validation errors
        # for a specific field.

        # Forms also include a general clean() method to validate the entire form,
        # which is useful to validate fields that depend on each other.
        # In this case, you use the field-specific clean_password2() validation
        # instead of overriding the clean() method of the form.
        # This avoids overriding other field-specific checks that the ModelForm gets from
        # the restrictions set in the model (for example, validating that the username is unique)

        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password don\'t match.')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    # This will allow users to edit their first name, last name, andemail,
    # which are attributes of the built-in Django user model
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)


class ProfileEditForm(forms.ModelForm):
    # This will allow users to edit the profile data that you savein the custom Profile model.
    # Users will be able to edit their date of birth and upload a picture for their profile
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo',)
