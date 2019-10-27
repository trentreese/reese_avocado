import requests
import xml.etree.ElementTree as ET
from .models import accounts

def get_currentlyreading(req_type):
    good_reads_account = accounts.objects.get(name='goodreads')
    client_key = good_reads_account.key
    headers = {'Content-type': 'application/json'}
    reading = []
    if req_type != "":
        url_curl = 'https://www.goodreads.com/review/list/93087855.xml?key=' + client_key + '&v=2&shelf=' + req_type + '&per_page=200&page=1'
        r = requests.get(url_curl, headers=headers)
        e = ET.ElementTree(ET.fromstring(r.content))
        for elt in e.iter():
            if elt.tag == "title":
                title = elt.text
            if elt.tag == "image_url":
                image_url = elt.text
            if elt.tag == "name":
                author = elt.text
                reading.append([title, author, image_url])

    return reading
