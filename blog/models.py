# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Post(models.Model):

    title = models.CharField(u'Заголовок', max_length=150)
    author = models.CharField(u'Автор', max_length=250, default='admin')
    text = models.TextField(u'Текст')
    create_date = models.DateTimeField(u'Дата создания', auto_now_add=True)

    class Meta:

        verbose_name = u'Запись'
        verbose_name_plural = u'Записи'
        ordering = ['-create_date']

    def __unicode__(self):

        return u'{} {}'.format(self.title, self.create_date)
