#!/usr/bin/env
# -*- coding: utf-8 -*-

import os
import urllib2
import re
from bs4 import BeautifulSoup as bs

BASE_URL = u"http://www.dw.de/"
YEAR_REGEX = u".*\d{4}$"
YEAR = re.compile(YEAR_REGEX)
ENTRY_REGEX = u".*a-\d{7}$"
ENTRY = re.compile(ENTRY_REGEX)
NOT = re.compile('^/top-thema.*')
FILENAME_REGEX = u"^/.*/"
FILENAME = re.compile(FILENAME_REGEX)
CONTENTID_REGEX = u'.*contentId_\d{7}.*'
CONTENTID = re.compile(CONTENTID_REGEX)

#############

url = ""
archive_urls = []
entry_urls = []
filenames = []

#############
def find_learn_german_link(url=BASE_URL):
	page = urllib2.urlopen(url)
	soup = bs(page)
	for link in soup.find_all('a',href=True):
		# print link
		if link.string == "LEARN GERMAN":
			url = link['href']
	return url


def find_level_b1(url):
	LEARN_GERMAN = urllib2.urlopen(url)
	soup = bs(LEARN_GERMAN)
	for link in soup.find_all('h2'):
		if link.string == "Level B1":
			url = link.parent['href']
	return url

def find_top_thema(url):
	LEVEL_B1 = urllib2.urlopen(BASE_URL + url)
	soup = bs(LEVEL_B1)
	for link in soup.find_all('h2'):
		if "Top-Thema" in str(link.string).split():
			url = link.parent['href']
	return url

def find_archiv(url):
	TOP_THEMA = urllib2.urlopen(url)
	soup = bs(TOP_THEMA)
	for link in soup.find_all('h2'):
		string = str(link.string)
		l = string.split()
		if "Archiv" in l and re.match(YEAR, string):
			archive_urls.append(BASE_URL + link.parent['href'])
	return archive_urls


def find_entries(url):
	archive_page = urllib2.urlopen(url)
	soup = bs(archive_page)

	for link in soup.find_all('a', href=True):
		url = link['href']
		if re.match(ENTRY, url) and not re.match(NOT,url) and "google" not in url:
			# print url
			entry_urls.append(BASE_URL + url)
			filename = re.findall(FILENAME, url)
			filenames.append(filename[0].strip('/').replace('-','_'))

	return entry_urls, filenames
	# entry_page = urllib2.urlopen(entry_urls[0])

	# soup = bs(entry_page)



def find_pdf_and_mp3_url(url):
	popup = ''
	pdf_url = ''
	mp3_url = ''
	entry_page = urllib2.urlopen(url)
	soup = bs(entry_page)
	for link in soup.find_all('a', href=True):
		if re.match(CONTENTID,link['href']) and 'audio' in link.parent['class']:
			popup = link['href']
		elif link['href'].endswith('pdf'or'PDF'or'Pdf'):
			pdf_url = link['href']
	mp3_page = urllib2.urlopen(BASE_URL + popup)
	soup = bs(mp3_page)
	for link in soup.find_all('a', href=True):
		if link['href'].endswith('mp3'or'MP3'):
			mp3_url = link['href']
	return mp3_url, BASE_URL + pdf_url


def download_and_save_under_name(url, path, name):
	source = urllib2.urlopen(url)
	if url.endswith("mp3" or "MP3"):
		with open(path + name +'.mp3', 'wb') as f:
			f.write(source.read())
			print name+'.mp3 saved.'
	else:
		with open(path + name+'.pdf', 'wb') as f:
			f.write(source.read())
			print name+'.pdf saved.'

def mkdir(cwd):
	if not os.path.exists(cwd+'\mp3'):
		os.mkdir(cwd+'\mp3')
	if not os.path.exists(cwd+'\pdf'):
		os.mkdir(cwd+'\pdf')

def main():
	cwd = os.getcwd()
	mkdir(cwd)
	learn_german_rel = find_learn_german_link(BASE_URL)
	learn_german_url = BASE_URL + learn_german_rel
	level_b1_rel = find_level_b1(learn_german_url)
	level_b1_url = BASE_URL + level_b1_rel
	top_thema_url = find_top_thema(level_b1_url)
	archive_urls = find_archiv(top_thema_url)
	entry_urls, filenames = find_entries(archive_urls[0])

	for i, v in enumerate(filenames):
		print i, v

	# download 1 file
	# mp3_url, pdf_url = find_pdf_and_mp3_url(entry_urls[79])
	# print mp3_url, pdf_url
	# download_and_save_under_name(mp3_url, cwd+'\\mp3\\', filenames[79])
	# download_and_save_under_name(pdf_url, cwd+'\\pdf\\', filenames[79])

	#download files
	for i, url in enumerate(entry_urls):
		mp3_url, pdf_url = find_pdf_and_mp3_url(url)
		download_and_save_under_name(mp3_url, cwd+'\\mp3\\', filenames[i])
		download_and_save_under_name(pdf_url, cwd+'\\pdf\\', filenames[i])


	print 'download finished.'


if __name__ == '__main__':
	import sys
	reload(sys)
	sys.setdefaultencoding('utf-8')
	main()