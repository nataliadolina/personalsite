from django.db import models
from django.db.models import AutoField, DateField, CharField, ForeignKey, DecimalField, TextField, EmailField, \
    BooleanField, IntegerField
from django.utils import timezone
from django.urls import reverse


class ProgramDescription(models.Model):
    id = AutoField(primary_key=True)
    content = TextField()
    objects = models.Manager()


class ProgramCats(models.Model):
    id = AutoField(primary_key=True)
    cat = CharField(max_length=500, blank=True)
    cat_description = ForeignKey(ProgramDescription, on_delete=models.DO_NOTHING, null=True)
    objects = models.Manager()


class Program(models.Model):
    id = AutoField(primary_key=True)
    name = TextField()
    description = TextField(null=True, blank=True)
    full_description = ForeignKey(ProgramCats, on_delete=models.CASCADE, blank=True)
    objects = models.Manager()

    def __str__(self):
        return '%s' % self.name

    def get_category_url(self):
        return reverse('program', kwargs={'id': self.id})


def default_programs_order():
    return Cats._base_manager.count() + 1


class Cats(models.Model):
    id = AutoField(primary_key=True)
    order = IntegerField(default=default_programs_order)
    name = CharField(max_length=150)
    description = TextField(blank=True)
    programs = ForeignKey(Program, on_delete=models.DO_NOTHING, null=True)
    objects = models.Manager()

    def __str__(self):
        return '%s' % self.name
