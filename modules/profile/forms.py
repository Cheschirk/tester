from django.forms import ModelForm
from modules.profile.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, ButtonHolder, Submit
from crispy_forms.layout import Div, HTML
from django.contrib.auth.forms import AuthenticationForm


class SigninForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'full_name', 'email', 'password']
        helper = FormHelper()
        helper.form_method = 'POST'

    def __init__(self, *args, **kwargs):
        super(SigninForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.label_class = 'col-md-2 col-xs-3 text-white'
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(Field('username', css_class='form-control'), css_class='form-group'),
                Div(Field('full_name', css_class='form-control'), css_class='form-group'),
                Div(Field('email', css_class='form-control'), css_class='form-group'),
                Div(Field('password', css_class='form-control'), css_class='form-group'),
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


class UserUpdateForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', ]
        helper = FormHelper()
        helper.form_method = 'POST'

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.label_class = 'col-md-2 col-xs-3 text-white'
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(Field('username', css_class='form-control'), css_class='form-group'),
                Div(Field('email', css_class='form-control'), css_class='form-group'),
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
