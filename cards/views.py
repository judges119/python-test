from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, DeleteView
from .models import Card, Category, PageView

class CardList(ListView): 
    model = Card

class CardDetail(DetailView): 
    model = Card

class CardCreate(CreateView): 
    model = Card
    fields = ['name', 'description', 'category']
    success_url = '/cards/'

class CardDelete(DeleteView): 
    model = Card
    success_url = '/cards/'