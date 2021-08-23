import pandas as pd
import requests
import os
import numpy as np

import PIL, os, glob
from PIL import Image
from math import ceil, floor
from PIL import ImageFont
from PIL import ImageDraw


#Brands = ["ADIDAS","NIKE","FILA","CONVERSE","VANS","NEWBALANCE","PUMA","BIRKENSTOCK","SPERRY"]
Brands = ["SPERRY"]

for brand in Brands:
    df = pd.read_excel ("/Users/dm/Documents/PythonStudy/"+brand+".xlsx")
    os.mkdir(brand)

    for index, row in df.iterrows():
        #if index < 112:
        y = 0
        listofurl = row['Imgs'].split(",")
        if len(listofurl)>1:
            for i in listofurl:
                y += 1
                url = i.replace("[","").replace("]","").replace("'","").strip()
                # print(url)
                print(row['Name'].strip() + "/" + str(index) + "_" + str(y) + ".jpg")
                response = requests.get(url)
                # file = open(row['Name'].strip() + "/" + str(index) + "_" + str(y) + ".jpg", "wb")
                file = open(brand+"/DL_" + str(index) + "_" + str(y) + ".jpg", "wb")
                file.write(response.content)
                file.close()
