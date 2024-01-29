from django.db import models

class Script(models.Model):
    name = models.CharField(max_length=20, default=None)
    author_id = models.IntegerField(default=0)
    body = models.TextField(default=None)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    color = models.CharField(max_length=20, default="0")
    url = models.CharField(max_length=256, default=None)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-updated']

class Template(models.Model):
    name = models.CharField(max_length=20, default=None)
    author_id = models.IntegerField(default=0)
    body = models.JSONField(default=None)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=256, default=None)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-updated']