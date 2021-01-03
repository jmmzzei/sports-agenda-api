from django.shortcuts import render
from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv 
import time
import os
import re

load_dotenv('.env')

def index(arg1):
    return HttpResponse('hello')

def we(arg1):
    arr = []
    browser = webdriver.Firefox()
    browser.get(os.getenv('BASE_URL'))
    browser.implicitly_wait(1)

    for date in browser.find_elements_by_css_selector(os.getenv('DATE')):
        inDate = {"date": '', "tournament": '', "events": [] }
        cDate = date.find_elements_by_css_selector(os.getenv('DATE_TITLE'))[0]
        inDate["date"] = cDate.text
        for tournament in date.find_elements_by_css_selector(os.getenv('TOURNAMENT')):
            for title in tournament.find_elements_by_css_selector(os.getenv('TOURNAMENT_TITLE')):
                inDate["tournament"] = title.text
            for ev in tournament.find_elements_by_css_selector(os.getenv('EVENT')):
                for events in ev.find_elements_by_css_selector(os.getenv('EVENT_SELECTOR')):
                    hour = events.find_element_by_css_selector(os.getenv('CUSTOM1'))
                    match = events.find_element_by_css_selector(os.getenv('CUSTOM2'))
                    tv = events.find_element_by_css_selector(os.getenv('CUSTOM3'))
                    obj = { 
                        match : match.text,
                        hour: hour.text,
                        tv: tv.text
                    }
                    inDate["events"].append(obj)
        arr.append(inDate)
    browser.quit()
    return HttpResponse(arr)
