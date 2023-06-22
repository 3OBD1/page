from PIL import Image
myimage = Image.open("pic.jpg")
myimage.show()
mb = (300, 300, 800, 800)  # (left,right,width,lenth)
nim = myimage.crop(mb)
nim.show()
mnb = myimage.convert("l")
mnb.show()
