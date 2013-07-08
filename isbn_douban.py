#!/usr/bin/python -tt
#!coding:utf8

import webbrowser
import urllib
import urllib2
from douban_client import DoubanClient
################
['{"access_token":"80dce6eac862de188296b4c059289a48","douban_user_id":"4191766","expires_in":604800,"refresh_token":"40b201579ee1ad76c2160406dca50862"}']
################
#data = {}
#secret = {}
#
#data['client_id'] = '09b8939a3413aad21d29bace9c3b0076'
#data['redirect_uri'] = 'http://bearzk.wordpress.com/'
#data['scope'] = 'book_basic_r,book_basic_w'
#data['response_type'] = 'code'
#secret['client_secret']  = '9859991d44544cb1'
#secret['code'] = 'b09c29a3f4af1ccb'
#
#newdata = urllib.urlencode(data)
#
#client_id = 'client_id=09b8939a3413aad21d29bace9c3b0076'
#redirect_uri = '&redirect_uri=http://bearzk.wordpress.com/'
#scope = '&book_basic_r,book_basic_w'
#response_type = '&response_type=code'
#
#grant_type = '&grant_type=authorization_code'
#code = '&code=b09c29a3f4af1ccb'
#
#
#url = 'https://www.douban.com/service/auth2/auth?'
#url = url + client_id + redirect_uri + scope + response_type
#
#print url,'\n'
#
##webbrowser.open(url,2)
#
#post = '&' + urllib.urlencode(secret)
#
#turl = 'https://www.douban.com/service/auth2/token?'
#post =  client_id + redirect_uri + grant_type + post
#
#print turl
#print post
#
#f = urllib2.urlopen(turl,post)
#print f.readlines()

key = '09b8939a3413aad21d29bace9c3b0076' 
secret = '9859991d44544cb1'
redirect = 'http://bearzk.wordpress.com/'
token = '80dce6eac862de188296b4c059289a48'

client = DoubanClient(key,secret,redirect)
client.auth_with_token(token)

g = client.book.getter()
print g
