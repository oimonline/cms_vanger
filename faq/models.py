#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime

class Tag(models.Model):
    tag_text = models.CharField(
        max_length=64,
        verbose_name=u'метка'
    )

    slug = models.SlugField()

    def __unicode__(self):
        return self.tag_text

class Question(models.Model):
    question_text = models.TextField(
        verbose_name=u'вопрос'
    )

    author_name = models.CharField(
        max_length=128,
        verbose_name=u'имя автора вопроса'
    )

    author_email = models.EmailField(
        verbose_name=u'электронная почта автора вопроса'
    )

    created = models.DateTimeField(
        default=datetime.now(),
        verbose_name=u'создан'
    )

    tags = models.ManyToManyField(
        Tag,
        blank=True,
        null=True,
        verbose_name=u'метка'
    )

    def __unicode__(self):
        return self.question_text

class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        verbose_name=u'вопрос'
    )

    answer_text = models.TextField(
        verbose_name=u'ответ'
    )

    author_name = models.CharField(
        max_length=128,
        verbose_name=u'автор ответа'
    )

    created = models.DateTimeField(
        default=datetime.now(),
        verbose_name=u'создан'
    )

    def __unicode__(self):
        return self.answer_text