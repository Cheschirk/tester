from django.forms import ModelForm
from modules.profile.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, ButtonHolder, Submit
from crispy_forms.layout import Div, HTML
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth.forms import UsernameField

from django import forms
from django.contrib.auth import (password_validation)
from django.utils.translation import gettext_lazy as _


class SigninForm(ModelForm):
    """
        A form that creates a user, with no privileges, from the given username and
        password.
        """
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = ("username", "full_name", "email", "password1", "password2")
        field_classes = {'username': UsernameField}
        helper = FormHelper()
        helper.form_method = 'POST'

    def __init__(self, *args, **kwargs):
        super(SigninForm, self).__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs.update({'autofocus': True})
        self.helper = FormHelper()
        self.helper.label_class = 'col-md-2 col-xs-3 text-white'
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(Field('username', css_class='form-control'), css_class='form-group'),
                Div(Field('full_name', css_class='form-control'), css_class='form-group'),
                Div(Field('email', css_class='form-control'), css_class='form-group'),
                Div(Field('password1', css_class='form-control'), css_class='form-group'),
                Div(Field('password2', css_class='form-control'), css_class='form-group'),
                Div(
                    Div(
                        ButtonHolder(
                            Submit('submit', 'Сохранить', css_class='mr-3 btn-success'),
                            HTML('<a class="ml-3 btn btn-secondary" href="{% url "index" %}">Отмена</a>'),
                        ),
                        css_class='col-12 d-flex justify-content-center'),
                    css_class='form-row w-100'),
            )
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get('password2')
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except forms.ValidationError as error:
                self.add_error('password2', error)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    # class Meta:
    #     model = User
    #     fields = ['username', 'full_name', 'email', 'password']
    #     helper = FormHelper()
    #     helper.form_method = 'POST'

    # def __init__(self, *args, **kwargs):
    #     super(SigninForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.label_class = 'col-md-2 col-xs-3 text-white'
    #     self.helper.form_method = 'POST'
    #     self.helper.layout = Layout(
    #         Div(
    #             Div(Field('username', css_class='form-control'), css_class='form-group'),
    #             Div(Field('full_name', css_class='form-control'), css_class='form-group'),
    #             Div(Field('email', css_class='form-control'), css_class='form-group'),
    #             Div(Field('password', css_class='form-control'), css_class='form-group'),
    #         Div(
    #             Div(
    #                 ButtonHolder(
    #                     Submit('submit', 'Сохранить', css_class='mr-3 btn-success'),
    #                     HTML('<a class="ml-3 btn btn-secondary" href="{% url "index" %}">Отмена</a>'),
    #                              ),
    #                 css_class='col-12 d-flex justify-content-center'),
    #             css_class='form-row w-100'),
    #             )
    #                                )


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kw):
        super(LoginForm, self).__init__(*args, **kw)

        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
             Div(
                Div(Field('username', css_class='form-control'), css_class='form-group'),
                Div(Field('password', css_class='form-control'), css_class='form-group'),
                ),
             Div(
               Submit('submit', 'Login', css_class='btn btn-secondary'),
                ),
                                    )


# class UserUpdateForm(UserChangeForm):
#     password = ReadOnlyPasswordHashField(
#         label=_("Password"),
#         help_text=_(
#             "Raw passwords are not stored, so there is no way to see this "
#             "user's password, but you can change the password using "
#             "<a href=\"{}\">this form</a>.", requirement='NONE'
#         ),
#     )
#
#     class Meta:
#         model = User
#         fields = '__all__'
#         field_classes = {'username': UsernameField}
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['password'].help_text = self.fields['password'].help_text.format('../password/')
#         f = self.fields.get('user_permissions')
#         if f is not None:
#             f.queryset = f.queryset.select_related('content_type')
#
#     def clean_password(self):
#         # Regardless of what the user provides, return the initial value.
#         # This is done here, rather than on the field, because the
#         # field does not have access to the initial value
#         return self.initial["password"]




    # class Meta:
    #     model = User
    #     fields = ['username', 'email', ]
    #     helper = FormHelper()
    #     helper.form_method = 'POST'
    #
    # def __init__(self, *args, **kwargs):
    #     super(UserUpdateForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.label_class = 'col-md-2 col-xs-3 text-white'
    #     self.helper.form_method = 'POST'
    #     self.helper.layout = Layout(
    #         Div(
    #             Div(Field('username', css_class='form-control'), css_class='form-group'),
    #             Div(Field('email', css_class='form-control'), css_class='form-group'),
    #         Div(
    #             Div(
    #                 ButtonHolder(
    #                     Submit('submit', 'Сохранить', css_class='mr-3 btn-success'),
    #                     HTML('<a class="ml-3 btn btn-secondary" href="{% url "index" %}">Отмена</a>'),
    #                              ),
    #                 css_class='col-12 d-flex justify-content-center'),
    #             css_class='form-row w-100'),
    #             )
    #                                )
