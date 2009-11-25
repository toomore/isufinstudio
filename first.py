#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datamodel

finalno = datamodel.startno.all().get().finalno
total = datamodel.rossdatas.all().count()
'''
a = datamodel.rossdatas.all()
for i in a:
  print i.datas.encode('utf-8')
'''

print '123'
print 'Finance Studio for isufin'
print 'Total Data: <b>%s</b>, Final No.: <b>%s</b>' % (total,finalno)
