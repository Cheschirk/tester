from django.shortcuts import render
from modules.test_plan.models import TestPlan
from django.views import generic
from modules.test_plan.forms import TestPlanForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


@method_decorator(login_required, name='dispatch')
class PlanListView(generic.ListView):
    model = TestPlan
    template_name = 'test_plan/test_plan_list.html'
    paginate_by = 10


@method_decorator(login_required, name='dispatch')
class DashboardView(generic.ListView):
    model = TestPlan
    template_name = 'test_plan/index.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        count_all = TestPlan.objects.filter().count()
        count_success = TestPlan.objects.filter(status='success').count()
        count_fail = TestPlan.objects.filter(status='failed').count()
        context['count_all'] = count_all
        context['count_success'] = count_success
        context['count_fail'] = count_fail
        return context


@method_decorator(login_required, name='dispatch')
class PlanDetailView(generic.DetailView):
    model = TestPlan
    template_name = 'test_plan/test_plan_view.html'

    def get_context_data(self, **kwargs):
        context = super(PlanDetailView, self).get_context_data(**kwargs)
        instance = self.get_object()
        context['plancase_list'] = instance.plancase_set.filter()
        return context


@method_decorator(login_required, name='dispatch')
class PlanNewView(generic.CreateView):
    model = TestPlan
    form_class = TestPlanForm
    template_name = 'test_plan/test_plan_new.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class PlanUpdateView(generic.UpdateView):
    model = TestPlan
    form_class = TestPlanForm
    template_name = 'test_plan/test_plan_edit.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return super().form_valid(form)






