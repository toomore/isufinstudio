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
    data = data.replace(' ','')
    data = data.replace('\n','')
    data = data.replace('\r','')
    data = data.replace(',','')
    data = data.replace('一','1')
    data = data.replace('二','2')
    data = data.replace('三','3')
    data = data.replace('四','4')
    data = data.replace('五','5')
    data = data.replace('六','6')
    data = data.replace('七','7')
    data = data.replace('八','8')
    data = data.replace('九','9')
    data = data.replace('Ｏ','0')
    data = data.replace('NT.$','')

    if data == '':
      pass
    elif data == 'e-mail':
      pass
    elif data == 'ADD':
      pass
    elif data == 'TEL':
      pass
    elif data == 'FAX':
      pass
    elif data == '負責人':
      pass
    elif data == '資本額':
      pass
    elif data == '員工人數':
      pass
    elif data == '人':
      pass
    elif data == '網　址':
      pass
    elif data == '主要產品':
      pass
    elif data == '備　註':
      pass
    elif data == '價格:':
      pass
    else:
      self.datas.append(data)

class intodatas:
  def __init__(self,per=5):
    from datamodel import startno

    #a = startno(finalno = 98).put()
    self.datasos = startno.all().get()
    self.no = self.datasos.finalno
    self.per = per

  def rungo(self):
    self.catchdatas(self.no,self.per)

  def catchdatas(self,start,per):
    from datamodel import rossdatas
    iii = ''
    for i in range(0,per):
      no = self.no + i
      response = urllib2.urlopen('http://www.efincs.net/twe/print_product_info.php?products_id=%s' % no)
      page = response.read()
      html_code = page.decode('big5').encode('utf-8')
      hp = MyHTMLParser()
      hp.feed(html_code)
      hp.close()

      for ii in hp.datas:
        iii = iii + ii.decode('utf-8') + ','

      rossdatas(datas = iii,datano = int(no),key_name = str(no)).put()
      iii = ''

    self.datasos.finalno = self.no + per + 1
    self.datasos.put()
