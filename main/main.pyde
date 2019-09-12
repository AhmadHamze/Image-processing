def setup():
    global myImage
    myImage = loadImage("Birds.jpg")
    size(1080,608)
    noLoop()
    
def draw():
    loadPixels()
    myImage.loadPixels()
    for i in range(myImage.width - 1):
        for j in range(myImage.height - 1):
            loc1 = i-1 + (j-1)*width
            loc2 = i + (j-1)*width
            loc3 = i+1 + (j-1)*width
            loc4 = i-1 + j*width
            loc5 = i+1 + j*width
            loc6 = i-1 + (j+1)*width
            loc7 = i + (j+1)*width
            loc8 = i+1 + (j+1)*width
            b1 = brightness(myImage.pixels[loc1])
            b2 = brightness(myImage.pixels[loc2])
            b3 = brightness(myImage.pixels[loc3])
            b4 = brightness(myImage.pixels[loc4])
            b5 = brightness(myImage.pixels[loc5])
            b6 = brightness(myImage.pixels[loc6])
            b7 = brightness(myImage.pixels[loc7])
            b8 = brightness(myImage.pixels[loc8])

            if (abs(b1-b6)>20 and abs(b2-b7)>20) and (abs(b3-b8)>20 and abs(b4-b5)>20):
                pixels[loc1] = color(0)
            else:
                pixels[loc1] = color(255)
    updatePixels()
    save("shadowBirds.jpg")
    print "file saved successfully."
