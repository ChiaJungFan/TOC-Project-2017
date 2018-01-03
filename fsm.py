from transitions.extensions import GraphMachine
# -*- coding: utf8 -*-
from lxml import etree, html
from bs4 import BeautifulSoup
import requests, json


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == 'breakfast'

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == 'drink'

    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == 'food'

    def on_enter_state1(self, update):
        update.message.reply_text("https://www.google.com.tw/search?client=ubuntu&hs=5Xn&channel=fs&dcr=0&ei=dfRMWuPmBsWi0QTct7S4AQ&q=%E6%88%90%E5%A4%A7%E6%97%A9%E9%A4%90&oq=%E6%88%90%E5%A4%A7%E6%97%A9%E9%A4%90&gs_l=psy-ab.3..0l3j0i5i30k1.9444.23297.0.23747.4.4.0.0.0.0.90.302.4.4.0....0...1c..64.psy-ab..0.4.300...0i67k1.0.cMEfyaJ8Wq0")
        
#        result = requests.get("http://www.atmovies.com.tw/showtime/t07703/a07/")
#        print(result.text)
#        result.encoding = 'utf8'
#        root = etree.fromstring(result.content, etree.HTMLParser())
#        name = root.xpath("//div[@id='theaterShowtimeBlock']/a/text()")
#        name2 = root.xpath("//strong[contains(@class, 'col-xs-12 LangTW Movi    eName')]")
#       print(name)
#        print('hi')
#       jsonData = "["
#        for row in root.xpath("//table[@class='table']/tr[position()>1]"):
#            column = row.xpath("./td/text()")
#            tmp = '{"name": "%s", "grades":{"chinese": %s, "math": %s, "science": %s, "soc": %s, "health": %s}},' %(column[0], column[1], column[2], column[3], column[4], column[5])
#           jsonData += tmp
# print(jsonData[0:-1] + ']')

#        target = 'http://web.vscinemas.com.tw/ShowTimes/'
#        req = requests.get(url = target)
#        html = req.text
#        bf = Beautiful(html)
#        texts = bf.find('strong', class_ = 'col-xs-12 LangTW MovieName')
#        print(texts)

        self.go_back(update)

    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_enter_state2(self, update):
        update.message.reply_text("https://www.google.com.tw/search?client=ubuntu&hs=CtS&channel=fs&dcr=0&ei=j_RMWq6FCsvC0gSs27HYDw&q=%E6%88%90%E5%A4%A7%E9%A3%B2%E6%96%99&oq=%E6%88%90%E5%A4%A7%E9%A3%B2%E6%96%99&gs_l=psy-ab.3..0l2.146130.148640.0.149214.3.3.0.0.0.0.114.243.2j1.3.0....0...1c..64.psy-ab..0.3.242...38j0i67k1j0i5i30k1.0.YHtXqcrlj-8")
        self.go_back(update)

    def on_exit_state2(self, update):
        print('Leaving state2')

    def on_enter_state3(self, update):
        update.message.reply_text("https://www.google.com.tw/search?client=ubuntu&channel=fs&dcr=0&ei=FvZMWrjVBoLt0ASS8r_QBg&q=%E6%88%90%E5%A4%A7%E7%BE%8E%E9%A3%9F&oq=%E6%88%90%E5%A4%A7&gs_l=psy-ab.1.5.0i67k1j0l2j0i67k1l4j0l3.109400.109623.0.113328.2.2.0.0.0.0.99.165.2.2.0....0...1c.1.64.psy-ab..0.2.163....0.RjL4ABUViZ8")
        self.go_back(update)

    def on_exit_state3(self, update):
        print('Leaving state3')
