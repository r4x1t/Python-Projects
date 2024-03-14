#Import image library

from PIL import Image

def grayify(image):
    return image.convert('L')

def resize(image,height,width):
    return image.resize((height,width))

def map_to_ascii(pixel_brightness):
    char=['#','$','%','*','+','=','!',':','-',',','.',' ']
    return char[-int(pixel_brightness/255 * len(char) -1)]#we do -ve  of index as its reversed intensity so the brighter it is the less intense it gets

def image_to_ascii(image) :
    #set new width and convert new height accordingly
    new_width=80
    new_height=int(image.height/image.width*new_width)
    #resize
    new_image=resize(image,new_height,new_width)
    #convert to grayscale
    gray_image=grayify(new_image)
    #map to ascii characters
    ascii_art=[]# created a list that stores each line of charcters we add\n while returning so each line is seperated to form a row ,column type matrix

    for y in range(gray_image.height):# y is 0 to height
        line=""
        for x in range(gray_image.width):
            pixel=gray_image.getpixel((x,y))
            line+=map_to_ascii(pixel)
     
        ascii_art.append(line)
    
    return "\n".join(ascii_art)


if __name__ =="__main__":
    path=input("ENter valid image path :")

    try:
        image=Image.open(path)
        ascii_art=image_to_ascii(image)
    except:
        print(path," not valid")

    print(ascii_art)

    with open("art.txt","w") as f:
        f.write(ascii_art)




    
    
    