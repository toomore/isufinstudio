#!/usr/bin/env python
# -*- coding: utf-8 -*-

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.api import memcache
from datamodel import rosst
import logging

class index(webapp.RequestHandler):
  """ index page.
  """
  def get(self):
    q = {
              '1':'食品',
              '2':'紡織',
              '3':'服飾',
              '4':'皮革',
              '5':'木竹及傢俱',
              '6':'造紙及印刷',
              '7':'化學材料',
              '8':'化學製品',
              '9':'石油煤製品',
              '10':'橡膠製品',
              '11':'塑膠製品',
              '12':'非金屬礦物製品',
              '13':'基本金屬',
              '14':'金屬製造',
              '15':'機械、公害防治設備',
              '16':'電器及電子',
              '17':'運輸工具',
              '18':'精密器機',
              '19':'雜項工業'
            }
    m = ''
    for t in q.keys():
      m = m + "<a href='./?q=%s'>%s</a>." % (t,q[t])

    if self.request.get('q'):
      noq = self.request.get('q')
    else:
      noq = '13'

    noc = memcache.get(noq)
    qti = q[noq]

    self.response.out.write(template.render('./template/htm_index.htm',{'qw':noq,'menu':m,'ti':qti,'noc':noc}))

class opmap(webapp.RequestHandler):
  """ Output map.
  """
  def get(self):

    q = {
          '1':'食品',
          '2':'紡織',
          '3':'服飾',
          '4':'皮革',
          '5':'木竹及傢俱',
          '6':'造紙及印刷',
          '7':'化學材料',
          '8':'化學製品',
          '9':'石油煤製品',
          '10':'橡膠製品',
          '11':'塑膠製品',
          '12':'非金屬礦物製品',
          '13':'基本金屬',
          '14':'金屬製造',
          '15':'機械、公害防治設備',
          '16':'電器及電子',
          '17':'運輸工具',
          '18':'精密器機',
          '19':'雜項工業'
        }

    b = memcache.get(self.request.get('q'),'njnj')

    if b is None:
      b = []
      a = rosst.gql("where datacno = '%s' " % (q[self.request.get('q')]).decode('utf-8'))
      noc = a.count()
      memcache.add(self.request.get('q'),noc,3600*6)
      logging.info('Add noc cache: %s' % noc)
      for i in a:
        try:
          b.append({
                    'lat':i.geolat.lat,
                    'lon':i.geolat.lon,
                    'datacno':i.datacno.encode('utf-8'),
                    'addres':i.addres.encode('utf-8'),
                    'mpo':i.mpo.encode('utf-8'),
                    'mso':i.mso.encode('utf-8'),
                    'name':i.name.encode('utf-8')
                   })
        except:
          pass

      memcache.add(self.request.get('q'),b,3600*6,namespace='njnj')
      logging.info('Add cache: %s' % self.request.get('q'))

    self.response.headers['Content-Type'] = 'text/xml'
    self.response.out.write(template.render('./template/map.kml',{'b':b}))

class flush(webapp.RequestHandler):
  """ Output map.
  """
  def get(self):
    memcache.flush_all()
    self.redirect('/')

def main():
  """ Start up. """
  application = webapp.WSGIApplication([
                                        ('/', index),
                                        ('/map.kml', opmap),
                                        ('/flush', flush)
                                      ],debug=True)
  run_wsgi_app(application)

if __name__ == '__main__':
  main()
