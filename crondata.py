#!/usr/bin/env python
# -*- coding: utf-8 -*-
#coding: utf-8
#http://www.liao123.net/cms/show_article/32007.html
# 98~516

#from app import intodatas
#a = intodatas().rungo()
#intodatas().rungo()

from datamodel import rosst
#rosst(name = 'toomore').put()
a = rosst().all()
print '123'
print a.count()
#for i in a:
#  i.delete()
