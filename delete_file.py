import os, glob
#Brands = ["ADIDAS","NIKE","FILA","CONVERSE","VANS","NEWBALANCE","PUMA"]

Brands = ["FILA","CONVERSE"]

for brand in Brands:
# Iterate over the list of filepaths & remove each file.
    fulllist = glob.glob(brand+"/collage_reseller_*")
    for filePath in fulllist:
        try:
            os.remove(filePath)
        except:
            print("Error while deleting file : ", filePath)