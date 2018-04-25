# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 11:30:28 2018

@author: bsuzow
"""
import requests
from bs4 import BeautifulSoup
#import time
import re

def Read_HTML(url,daynum):
    """
    Crawls and extracts text in interest of the html page.  This function is written for web scraping of the FB CEO senate hearings held in April 2018. The transcripts are available on the Washington Post site. As such, the code is taylored to crawal the WP pages. 
    Arguments:
        url: web address of the transcript
        daynum: 1 for the first day of the hearing; 2 for the 2nd
    Outout:
        A text file named FB_CEO_hearing_Day#.txt containg the scraped paragraphs (all text enclosed in <p> tags).
    Return values:
        1. paragraphs scraped from the WP web page for all spoken in a list obj
        2. paragraphs scraped from the WP web page for FB CEO's remarks in a list obj
    """
    r = requests.get(url)
    html = r.text  # convert the html code of the page to a long string
    soup = BeautifulSoup(html,"html.parser")           
	
    """ 
    The hearing transcript is rendered in the <p> tags.
    """
    """
    If the content of the <p> tag is:
        start of FB CEO's remark (^zuckerberg:)
            append to the FB_CEO list as a new elemt
            write to csv
        FB CEO's remark continuation
            append to the FB_CEO list as a new elemt
            write to csv
        start of a senator's remark (^senator_name:)
            increment FB CEO list element counter
        A senator's remark continuation
            skip
    """
    p_list = []
    p_index = 0
    FB_CEO = []
    FB_CEO_p = False
    FB_CEO_index = 0
    
    file_name = "FB_CEO_hearing_Day" + str(daynum) + ".txt"
    with open(file_name,'w') as txtfile:
    
        for tag in soup.findAll('p'):  # harvest all <p> tags
            txt = tag.renderContents() # extract contents
            txt = txt.decode('utf-8')  # convert from bytes to string
            
            # any lines starting with <, skip.
            if not(re.search("^<",txt)):
                if re.search("^mark\\szuckerberg:|^zuckerberg:",txt.lower()):  # head of para by zuckerberg
                   # add to the FB_CEO list if zuckerberg's remarks
                   # remove "ZUCKERBERG:" or "MARK ZUCKERBERG:"
                   
                   FB_CEO.append(txt.split(":")[1])
                   FB_CEO_index +=1
                   txtfile.write(txt.split(":")[1])
                   txtfile.write("\n")
                   FB_CEO_p = True
                   
                   #print(txt)
                elif re.search("^[A-Z]+:|^REP\.|^SEN\.",txt): # head of a para by senator or rep
                    if FB_CEO_p:  # txt is part of FB CEO's
                        #print("FB CEO index: {}".format(FB_CEO_index))
                        
                        FB_CEO_p = False
                else:  
                    if FB_CEO_p:
                        FB_CEO.append(txt)
                        FB_CEO_index +=1
                        txtfile.write(txt)
                        txtfile.write("\n")
                        
                p_list.append(txt)
                p_index += 1
                
    return p_list, FB_CEO  # list objects  