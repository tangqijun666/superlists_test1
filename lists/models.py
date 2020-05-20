# coding=utf-8

from django.db import models


class List(models.Model):
    pass


class Item(models.Model):
    text = models.TextField(default='', verbose_name='内容')
    list = models.ForeignKey(List, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
