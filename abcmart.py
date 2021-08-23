from bs4 import BeautifulSoup
import requests
import csv
import os
from googletrans import Translator

translator = Translator()
# Brands = ["ADIDAS","NIKE","FILA","CONVERSE","VANS","NEWBALANCE","PUMA","BIRKENSTOCK","SPERRY"]
# Links = ["https://www.abc-mart.net/shop/goods/search.aspx?fssort=price&fsstock=1&fssales=1&fsbrand=adidas&fscategory=all&fsgender=all&fssize=all&fscolor=all&p=PAGE##goodslist"
# ,"https://www.abc-mart.net/shop/goods/search.aspx?fssort=price&fsstock=1&fssales=1&fsbrand=NIKE&fscategory=all&fsgender=all&fssize=all&fscolor=all&p=PAGE##goodslist"
# ,"https://www.abc-mart.net/shop/goods/search.aspx?fssort=price&fsevent=&fsstock=1&fssales=1&keyword=&fsbrand=FILA&fsseries=&fscategory=all&fsgender=all&fssize=all&fscolor=all&fsmaterial=&fswidth=&fsprice-low=&fsprice-high=#goodslist"
# ,"https://www.abc-mart.net/shop/goods/search.aspx?fssort=price&fsstock=1&fssales=1&fsbrand=CONVERSE&fscategory=all&fsgender=all&fssize=all&fscolor=all&p=PAGE##goodslist"
# ,"https://www.abc-mart.net/shop/goods/search.aspx?fssort=price&fsstock=1&fssales=1&fsbrand=VANS&fscategory=all&fsgender=all&fssize=all&fscolor=all&p=PAGE##goodslist"
# ,"https://www.abc-mart.net/shop/goods/search.aspx?fssort=price&fsstock=1&fssales=1&fsbrand=New+Balance&fscategory=all&fsgender=all&fssize=all&fscolor=all&p=PAGE##goodslist"
# ,"https://www.abc-mart.net/shop/goods/search.aspx?fssort=price&fsstock=1&fssales=1&fsbrand=PUMA&fscategory=all&fsgender=all&fssize=all&fscolor=all&p=PAGE##goodslist"
# ,"https://www.abc-mart.net/shop/goods/search.aspx?fssort=price&fsstock=1&keyword=birkenstock&fsbrand=all&fscategory=all&fsgender=all&fssize=all&fscolor=all&p=PAGE##goodslist"
# ,"https://www.abc-mart.net/shop/goods/search.aspx?fssort=price&fsstock=1&fssales=1&fsbrand=SPERRY+TOPSIDER&fscategory=all&fsgender=all&fssize=all&fscolor=all&p=PAGE##goodslist"]
# PageNumber = [10,7,1,3,15,10,13,2,5]

Brands = ["SPERRY"]
Links = ["https://www.abc-mart.net/shop/goods/search.aspx?fssort=price&fsstock=1&fssales=1&fsbrand=SPERRY+TOPSIDER&fscategory=all&fsgender=all&fssize=all&fscolor=all&p=PAGE##goodslist"]
PageNumber = [5]

for index, brand in enumerate(Brands):

    productlist = []
    for i in range(1,PageNumber[index]+1):
        link = str(Links[index]).replace("PAGE#",str(i))
        print(link)
        page = requests.get(link)
        soup = BeautifulSoup(page.content, 'html.parser')

        for a in soup.find_all('a', href=True):
            
            if "https://www.abc-mart.net/shop/g/" in a['href']:
                productlist.append(a['href'])
                #print(a['href'])


    with open(brand + '.csv', mode='w') as csv_file:
        fieldnames = ["Name", "Yen",'OriginalYen',"OriginalPeso",'Exchange','PriceRaw', 'Profit', "Price",'Res_profit','Reseller', "SizesLabel","Imgs"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        x = 0
        for link in productlist:
            x += 1
            page = requests.get(link)
            soup = BeautifulSoup(page.content, 'html.parser')
            prodname = str(soup.findAll("div", {"class": "goods_name"}))
            extractname = prodname[prodname.find('temprop="name">')+15:prodname.find("</span>")].upper()
            if len(extractname) > 1:
                engtext = translator.translate(extractname, src="ja", dest="en").text
                finalname = engtext[:13].upper()
                print(finalname)
                originalprice = 0
                price = str(soup.findAll("div", {"class": "price_sale"}))
                extractprice = price[price.find('class="price_sale">')+19:price.find("<span")].replace("￥","").strip()
                origprice = str(soup.findAll("div", {"class": "price_default"}))
                originalprice = origprice[origprice.find('class="price_default">')+22:origprice.find("<span")].replace("￥","").strip()
                if len(extractprice) < 1:
                    price = str(soup.findAll("div", {"class": "price"}))
                    extractprice = price[price.find('class="price">')+14:price.find("<span")].replace("￥","").strip()
                #color = str(soup.findAll("div", {"class": "choosed_color"}))
                #extractcolor = color[color.find('選択されたカラー：')+9:color.find("</div")]
                #print(extractcolor)
                sizes = str(soup.findAll("div", {"class": "choosed_size_list"}))
                extractsizes = []
                for line in sizes.splitlines():
                    if "<dt>" in line and "<span>○</span>" in line:
                        extractsizes.append("SIZE: " + line[line.find('<dt>')+4:line.find(" / <span>")])

                extract_imglinks = []
                imgs = str(soup.findAll("div", {"class": "goodsimg zoomimg"}))
                for line in imgs.splitlines():
                    if 'data-zoom-image="' in line:
                        extract_imglinks.append(line[line.find('data-zoom-image="')+17:line.find('" decoding')])

                #print(extract_imglinks)

                if len(extractsizes) > 0:
                    if len(extract_imglinks) > 0:
                        writer.writerow({'Name': finalname, 'Yen': extractprice,'OriginalYen': originalprice, 'SizesLabel': extractsizes, 'Imgs': extract_imglinks[:5]})             