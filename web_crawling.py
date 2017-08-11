import csv
from pandas import DataFrame
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError

"""""""""""""""""""""""""""
Get the title of the page
"""""""""""""""""""""""""""
def Gettitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bs = BeautifulSoup(html , "lxml")
        title = bs.find_all("title")
    except AttributeError as e:
        return None
    return [titl.get_text().strip() for titl in title][0]

""""""""""""""""""""""
Get the Item title function
"""""""""""""""""""""    
def GetItemTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e :
        print(e)
        return None
    try:
        bs = BeautifulSoup(html, 'lxml')
        item = bs.find_all("h1" , {"class" : "itemTitle"})
    except AttributeError as e : 
        return None
    return [itm.get_text().strip() for itm in item] 

""""""""""""""""""""""
Get the Item price function
"""""""""""""""""""""    
def GetItemPrice(url):
    try:
        html = urlopen(url)
    except HTTPError as e :
        print(e)
        return None
    try:
        bs = BeautifulSoup(html, 'lxml')
        item = bs.find_all("h3" , {"class" : "itemPrice"})
    except AttributeError as e : 
        return None
    return [itm.get_text().strip() for itm in item] 
 
""""""""""""""""""""""
Get the Item images function
"""""""""""""""""""""   
def GetItemImage(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bs = BeautifulSoup(html, 'lxml')
    except AttributeError as e : 
        return None
    return [raw_img['src'] for raw_img in bs.find_all('img', 
        {"class" : "img-size-medium lazy-loaded imageUrl"})]

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Scraping the first 3 pages in souq.com and use the previous functions 
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""    
#url = "https://egypt.souq.com/eg-en/mobile-phone/l/?&sortby=sr&section=2&page=2"

print(Gettitle("https://egypt.souq.com/eg-en/mobile-phone/l/?sortby=sr&section=2&page=1"))

m = 1

for i in range(3):   
    url ="https://egypt.souq.com/eg-en/mobile-phone/l/?sortby=sr&section=2&page="+str(i+1)+""
    itemtitle = GetItemTitle(url)
#    itemtitle2.extend(itemtitle)
    itemprice= GetItemPrice(url)
#    itemprice2.extend(itemprice)
    itemimgs = GetItemImage(url)
#    itemimgs2.extend(itemimgs)
    itemlist = list(zip(itemtitle, itemprice, itemimgs))
        
    df = DataFrame({'itemtitle': itemtitle, 'itemprice': itemprice, 'itemimage': itemimgs})

    df.to_excel('E:\\WORK\\PROGRAMMER\\10)webCrawling\\souq.com\\Page'+str(i+1)+'.xlsx', 
                   sheet_name='sheet1', 
                   index=False,
                   header=False
                   )
        
    
    
    
    for img in itemimgs :
        imgurl = urlopen(img)
        output = open("E:\\WORK\\PROGRAMMER\\10)webCrawling\\souq.com\\img"+str(m)+".jpg","wb")
        output.write(imgurl.read())
        output.close()
        m+=1
    
    
    
    
