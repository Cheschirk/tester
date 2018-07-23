from django.shortcuts import render
from modules.test_case.models import TestCase
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='dispatch')
class CaseListView(generic.ListView):
    model = TestCase
    template_name = 'test_case/test_case_list.html'
    paginate_by = 10


@method_decorator(login_required, name='dispatch')
class CaseDetailView(generic.DetailView):
    model = TestCase
    template_name = 'test_case/test_case_view.html'

    def get_context_data(self, **kwargs):
        context = super(CaseDetailView, self).get_context_data(**kwargs)
        instance = self.get_object()
        context['plancase_list'] = instance.plancase_set.filter()
        return context


def test_case_new(request):
    return render(request, '../templates/test_case/test_case_new.html')


def test_case_edit(request):
    return render(request, '../templates/test_case/test_case_edit.html')







