""" Data property. """

from google.appengine.ext import db


class angeldata(db.Model):

  datas = db.StringProperty()
  created_at = db.DateTimeProperty(auto_now_add = True)
