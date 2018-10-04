# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from .models import Person
# generic delete view
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy


# Create your views here.
from django.http import HttpResponse

def contact_list(request):
    # gets all contacts and sorts them by name
    persons = Person.objects.all().order_by('first_name')
    return render(request, 'addressbook/contact_list.html', {'persons': persons})

# contact details
def contact_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)
    return render(request, 'contact/contact_detail.html', {'person': person})

# adding a contact
def contact_new(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PersonForm()
    return render(request, 'contact/contact_edit.html', {'form': form})

# editing a contact
def contact_edit(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('/person/' + str(person.pk))
    else:
        form = PersonForm(instance=person)
    return render(request, 'contact/contact_edit.html', {'form': form})

    # deleting a contact
    # generic view
    class ContactDelete(DeleteView):
        model = Person
        success_url = reverse_lazy('contact_list')