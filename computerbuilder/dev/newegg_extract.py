import requests
import lxml, lxml.html
import json

"""

r = requests.api.get('http://www.ows.newegg.com/Stores.egg/Menus')
print [store['StoreID'] for store in json.loads(r.content)]

# Computer Hardware "StoreID" : 1

r = requests.api.get(
      'http://www.ows.newegg.com/Stores.egg/Categories/1')
for cat in json.loads(r.content):
    print cat
    print '\n'

"""

"""
Newegg Categories

Name NodeId CategoryId : Subcategory CategoryId NodeId

Fans/Cooling 6648 
Monitors 6652
Sound Cards 25014

Cases 6644 9 : 7 7583
CPUs 6676 34 : 343 7671
Hard Drives 6670 15 : Internal 338 22264
                    : SSDs 119 11389 : 636 8120

SSDs 11692 119 11689 ?

Memory 6650 17 : 147 7611
Motherboards 6654 : Intel 280 7627
                  : AMD 22 7625
Video Cards 6662 38 : 48 7709
"""

def newegg_items_page_req(node, page):
    r = requests.api.post(
      'http://www.ows.newegg.com/Search.egg/Advanced', 
      json.dumps({'NodeId':node, 'PageNumber':page})
    )
      #'''{"NodeId":6642,"PageNumber":%i}''' % page)
    
    prodlist = json.loads(r.content)['ProductListItems']
    if prodlist is None: return False
    
    items = [
      (item['Title'], float(item['OriginalPrice'][1:].replace(',', ''))) 
      for item in prodlist
    ]

    return items

def newegg_items(node):
    last_res = list()
    page = 0
    while last_res != False:
        yield last_res
        page += 1
        last_res = newegg_items_page_req(node, page)

def part_list(node):
    part_list = list()
    for page in newegg_items(node):
        part_list += page
    return part_list

def case_list():
    return part_list(7583)

def cpu_list():
    list = part_list(7671)
    '''
    for name, price in list:
        print name[:20], price
    '''
    return part_list(7671)

def mobo_list_intel():
    return part_list(7627)

def mobo_list_amd():
    return part_list(7625)

def mem_list():
    return part_list(7611)

def hdd_list():
    return part_list(22264)

def ssd_list():
    return part_list(8120)

def gpu_list():
    return part_list(7709)


part_list = hdd_list()

for name, price in part_list:
    for i in name:
        i.replace('\"', '\\"')
    print "[\"", name, "\",", price, "],"

