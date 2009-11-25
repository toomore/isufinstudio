#!/usr/bin/env python
# -*- coding: utf-8 -*-
#coding: utf-8
#http://www.liao123.net/cms/show_article/32007.html

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

if __name__ == "__main__":
    iii = ''
    print '123'

    for i in range(98,102):
      response = urllib2.urlopen('http://www.efincs.net/twe/print_product_info.php?products_id=%s' % i)
      page = response.read()
      html_code = page.decode('big5').encode('utf-8')
      hp = MyHTMLParser()
      hp.feed(html_code)
      hp.close()

      #print(html_code)
      #print(hp.links)

      for ii in hp.datas:
          iii = iii + ii + ','
      print iii
      iii = ''
      #print hp.datas + ','
