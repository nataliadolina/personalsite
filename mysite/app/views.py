from django.shortcuts import render
from .models import Cats
from .forms import AddCat, AddProgram
import numpy as np


def index(request):
    b_programs = {}
    cats_names = [el.name for el in Cats.objects.all().order_by("order")]
    for name in cats_names:
        query = Cats.objects.select_related('programs').get(name=name)
        add, length = return_divisible_length(3, query)
        query = list(query)
        query += [0] * (add - length)
        query = np.array(query).reshape((length // 3, 3))
        b_programs[name] = query
    context = {'programs': b_programs.items()}
    return render(request, 'index.html', context)


def return_divisible_length(number, query):
    length = len(query)
    if length % number == 0:
        return length, length
    return length // number + number, length


def add_new_program(request, id):
    id = int(id)
    if request.method != 'POST':
        if id == 0:
            formCat = AddCat
            formProgram = AddProgram
        else:
            formCat = AddCat(Cats.objects.filter(id=id))
            formProgram = AddProgram(Cats.objects.select_related('programs').get(id=id))
    else:
        formCat = AddCat(request.POST)
        formProgram = AddProgram(request.POST)
        if formCat.is_valid() and formProgram.is_valid():
            cat = formCat.save(commit=False)
            cat.program_set.add(formProgram.save())
    return render(request, 'add_program.html', {'formCat': formCat, 'formProgram': formProgram})
