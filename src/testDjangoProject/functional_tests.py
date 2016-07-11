# -*- coding: utf-8 -*-
from selenium import webdriver
#引用标准的 unittest 模块



browser = webdriver.Firefox()
browser.get('http://localhost:8080')

assert 'To-do' in browser.title()

browser.quit()
