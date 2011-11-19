'''
Created on Nov 18, 2011

@author: Haruka
'''
'''
# Create your views here.
from django.http import HttpResponse
from django import form
from django.forms import ModelForm
from django.template import loader, Context
from models import Food

def survey(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/food/result') 
    else:
        form = FoodForm()
    
    return render_to_response('html/food.html', {'form':form})


class FoodForm(ModelForm):
    class Meta:
        model = Food
'''

import os

def generate(category, csvfile, dest=None):
    pass
    
    