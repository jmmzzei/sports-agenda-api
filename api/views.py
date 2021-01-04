from django.shortcuts import render
from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from .models import Event
from dotenv import load_dotenv 
import time
import os
import re

load_dotenv('.env')

def getData():
    arr = []
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(options=options)

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
                        "match" : match.text,
                        "hour": hour.text,
                        "tv": tv.text
                    }
                    instance = Event.objects.create(date=inDate["date"], tournament=inDate["tournament"], hour=hour.text, match=match.text, tv=tv.text)
                    print(instance)
                    inDate["events"].append(obj)
        arr.append(inDate)
    browser.quit()
    return arr

def index(arg1):
    return HttpResponse('hello')

def we(arg1):
    first_event_date = Event.objects.filter(date="LUNES 04 DE ENERO")
    print(first_event_date[0])
    return HttpResponse(first_event_date[0])
    # arr = getData()
    # return HttpResponse(arr)

def time(request, date):
    arr = getData()    
    dateMapper = {
        "today": 1,
        "tomorrow": 2,
        "day-after-tomorrow": 3
    }
    index = dateMapper[date]
    print(arr[index])
    return HttpResponse(arr[index])
