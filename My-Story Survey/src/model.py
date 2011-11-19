'''
Created on Nov 2, 2011

@author: Hanabi
'''

"""
from django.db import models

# Create your models here.



class Food(models.Model):
    LIKES_CHOICES = ((2, u'Love it!'),
                     (1, u'Like it'),
                     (0, u'Neutral'),
                     (-1, u'Dislike'),
                     (-2, u'Hate it!'),
                 )
    
    COFFEE_OR_TEA = ((0, u'Coffee'), (1, u'Tea'), (2, u'Neither'),)
    
    uid = models.IntegerField(primary_key = True)
    l_spicy = models.IntegerField(default = 0)
    l_sweet = models.IntegerField(default = 0, choices = LIKES_CHOICES)
    l_tart = models.IntegerField(default = 0, choices = LIKES_CHOICES)
    l_sour = models.IntegerField(default = 0, choices = LIKES_CHOICES)
    l_bitter = models.IntegerField(default = 0, choices = LIKES_CHOICES)
    l_salty = models.IntegerField(default = 0, choices = LIKES_CHOICES)
    c_or_t = models.IntegerField(default=2, choices = COFFEE_OR_TEA)
"""
import os
import sys
import csv
from string import Template
from datetime import datetime


def get_header(category):
    with open('templates/model_header.tmp','r') as temp:
        dtime = datetime.now().strftime("%A %d. %B %Y %H:%M:%S")
        return Template("".join(temp.readlines())).substitute(date=dtime,
                                                                cat=category)
        
def create_options(choices):
    options = ["({0}, \"{1}\")".format(choices[i], choices[i+1]) for i in xrange(0, len(choices), 2)]
    print options
    ostring = ", ".join(options)
    return ostring
        

def generate(category, queries, dest=None):
    print dest
    print '{0}/{1}.py'.format(dest, category)
    with open('{0}/model.py'.format(dest, category), 'w') as model_file:
        print >> model_file, get_header(category)
        print >> model_file, "#    ------ BEGIN ATTRIBUTES -----    #"
        count = 0
        for query in queries:
            print >> model_file, "#    *** QUESTION {0} {1}***    ".format(count, query[0])
            print >> model_file, "    choices{0} = ({1},)".format(count, create_options(query[1:]))
            print >> model_file, "    query{0} = models.IntegerField(default = 0, choices = choices{0})".format(count)
            count += 1
        print >> model_file, "#    ------ END ATTRIBUTES -----     "
        print >> model_file, "#--------- END MODEL DEFINITION ----------"
    pass


if __name__ == '__main__':
    with open('/Users/Haruka/git/My-Story2/My-Story Survey/src/categories/food.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC, delimiter=",", quotechar='"')
        generate('food', csvreader)
    
    
    
    