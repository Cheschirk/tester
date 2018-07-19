from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.urls import reverse


class TestPlan(models.Model):
    TEST_PLAN_STATUS = (
        ('success', 'Пройдён'),
        ('in_process', 'В процессе'),
        ('failed', 'Не пройден'),
    )
    title = models.CharField(max_length=300, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    status = models.CharField(max_length=10, choices=TEST_PLAN_STATUS, default='failed', verbose_name='Статус')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    test_cases = models.ManyToManyField('test_case.TestCase', through='test_plan.PlanCase')

    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)

    class Meta:
        verbose_name = 'Тест план'
        verbose_name_plural = 'Тест планы'

    def __str__(self):
        return self.title

    def get_absolute_url(self):

        return reverse('test_plan_view', args=[str(self.id)])


class PlanCase(models.Model):
    test_plan = models.ForeignKey(TestPlan, on_delete=models.CASCADE)
    test_case = models.ForeignKey('test_case.TestCase', on_delete=models.CASCADE)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Связь тест плана и тест кейса'
        verbose_name_plural = 'Связи тест планов и тест кейсов'


class PlanLog(models.Model):
    TEST_CASE_STATUS = (
        ('success', 'Пройдён'),
        ('failed', 'Не пройден'),
    )
    test_plan = models.ForeignKey(TestPlan, on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=TEST_CASE_STATUS, default='failed', verbose_name='Статус')

    class Meta:
        verbose_name = 'Лог тест-плана'
        verbose_name_plural = 'Логи тест-плана'

    def __str__(self):
        return self.created_at



