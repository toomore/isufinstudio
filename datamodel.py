""" Data property. """

from google.appengine.ext import db

class rossdatas(db.Model):

  datano = db.IntegerProperty()
  datas = db.StringProperty()
  created_at = db.DateTimeProperty(auto_now_add = True)

class startno(db.Model):

  finalno = db.IntegerProperty()
  worked_at = db.DateTimeProperty(auto_now = True)
