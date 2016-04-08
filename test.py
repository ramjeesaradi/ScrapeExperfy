'''
Created on 08-Apr-2016

@author: ramjeesaradi
'''

from lxml import html
import requests

def main():
    page = requests.get('https://www.experfy.com')
    tree = html.fromstring(page.content)
    #This will create a list of buyers:
    pracAreaslinks = tree.xpath('//a[@class="ga-track-event mixpanel-track-event" and @data-gae-category="Practice Area"]/./@href')
    pracAreas = tree.xpath('//a[@class="ga-track-event mixpanel-track-event" and @data-gae-category="Practice Area"]/./@data-mixpanel-name')
    for i in range(len(pracAreaslinks)):
        page = requests.get('https://www.experfy.com'+pracAreaslinks[i])
        tree = html.fromstring(page.content)
        caseStudy = tree.xpath('//a[@data-mixpanel-event="View Case Study"]/./@data-mixpanel-name')
        print pracAreas[i] + " - " + ", ".join(caseStudy)
#     pracAreas = pracAreas.remove("")
    #This will create a list of prices
#     print 'PA: ', ", ".join(pracAreas)
if __name__ == '__main__':
    main()
    
