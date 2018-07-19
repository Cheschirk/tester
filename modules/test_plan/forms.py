from django.forms import ModelForm
from modules.test_plan.models import TestPlan
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, ButtonHolder, Submit, Fieldset
from crispy_forms.layout import Div, HTML


class TestPlanForm(ModelForm):

    class Meta:
        model = TestPlan
        fields = ['title', 'description', ]
        helper = FormHelper()
        helper.form_method = 'POST'

    def __init__(self, *args, **kwargs):
        super(TestPlanForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.label_class = 'col-md-2 col-xs-3 text-white'
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(Field('title', css_class='form-control'), css_class='form-group'),
                Div(Field('description', css_class='form-control'), css_class='form-group'),
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



