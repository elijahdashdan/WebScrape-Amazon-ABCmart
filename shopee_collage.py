
import os, glob
from fpdf import FPDF
from PIL import Image

categories = ["Chocolates","Hair","Face","Watch","Soup","Vitamin","Snack","Electronics","Food","Noodle"]

######RESELLER PDF COLLAGE
# for category in categories:
#     pdf = FPDF()
#     imagelist = (glob.glob(category+"/*.jpg"))
#     imagelist.sort(key=os.path.getmtime)
#     for image in imagelist:
#         pdf.add_page()
#         pdf.image(image,0,0,200,200)
#     pdf.output(category+"_final.pdf", "F")
######RESELLER PDF COLLAGE

def create_collage(width, height, listofimages,filename):
    
    cols = 2
    rows = int(len(listofimages)//2)
    print("LISTOFimages"+str(rows))

    thumbnail_width = width//cols
    thumbnail_height = height//rows
    size = thumbnail_width, thumbnail_height
    new_im = Image.new('RGB', (width, height),(0,0,0))

    ims = []
    for p in listofimages:
        im = Image.open(p)
        imthumb = im.thumbnail(size,Image.ANTIALIAS)
        ims.append(imthumb)
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

for category in categories:
    images = (glob.glob(category+"/*.jpg"))
    dividend = len(images[:200])//2
    images.sort(key=os.path.getmtime)
    print(images)

    i = 0 
    x = 0

    for i in range(0,len(images),8):
        listofimages = images[i:i+8]
        print(listofimages)
        create_collage(2480, 3508, listofimages,category+"/collage_final_"+str(x)+".jpg")
        x += 1


    pdf = FPDF()
    imagelist = (glob.glob(category+"/collage_final_*"))
    imagelist.sort(key=os.path.getmtime)
    
    for image in imagelist:
        pdf.add_page()
        pdf.image(image,0,0,210,297)
    pdf.output(category+"_final.pdf", "F")