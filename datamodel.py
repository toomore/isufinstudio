#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Data property. """

from google.appengine.ext import db

class rosst(db.Model):

  datano = db.StringProperty()
  datacno = db.StringProperty()
  name = db.StringProperty()
  phone = db.StringProperty()
  fax = db.StringProperty()
  addres = db.StringProperty()
  mpo = db.StringProperty()
  mso = db.StringProperty()
  geostatus = db.StringProperty()
  geoacc = db.StringProperty()
  geolat = db.GeoPtProperty()
  created_at = db.DateTimeProperty(auto_now_add = True)
