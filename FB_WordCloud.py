# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 09:33:29 2018

@author: bsuzow

ref: http://ramiro.org/notebook/sherlock-holmes-canon-wordcloud/

https://github.com/amueller/word_cloud/blob/master/examples/masked.py 

https://amueller.github.io/word_cloud/generated/wordcloud.WordCloud.html
"""

try:
    import wordcloud
except:
    import pip
    pip.main(['install','wordcloud'])

import random
import matplotlib as mpl
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from scipy.misc import imread

# HSL color picker http://hslpicker.com/#0f17ff

def grey_color(word, font_size, position, orientation, random_state=None, **kwargs):
    #return 'hsl(0, 0%%, %d%%)' % random.randint(50, 100)
    return 'hsl(240,100%%,%d%%)' % random.randint(1,50)

def word_cloud(text):
    """
    Plot a wordcloud using FB CEO congressional hearing text.

    """
    #mpl.style.use('dark')
    limit = 200
    infosize = 12
    
    #chartinfo = 'Author: Bo Suzow'
    #footer = "Frequently spoken words.\n{}".format(limit, chartinfo)
    #font = '/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-B.ttf'
    #fontcolor='#fafafa'   # gray98
    #bgcolor = '#000000'  # black
    bgcolor = "#FFFFFF"   # white
    wordcloud = WordCloud(
    max_words=limit,
    #stopwords=english_stopwords,
    
    # FB Logo souce: https://www.freepik.com/free-icon/facebook-logo_736921.htm
    mask=imread('facebook-logo_318-49940.jpg'),
    background_color=bgcolor,
    collocations = False
    #font_path=font
    ).generate(text)
    
    fig = plt.figure()
    fig.set_figwidth(14)
    fig.set_figheight(18)
    
    plt.imshow(wordcloud.recolor(color_func=grey_color, random_state=3),interpolation="bilinear")
    
    #plt.title(title, color=fontcolor, size=30, y=1.01)
    #plt.annotate(footer, xy=(0, -.025), xycoords='axes fraction', fontsize=infosize, color=fontcolor)
    plt.axis('off')
    plt.show()
    
    return wordcloud
