def crop():
    top = 30
    left = 30
    from PIL import Image


    for i in range(1,37):
        im = Image.open(r"D:\\pics\\null"+" "+"("+str(i)+").jpg")
        
        width, height = im.size
        
        right=width*0.53
        bottom=5*height/9

        im1 = im.crop((left, top, right, bottom))

        im1 = im1.save("D:\\pics_save\\null"+" "+"("+str(i)+").jpg")


crop()


