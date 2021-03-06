# -*- coding: utf-8 -*-
"""classImageHierarchy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lcuptJByCbZHvyJhwoz_53ySRKX3XH7v
"""

import pandas as pd

classes = pd.read_csv('oidv6-class-descriptions.csv', header=None)
classes2name={i:j for i,j in zip(classes[0], classes[1])}
name2classes={j:i for i,j in zip(classes[0], classes[1])}
classes.tail()

import json

hier = json.load(open('bbox_labels_600_hierarchy.json','r'))

level1 = level2 = level3 = []

for l2 in hier['Subcategory']:
    print(classes2name[l2['LabelName']])
    level3.append(classes2name[l2['LabelName']])
    try:
        for j in l2['Subcategory']:
            print('----> ',classes2name[j['LabelName']])
            level2.append(classes2name[j['LabelName']])
            try:
                for k in j['Subcategory']:
                    print('\t----> ',classes2name[k['LabelName']])
                    level1.append(classes2name[k['LabelName']])
            except:
                pass
    except:
        pass
        
level1 = set(level1)
level2 = set(level2)
level3 = set(level3)

print('level 1 Class count -> {}'.format(len(level1)))
print('level 2 Class count -> {}'.format(len(level2)))
print('level 3 Class count -> {}'.format(len(level3)))
print('Unique classes {}'.format(len(level1)+len(level2)+len(level3)))

print('level 1&2 overlaps -> {}'.format(len(level2&level1)))
print('level 2&3 overlaps -> {}'.format(len(level2&level3)))
print('level 1&3 overlaps -> {}'.format(len(level3&level1)))

all_training_classes = set(list(classes[1]))
all_json_classes = level1.union(level2).union(level3)
print("Number of Classes in JSON are -> ", len(all_json_classes))
print("Number of Classes in Training file are -> ", len(all_training_classes))
# print('There are {} classes from JSON file and {} classes from training file'.format(len(all_json_classes), len(all_training_classes)))
print('No. of missing classes -> ', (len(all_training_classes)-len(all_json_classes)))

print(all_training_classes-all_json_classes)