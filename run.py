#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Meituan api spider's main runtime program file. In this file, we instantialize
an instance of MT_spider.
'''

from spider_develop import MeituanSpider


# save_mode 

# spider = MeituanSpider(save_mode='txt')
spider = MeituanSpider(save_mode='csv')
# spider = MeituanSpider(save_mode='db')

spider.run()
