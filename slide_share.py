#!/usr/bin python3

'''
	A Simple Script used to extract images from url and convert into pdf format
	Author : iam048
	10/02/2018
'''

import requests, re, urllib, os
from fpdf import FPDF
from libs.colors import *
from libs.amutils import *

value = 'Slide Share'
utils.banner(value)

def processor():
	print("[+] Found %s slides" % len(image_list))
	os.mkdir("temp")
	Make_pdf()
	the_end()

def Make_pdf():
	no, left, top = 0, 20, 10
	print("[*] Grabbing Images")
	with Spinner():
		for image in image_list:
			pdf.add_page('L') # adding new page to the pdf
			pdf.image(urllib.request.urlretrieve(image_list[no], 'temp/'+ str(no) + '.jpg')[0], left, top) # inserting target image into the current page
			no += 1

def the_end():
	pdf.output("test.pdf", "F") #output as pdf format 

if __name__ == '__main__':
	try:
		url = input("Enter the URL : ")
		content = requests.get(url).text
		image_list = re.findall(r'normal="(.*?)[?]', content)
		pdf = FPDF()	# parser for the pdf
		processor()
	except Exception as e:
		print(R, e)
