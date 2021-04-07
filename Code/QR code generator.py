#!/usr/bin/env python
# coding: utf-8

# In[5]:


import qrcode
qr=qrcode.QRCode(version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=20,
                border=2)

websiteLink=input("Enter the link of the website:")
qr.add_data(websiteLink)
qr.make(fit=True)

img=qr.make_image(fill_color="black",back_color="white")
img.save('Blog.png')

