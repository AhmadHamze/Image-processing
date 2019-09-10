def setup():
    global myImage
    myImage = loadImage("Birds.jpg")
    size(1080,608)
    
def draw():
    image(myImage,0,0)
