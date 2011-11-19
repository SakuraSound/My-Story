'''
Created on Nov 18, 2011

@author: Haruka
'''


import os
import os.path as path
import sys
import csv
import model
import view


def start(csvpath = "csv_queries/", app_path="my_story/"):
    print "Start"
    if not os.path.exists(csvpath):
        print "Either the csv path or the output path don't exist"
    else:
        file_list = [f for f in os.listdir(csvpath) if path.splitext(f)[1] == '.csv']
        print file_list
        for csvfile in file_list:
            category = path.splitext(csvfile)[0]
            print "Reading question bank for {0}".format(category)
            src_path = path.join(csvpath, csvfile)
            #Check if the django model path exists
            if not path.exists(app_path):
                os.mkdir(app_path)
            # Check if the category path exists
            cat_path = "/".join([app_path, category])
            if not path.exists(cat_path):
                os.mkdir(cat_path)
                open(path.join(cat_path, "__init__.py"),'w').close()
            # Get to work
            with open(src_path, 'r') as f_obj:
                csvreader = csv.reader(f_obj, quoting=csv.QUOTE_NONNUMERIC, delimiter=",", quotechar='"')
                model.generate(category, csvreader, cat_path)
                view.generate(category, csvreader, cat_path)
    
if __name__ == '__main__':
    start()
