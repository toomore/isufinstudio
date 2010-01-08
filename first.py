#!/usr/bin/env python
# -*- coding: utf-8 -*-
#http://maps.google.com/maps/geo?q=&output=csv&sensor=false

from datamodel import rosst
import csv,urllib2,logging
from google.appengine.ext import db
from google.appengine.api import memcache

#page = urllib2.urlopen('http://maps.google.com/maps/geo?q=%s&output=csv&sensor=false' % '台灣高雄市')
#cs = csv.reader(page)

geono = memcache.get('geono')
if geono is None:
  memcache.add('geono',0)
  geono = 0

ro = rosst.all().fetch(5,geono)

print '123'
for i in ro:
  try:
    page = urllib2.urlopen('http://maps.google.com/maps/geo?q=%s&output=csv&sensor=false&key=ABQIAAAAhOYTJ_D7BinxvFiT95rfOhS_8Uw6SStDZi9m0gbiCYqHE4wcjhSXGCSAq6wb4wjd6h9DDN22ga8yaw' % i.addres.encode('utf-8'))
    cs = csv.reader(page)
    print i.name.encode('utf-8')
    for u in cs:
      i.geostatus = u[0]
      i.geoacc = u[1]
      i.geolat = db.GeoPt(u[2],u[3])
    i.put()
  except:
    pass

memcache.replace('geono',geono+5)
logging.info('Geono: %s' % geono)
