from bs4 import BeautifulSoup
import requests
import csv
import os

productlist = []

links = ["https://comme-des-garcons-online.com/category/item/converse/?fbclid=IwAR3IoNYSs1BJ855Mq51vsNuVXVmI-L9179sjtWl0W9FseViUgfzI6bzVJuU",
        "https://comme-des-garcons-online.com/category/item/converse/page/2/?fbclid=IwAR3IoNYSs1BJ855Mq51vsNuVXVmI-L9179sjtWl0W9FseViUgfzI6bzVJuU",
        "https://comme-des-garcons-online.com/category/item/converse/page/3/?fbclid=IwAR3IoNYSs1BJ855Mq51vsNuVXVmI-L9179sjtWl0W9FseViUgfzI6bzVJuU"]

for link in links:
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    productDivs = soup.findAll('div', attrs={'class' : 'itemimg'})
    #print(productDivs)
    for div in productDivs:
        productlist.append(div.a['href'])

#print(productlist)

with open('CDG.csv', mode='w') as csv_file:
    fieldnames = ['Japanese', 'NameRaw', "Name", "Yen",'PriceRaw', 'Profit', "Price", "SizesLabel","Imgs"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    
    for link in productlist:
    #     x += 1
        #page = requests.get("https://comme-des-garcons-online.com/play-converse-20ss-jp-low-bk/")
        page = requests.get(link)
        soup = BeautifulSoup(page.content, 'html.parser')
        division = str(soup.findAll("div", {"class": "item-description tab-box"}))

        productname = division[division.find('モデル名<br/>')+9:division.find("■色")].replace("</p>","").replace("<p>","").strip()
        #print(productname)

        sizes = division[division.find('サイズ対応（目安')+9:division.find("■素材")].replace("</p>","").replace("<p>","").replace("<br/>",",").replace("\n","").strip()
        #print(sizes)

        spanorigprice = str(soup.findAll("span", {"class": "field_cprice ss_cprice"}))
        origprice = spanorigprice[spanorigprice.find("¥")+1:spanorigprice.find("</span>]")].replace(",","")
        print(origprice)

        spansaleprice = str(soup.findAll("span", {"class": "sell_price ss_price"}))
        saleprice = spansaleprice[spansaleprice.find("¥")+1:spansaleprice.find("</span>]")].replace(",","")
        print(saleprice)

        extract_imglinks = []
        images = soup.findAll('img')
        x=0
        for image in images:
            #print image source
            if ".png" not in image['src']:
                extract_imglinks.append(image['src'])
                x += 1
                if x == 5:
                    break

        print(extract_imglinks)
        
        writer.writerow({'Japanese': productname, 'Yen': saleprice, 'PriceRaw': origprice ,'SizesLabel': sizes, 'Imgs': extract_imglinks[:5]})
            
                    