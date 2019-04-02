# -*- coding: utf-8 -*-
# __author__ = 'zjj'
# date：2019/3/27 21:07
import sys

sys.path.append("..")

from orm import Model, StringField, IntegerField

class User(Model):
    __table__ = 'users'
    id = IntegerField(primary_key=True)
    name = StringField()