import lxml.html
import requests
from nefuncs import IterPages,BoolToInt,getPIDS,getData

"""
http://m.newegg.com/ProductList?description=USCwlKSl76suit%252bEk6WP%252bN0X6p0HeDANTptHWEaWwMs%253d&storeid=1&categoryid=-1&nodeid=7671&storetype=2&subcategoryid=343&brandid=-1&nvalue=100007671&showseealldeals=False&itemcount=0&issubcategory=true&level=3
"""

baseurl = 'http://www.newegg.com/Processors-Desktops/SubCategory/ID-343'

pg1 = requests.get(baseurl).content

root1 = lxml.html.fromstring(pg1)
page_count = IterPages(root1)
URLs = ['%s&Page=%s' % (baseurl, pgnum) for pgnum in range(1, page_count + 1)]
# FETCH AND PARSE THE DATA
pids = getPIDS(URLs, root1)
df = getData(pids)

print df
