from django.db import models
from datetime import datetime

# Create your models here.

class Tag(models.Model):
    text = models.CharField(max_length=50)

    def __unicode__(self):
        return self.text

class Question(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=50)
    created = models.DateTimeField()
    tag = models.ForeignKey(Tag)

    #def __init__(self):
    #    self.created = datetime.now()

    def __unicode__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question)
    text = models.TextField()
    author = models.CharField(max_length=50)
    created = models.DateTimeField()

    def __unicode__(self):
        return self.text