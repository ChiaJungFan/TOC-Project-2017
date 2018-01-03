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
        return text.lower() == 'list all'

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == 'go to state2'

    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == 'go to state3'

    def on_enter_state1(self, update):
        update.message.reply_text("I'm entering state1")
        
        result = requests.get("http://web.vscinemas.com.tw/ShowTimes/")
        result.encoding = 'utf8'
        root = etree.fromstring(result.content, etree.HTMLParser())
        name = root.xpath("//strong[contains(@class, 'col-xs-12 LangTW MovieName')]")
        name2 = root.xpath("//strong[contains(@class, 'col-xs-12 LangTW Movi    eName')]")
        print(name)
        print(name2)
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
        update.message.reply_text("I'm entering state2")
        self.go_back(update)

    def on_exit_state2(self, update):
        print('Leaving state2')

    def on_enter_state3(self, update):
        update.message.reply_text("I'm entering state3")
        self.go_back(update)

    def on_exit_state3(self, update):
        print('Leaving state3')
