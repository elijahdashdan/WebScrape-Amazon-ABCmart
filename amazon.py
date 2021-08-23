from bs4 import BeautifulSoup
import requests
import csv
import os

productlist = []
for i in range(1,3):
    link = "https://www.amazon.co.jp/-/en/gp/bestsellers/beauty/5263242051/ref=zg_bs_pg_"+ str(i)+"?ie=UTF8&pg="+ str(i)
    print(link)
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    productDivs = soup.findAll('a', attrs={'class' : 'a-link-normal'})

    productlinks = []
    for div in productDivs:
        productlinks.append("https://www.amazon.co.jp"+str(div['href']))

print(productlinks)

# with open('PERFUME.csv', mode='w') as csv_file:
#     fieldnames = ['Japanese', 'NameRaw', "Name", "Yen",'PriceRaw', 'Profit', "Price", "SizesLabel","Imgs"]
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#     writer.writeheader()
#     x = 0
#     for link in productlist:
#         x += 1
# #x = 1
# #link = "https://www.abc-mart.net/shop/g/g6030070001047/"
#         page = requests.get(link)
#         soup = BeautifulSoup(page.content, 'html.parser')
#         prodname = str(soup.findAll("div", {"class": "goods_name"}))
#         extractname = prodname[prodname.find('temprop="name">')+15:prodname.find("</span>")].upper()
#         #print(extractname)
#         price = str(soup.findAll("div", {"class": "price_sale"}))
#         extractprice = price[price.find('class="price_sale">')+19:price.find("<span")].strip()
#         if len(extractprice) < 1:
#             price = str(soup.findAll("div", {"class": "price"}))
#             extractprice = price[price.find('class="price">')+14:price.find("<span")].replace("￥","").strip()
#         #color = str(soup.findAll("div", {"class": "choosed_color"}))
#         #extractcolor = color[color.find('選択されたカラー：')+9:color.find("</div")]
#         #print(extractcolor)
#         sizes = str(soup.findAll("div", {"class": "choosed_size_list"}))
#         extractsizes = []
#         for line in sizes.splitlines():
#             if "<dt>" in line and "<span>○</span>" in line:
#                 extractsizes.append("SIZES: " + line[line.find('<dt>')+4:line.find(" / <span>")])

#         extract_imglinks = []
#         imgs = str(soup.findAll("div", {"class": "goodsimg zoomimg"}))
#         for line in imgs.splitlines():
#             if 'data-zoom-image="' in line:
#                 extract_imglinks.append(line[line.find('data-zoom-image="')+17:line.find('" decoding')])

#         #print(extract_imglinks)

#         if len(extractsizes) > 0:
#             writer.writerow({'Japanese': extractname, 'Yen': extractprice, 'SizesLabel': extractsizes, 'Imgs': extract_imglinks[:5]})
            
                    