from PIL import Image
import os, glob
from fpdf import FPDF

def create_collage(width, height, listofimages,filename):
    
    #cols = 2
    #rows = int(len(listofimages)/2)

    #RESELLER
    cols = 1
    rows = int(len(listofimages))

    thumbnail_width = width//cols
    thumbnail_height = height//rows
    size = thumbnail_width, thumbnail_height
    #new_im = Image.new('RGB', (width, height),(0,0,0))
    
    #RESELLER
    new_im = Image.new('RGB', (width, height),(255,255,255))

    ims = []
    for p in listofimages:
        im = Image.open(p).resize(size)
        ims.append(im)
    i = 0
    x = 0
    y = 0

    for row in range(rows):
        for col in range(cols):
            print(i, x, y)
            new_im.paste(ims[i], (x, y))
            i += 1
            x += thumbnail_width
        y += thumbnail_height
        x = 0


    new_im.save(filename)
    #new_im.show()

# Brands = ["ADIDAS","NIKE","FILA","CONVERSE","VANS","NEWBALANCE","PUMA","BIRKENSTOCK","SPERRY"]

Brands = ["FILA","CONVERSE","VANS","NEWBALANCE","PUMA","BIRKENSTOCK","SPERRY"]

for brand in Brands:
    #images = (glob.glob(brand+"/final_*"))
    images = (glob.glob(brand+"/reseller_*"))
    dividend = len(images[:200])//2
    images.sort(key=os.path.getmtime)
    print(images)

    i = 0 
    x = 0
    # for i in range(0,len(images),8):
    #     listofimages = images[i:i+8]
    #     print(listofimages)
    #     create_collage(2480, 3508, listofimages,brand+"/collage_final_"+str(x)+".jpg")
    #     x += 1

    for i in range(0,len(images[:200]),2):
        print(i)
        listofimages = images[i:i+2]
        print(listofimages)
        create_collage(2480, 3508, listofimages,brand+"/collage_reseller_"+str(x)+".jpg")
        x += 1    

    pdf = FPDF()
    #imagelist = (glob.glob(brand+"/collage_final_*"))
    imagelist = (glob.glob(brand+"/collage_reseller_*"))
    imagelist.sort(key=os.path.getmtime)
    
    imagelistfinal1 = imagelist[:50]
    for image in imagelistfinal1:
        pdf.add_page()
        pdf.image(image,0,0,210,297)
    #pdf.output(brand+"_final.pdf", "F")
    pdf.output(brand+"_reseller1.pdf", "F")

    if len(imagelist)>50:
        print("HEYYYYYY")
        pdf2 = FPDF()
        imagelistfinal2 = imagelist[51:]
        for image in imagelistfinal2:
            pdf2.add_page()
            pdf2.image(image,0,0,210,297)
        #pdf.output(brand+"_final.pdf", "F")
        pdf2.output(brand+"_reseller2.pdf", "F")