#!/usr/bin/env python
# -*- coding: utf-8 -*-

from google.appengine.ext import db
from google.appengine.tools import bulkloader
import datamodel
#from datamodel import rosst

class rossload(bulkloader.Loader):
  def __init__(self):
    bulkloader.Loader.__init__(self, 'rosst',
             [('datano', lambda x: x.decode('utf-8')),
              ('datacno', lambda x: x.decode('utf-8')),
              ('name', lambda x: x.decode('utf-8')),
              ('phone', lambda x: x.decode('utf-8')),
              ('fax', lambda x: x.decode('utf-8')),
              ('addres', lambda x: x.decode('utf-8')),
              ('mpo', lambda x: x.decode('utf-8')),
              ('mso', lambda x: x.decode('utf-8'))
             ])

loaders = [rossload]
