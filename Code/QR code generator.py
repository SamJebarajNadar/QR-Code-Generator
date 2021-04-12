#!/usr/bin/env python
# coding: utf-8

# In[16]:


import qrcode
from PIL import Image
qr=qrcode.QRCode(version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=20,
                border=2)

print("-----------------Welcome to Sam QR code Generator-------------------\n\n")

websiteLink=input("Enter the link of the website:")
qr.add_data(websiteLink)
qr.make(fit=True)

img=qr.make_image(fill_color="black",back_color="white")
name=input('Enter the file name:')
try:
    file_format=int(input('Enter the file format in which you want to save: \n1.png \n2.pdf\nOption:'))

    if file_format==1:
        extension='.png'
        img.save(name+extension)
        print("\nFile saved successfully...")

    elif file_format==2:
    #Note: we convert this png file into pdf in option 2   
        extension='.png'
        img.save(name+extension)

        image1 = Image.open(r'C:\Users\PRIZE\Downloads\Sam SEM 6\Coding\New_practice_codes\New_practice_codes\Python Projects Personal\QR code generator'+'\\'+name+'.png')
        img1 = image1.convert('RGB')
        img1.save(r'C:\Users\PRIZE\Downloads\Sam SEM 6\Coding\New_practice_codes\New_practice_codes\Python Projects Personal\QR code generator'+'\\'+name+'.pdf')    
        print("\nFile saved successfully...")

    else:
        print("\nPlease enter valid format (i.e number adjacent to the format you want to convert) : \n1.png\n2.pdf")

except ValueError:
    print("Please Enter valid option number")
    


# In[ ]:




