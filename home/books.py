import xmltodict
import goodreads
from requests_oauthlib import OAuth1Session
import requests
from requests_oauthlib import OAuth1
from goodreads import client
from goodreads.user import GoodreadsUser
from goodreads.shelf import GoodreadsShelf
#import session
#import oauth2 as oauth
import urllib
import sys
from urllib import parse
import xml.etree.ElementTree as ET

def get_currentlyreading():
	gc = client.GoodreadsClient('KieVMozaGh1Vtjf95ymaw','kBQcjRMivcHAQKfJEYWfd6JjjExaUrPCfEfXwgy8FD4')
	url = 'http://www.goodreads.com'
	request_token_url = '%s/oauth/request_token' % url
	authorize_url = '%s/oauth/authorize' % url
	access_token_url = '%s/oauth/access_token' % url

	client_key='KieVMozaGh1Vtjf95ymaw'
	client_secret='kBQcjRMivcHAQKfJEYWfd6JjjExaUrPCfEfXwgy8FD4'


		# oauth = OAuth1Session(client_key, client_secret=client_secret)
		# fetch_response = oauth.fetch_request_token(request_token_url)
		# resource_owner_key = fetch_response.get('oauth_token')
		# resource_owner_secret = fetch_response.get('oauth_token_secret')

		# base_authorization_url = authorize_url
		# authorize_url = base_authorization_url + '?oauth_token='
		# authorize_url = authorize_url + resource_owner_key
		# print(authorize_url)
		# verifier = input('Please input the verifier')

		# oauth = OAuth1Session(client_key,
		#                           client_secret=client_secret,
		#                           resource_owner_key=resource_owner_key,
		#                           resource_owner_secret=resource_owner_secret,
		#                           verifier=verifier)
		# oauth_tokens = oauth.fetch_access_token(access_token_url)
		# print(oauth_tokens)

		# key = fetch_response.get('oauth_token')
		# secret = fetch_response.get('oauth_token_secret')
		# print(key, secret)
	key = 'xPL1Z7ySP9N38eSon4LP7w'
	secret = 'zilIhfFrCHRbZDU7Ok24ZEAPM1RAlwXF8Jbw2kAS0'
	gc.authenticate(key, secret)

	user = gc.user(6111554)
	headers = {
	    'Content-type': 'application/json',
	}
	url_curl = 'https://www.goodreads.com/review/list/93087855.xml?key=' + client_key + '&v=2&shelf=currently-reading&per_page=200&page=1'
	r = requests.get(url_curl, headers=headers)
	e = ET.ElementTree(ET.fromstring(r.content))
	reading = []
	for elt in e.iter():
		if elt.tag == "title":
			title = elt.text
		if elt.tag == "image_url":
			image_url = elt.text
		if elt.tag == "name":
			author = elt.text
			reading.append([title, author, image_url])

	return reading
#user = gc.user(6111554)
#print(user.shelves(0))
#sys.exit()


#user = gc.user(6111554)
#l = user.shelves.list()

#owned_books = user.owned_books()
