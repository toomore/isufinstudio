#!/usr/bin/env python
# -*- coding: utf-8 -*-

from HTMLParser import HTMLParser
import urllib2

class MyHTMLParser(HTMLParser):
  def __init__(self):
    HTMLParser.__init__(self)
    self.links = []
    self.datas = []

  def handle_starttag(self, tag, attrs):
    #print "Encountered the beginning of a %s tag" % tag
    if tag == "a":
      if len(attrs) == 0:
        pass
      else:
        for (variable, value)  in attrs:
          if variable == "href":
            self.links.append(value)

  def handle_data(self,data):
    self.datas.append(data)

class intodatas:
  def __init__(self,per=5):
    '''
    from datamodel import startno

    #a = startno(finalno = 98).put()
    self.datasos = startno.all().get()
    self.no = self.datasos.finalno
    self.per = per
    '''
    self.no = 0
    self.per = 0

  def rungo(self):
    self.catchdatas(self.no,self.per)

  def catchdatas(self,start=0,per=2):
    #from datamodel import rossdatas
    iii = ''
    #for i in range(0,per):
      #try:
    #no = self.no + i
    response = urllib2.urlopen('http://mis.tse.com.tw/Best5_new.html?StkNo=%s' % '2323')
    page = response.read()
    #html_code = page.decode('big5').encode('utf-8')
    html_code = page.decode('big5')
    hp = MyHTMLParser()
    hp.feed(html_code)
    hp.close()

    for ii in hp.datas:
      iii = iii + ii.encode('utf-8') + ','

    print iii
    #rossdatas(datas = iii,datano = int(no),key_name = str(no)).put()
    iii = ''
      #except:
        #pass

    #self.datasos.finalno = self.no + per + 1
    #self.datasos.put()
