import requests
import xml.etree.ElementTree as ET
from .models import accounts

def get_currentlyreading(req_type):
    good_reads_account = accounts.objects.get(name='goodreads')
    client_key = good_reads_account.key
    headers = {'Content-type': 'application/json'}
    reading = []
    reading_final = []
    if req_type != "":
        page = 1
        while page > 0:
            url_curl = 'https://www.goodreads.com/review/list/93087855.xml?key=' + client_key + '&v=2&shelf=' + req_type + '&per_page=50&page=' + str(page)
            print(url_curl)
            r = requests.get(url_curl, headers=headers)
            reading = set_reading_list(r.content)
            if reading:
                reading_final.extend(reading)
                page += 1
            else:
                page = 0

    return reading_final

def set_reading_list(content):

    readinglist = []
    e = ET.ElementTree(ET.fromstring(content))
    for elt in e.iter():
        if elt.tag == "title":
            title = elt.text
        if elt.tag == "image_url":
            image_url = elt.text
        if elt.tag == "name":
            author = elt.text
            readinglist.append([title, author, image_url])

    return readinglist
