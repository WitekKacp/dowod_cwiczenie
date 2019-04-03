add_library("pdf")


def setup():
    global img
    global nazwa
    global ext
    size(198, 255)
    beginRecord(PDF, "mojPDFinny.pdf")
    img = loadImage("prawidlowe-1.jpg")
    imageMode(CENTER)
    image(img, width/2, height/2, width, height)
def draw():
    global img
    global nazwa
    global ext
    if mousePressed == True:
        i = loadImage("was.png")
        image(i, width/2, (height/3)*2, 80, 40)
        im = loadImage("glasses.png")
        image(im, width/2, 130, 140, 70) 
        endRecord()    
        
        
