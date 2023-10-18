from django.shortcuts import render
from django.views.generic import (ListView,
                                DetailView,
                                CreateView,
                                )
from .models import AddressBook
from .forms import AddressBookForm

class AddressListView(ListView):
    model = AddressBook
    template_name = 'directory/address_list.html'

class AddressCreateView(CreateView):
    model = AddressBook
    fields = '__all__'
    template_name = 'directory/address_create.html'

class AddressDetailView(DetailView):
    model = AddressBook
    template_name = 'directory/address_detail.html'