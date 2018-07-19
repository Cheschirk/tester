from __future__ import unicode_literals
from django.db import models
from django.conf import settings


class TestCase(models.Model):
    TEST_CASE_STATUS = (
        ('success', 'Пройдён'),
        ('failed', 'Не пройден'),
    )
    title = models.CharField(max_length=300, verbose_name='Название')
    precondition = models.TextField(verbose_name='Предусловие')
    description = models.TextField(verbose_name='Описание')
    result = models.TextField(verbose_name='Результат')

    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)
    last_run = models.DateTimeField(verbose_name='Дата последнего запуска')
    status = models.CharField(max_length=10, choices=TEST_CASE_STATUS, default='failed', verbose_name='Статус')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tag = models.ForeignKey('tag.Tag', on_delete=models.CASCADE, verbose_name='Тег')

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'

    def __str__(self):
        return self.title


class CaseLog(models.Model):
    TEST_CASE_STATUS = (
        ('success', 'Пройдён'),
        ('failed', 'Не пройден'),
    )
    test_case = models.ForeignKey(TestCase, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=TEST_CASE_STATUS, default='failed', verbose_name='Статус')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Лог тест-кейса'
        verbose_name_plural = 'Логи тест-кейса'

    def __str__(self):
        return self.created_at



