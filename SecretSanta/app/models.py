from django.contrib.auth.models import AbstractUser
from django.db import models


class Owner(AbstractUser):
    owned_groups = models.ManyToManyField('Group')


class SimpleUser(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    answers = models.ForeignKey('FieldAnswer', blank=True, null=True, on_delete=models.CASCADE)
    assigned = models.ForeignKey('SimpleUser', blank=True, null=True, on_delete=models.CASCADE)


# TODO: Maybe add many forms per group
class Group(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=150)
    fields = models.ManyToManyField('Field')
    

# TODO: Add ability to make fields required
class Field(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=150)

# TODO: Allow for deleting of Submitted Entries
class FieldAnswer(models.Model):
    def __str__(self):
        return self.answer

    answer = models.CharField(max_length=600)
    field = models.ManyToManyField('Field')
    user = models.ManyToManyField('SimpleUser')
