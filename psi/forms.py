from django import forms

"""
Forms and validation code for user registration.

Note that all of these forms assume your user model is similar in
structure to Django's default User class. If your user model is
significantly different, you may need to write your own form class;
see the documentation for notes on custom user models with
django-registration.

"""

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from apps.usuarios.models import *

from registration import validators


#User = get_user_model()
User = usuarioPerfil()

class MyRegistrationForm(UserCreationForm):
    """
    Form for registering a new user account.

    Validates that the requested username is not already in use, and
    requires the password to be entered twice to catch typos.

    Subclasses should feel free to add any additional validation they
    need, but should take care when overriding ``save()`` to respect
    the ``commit=False`` argument, as several registration workflows
    will make use of it to create inactive user accounts.

    """
    # Explicitly declared here because Django's default
    # UserCreationForm, which we subclass, does not require this field
    # but workflows in django-registration which involve explicit
    # activation step do require it. If you need an optional email
    # field, simply subclass and declare the field not required.
    
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':'text',"placeholder":'Usuario'}), label='',required=True)
    email = forms.EmailField(widget= forms.TextInput(attrs={'class':'form-control','type':'text',"placeholder":'correo'}), label='',required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type':'password',"placeholder":'Password'}),label='')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type':'password',"placeholder":'Re Type Password'}),label='')
    class Meta(UserCreationForm.Meta):
        fields = [
           	'username',
            'email',
            'password1',
            'password2'
        ]
        required_css_class = 'required'

    def clean(self):
        """
        Apply the reserved-name validator to the username.

        """
        # This is done in clean() because Django does not currently
        # have a non-ugly way to just add a validator to an existing
        # field on a form when subclassing; the standard approach is
        # to re-declare the entire field in order to specify the
        # validator. That's not an option here because we're dealing
        # with the user model and we don't know -- given custom users
        # -- how to declare the username field.
        #
        # So defining clean() and attaching the error message (if
        # there is one) to the username field is the least-ugly
        # solution.
        username_value = self.cleaned_data.get('username')
        if username_value is not None:
            try:
                if hasattr(self, 'reserved_names'):
                    reserved_names = self.reserved_names
                else:
                    reserved_names = validators.DEFAULT_RESERVED_NAMES
                validator = validators.ReservedNameValidator(
                    reserved_names=reserved_names
                )
                validator(username_value)
            except ValidationError as v:
                self.add_error('username', v)
        super(MyRegistrationForm, self).clean()


class RegistrationFormTermsOfService(MyRegistrationForm):
    """
    Subclass of ``RegistrationForm`` which adds a required checkbox
    for agreeing to a site's Terms of Service.

    """
    tos = forms.BooleanField(
        widget=forms.CheckboxInput,
        label=_(u'I have read and agree to the Terms of Service'),
        error_messages={
            'required': validators.TOS_REQUIRED,
        }
    )


class RegistrationFormUniqueEmail(MyRegistrationForm):
    """
    Subclass of ``RegistrationForm`` which enforces uniqueness of
    email addresses.

    """
    def clean_email(self):
        """
        Validate that the supplied email address is unique for the
        site.

        """
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(validators.DUPLICATE_EMAIL)
        return self.cleaned_data['email']


class RegistrationFormNoFreeEmail(MyRegistrationForm):
    """
    Subclass of ``RegistrationForm`` which disallows registration with
    email addresses from popular free webmail services; moderately
    useful for preventing automated spam registrations.

    To change the list of banned domains, pass a list of domains as
    the keyword argument ``bad_domains`` when initializing the form.

    """
    bad_domains = ['aim.com', 'aol.com', 'email.com', 'gmail.com',
                   'googlemail.com', 'hotmail.com', 'hushmail.com',
                   'msn.com', 'mail.ru', 'mailinator.com', 'live.com',
                   'yahoo.com']

    def clean_email(self):
        """
        Check the supplied email address against a list of known free
        webmail domains.

        """
        email_domain = self.cleaned_data['email'].split('@')[1]
        if email_domain in self.bad_domains:
            raise forms.ValidationError(validators.FREE_EMAIL)
        return self.cleaned_data['email']


class Login_form(forms.Form):
	username = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control','type':'text',"placeholder":'Username',}),label='')
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type':'password',"placeholder":'Password'}),label='')

class Remember_form(forms.Form):
	email = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control',"placeholder":'E-Mail','id':'MailRecover'}))