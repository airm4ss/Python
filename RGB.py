from PIL import Image

def bitSolve(img):
    img=Image.open(file)
    width, height = img.size

    for x in range(width):
        for y in range(height):
            color = img.getpixel((x,y))
            r,g,b = color

            if r&4 != 0:
                r,g,b = (0xFF,0xFF,0xFF) #흰색
            else:
                r,g,b = (0,0,0) #검정색
            
            img.putpixel((x,y),(r,b,g))
        img.save("solved.png","png")

if __name__ == '__main__':
    file="hidden.png"
    bitSolve(file)