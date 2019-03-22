from django.shortcuts import render
from django.views import generic
from django.shortcuts import render

from unesco2.models import Category, State, Region, Iso, Site

# Create your views here.

class CategoryListView(generic.ListView):
    model = Category

class CategoryDetailView(generic.DetailView):
    model = Category

class StateListView(generic.ListView):
    model = State

class StateDetailView(generic.DetailView):
    model = State

class RegionListView(generic.ListView):
    model = Region

class RegionDetailView(generic.DetailView):
    model = Region

class IsoListView(generic.ListView):
    model = Iso

class IsoDetailView(generic.DetailView):
    model = Iso

class SiteListView(generic.ListView):
    model = Site

class SiteDetailView(generic.DetailView):
    model = Site