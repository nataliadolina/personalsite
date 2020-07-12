from django.forms import ModelForm

from .models import ProgramDescription, ProgramCats, Program, Cats


class AddCat(ModelForm):
    class Meta:
        model = Cats
        fields = ['order', 'name', 'description']


class AddProgram(ModelForm):
    class Meta:
        model = Program
        fields = ['name', 'description', 'full_description']
