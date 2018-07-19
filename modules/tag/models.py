from __future__ import unicode_literals
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import fields


class TagItem(models.Model):
    tag = models.SlugField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = 'TagItem'
        verbose_name_plural = 'TagItems'

    def __str__(self):
        return self.tag


class Tag(models.Model):
    title = models.CharField(max_length=20, default='tag')
    tags = fields.GenericRelation(TagItem, content_type_field='content_type_fk', object_id_field='object_primary_key')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.title


