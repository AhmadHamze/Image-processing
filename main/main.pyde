def setup():
    global myImage
    myImage = loadImage("Birds.jpg")
    size(1080,608)
    noLoop()
    
def draw():
    loadPixels()
    myImage.loadPixels()
    for i in range(myImage.width - 1):
        for j in range(myImage.height):
            loc1 = i + j*width
            loc2 = i+1 +j*width
            b1 = brightness(myImage.pixels[loc1])
            b2 = brightness(myImage.pixels[loc2])
            diff = abs(b1 - b2)
            if diff > 20:
                pixels[loc1] = color(0)
            else:
                pixels[loc1] = color(255)
    updatePixels()
