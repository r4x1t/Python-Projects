#image to ascii converter
#we first declare the ascii characters we will be using for the conversion
#we then import the image we want to convert then we resize the image
#why do we resize it?
#because 2 reasons : 1. terminal width : terminal can only fit a certain amount of charcters in a line , so if we dont resize it to fit the terminal,the art would be distorted
#2.  resizing for clarity as we have limited characters to map to each pixel we resize so there are less pixel and we get a finer art
# after resize we convert image to grayscale so its easier to map according to brightness of the pixel 
# the more brighter the pixel the denser the character we map it to
# then we map the characters to the pixels
#then we save the txt art and were done!!!!
#code::

#import python image library , make sure u install Pillow beforehand

from PIL import Image
#import PIL.Image

#create a function to convert an image to grayscale

def convert_to_grayscale(image):
    return image.convert('L')

#we create a function to map ascii char to each pixel

#we first create a list of ASCII characters in decreasing intensity so we can map our pixels to them accordingly
#logic here is that grayscale pixels range of brightness is from 0 to 255 so if we get any pixel_brightness we divide it by 255 this gives us a number between 0 and 1 (basically normalizes each pixel between range of 0 and 1)
#then we can multiply this value between 0 and 1**  to the length of list** so that we can get the appropriate intensity character*** to be mapped to the pixel** accordingly (in accordance to their brightness)
# eg. 128 brightness pixel is received we divide it by 255 we get 0.50 aprox 
#then multiply it to length of ASCII CHAR list, we get 10 * 0.5 = 5  now subtract 1***** 
#important to subtract 1 as python is 0 indexed so 5th index is actually 4 for the list 
#so 5-1 =4 so that would be the index of character that needs to be mapped in accordance to intensity adn brightness
#function::  **note the less brightness means darker pixel
#we take pixel brightness as input
#less darkness is darker pixels so more intensity

def ascii_map(pixel_brightness):
   char=['@','#','B','$','&','%','*','!',']',')',':',',','.',' ']
   char=['$','@','B','%','8','&','W','M','#','*','o','a','h','k','b','d','p','q','w','m','Z','O','0','Q','L','C','J','U','Y','X','z','c','v','u','n','x','r','j','f','t','/','|','(',')','1','{','}','[',']','?','-','_','+','~','<','>','i','!','l','I',';',':',',','"','^','`','.',' ']
   #char="$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,^`."
   
    #now we map the char to brightness
   return char[-int(pixel_brightness/255*len(char)-1)]


#now after grayscale and mapping we have to create a main fucntion that will take input for the image, call all these functions and save the txt file that would be the art

def image_to_ascii(image_path):
    image= Image.open(image_path)
    # i chose the desired output width lets take it 100 here, but we can also let the user chose it aswell
    #we resize the image
    output_width=100
    output_heigth=int(image.height/image.width*output_width)
    image1=image.resize((output_width,output_heigth))
    #image is resized
    #convert to greyscale
    grayscale_image=convert_to_grayscale(image1)
    #now we iterate through each pixel to convert each pixel to grayscale
    #create a list that stores the art
    ascii_art=[]

     #range is 0 to height,width
    for y in range(grayscale_image.height):# we start with y because we are going horizontally as we are saving the art line by line
        ascii_line=""
        for x in range(grayscale_image.width):
            #get the brightness for this pixel x, y we use getpixel method
            pixel_brightness= grayscale_image.getpixel((x,y))
            ascii_line= ascii_line + ascii_map(pixel_brightness)
        
        ascii_art.append(ascii_line)

    return "\n".join(ascii_art) # returns the art Once the loop finishes processing all rows, the code uses the .join() method on the ascii_art list.
#The .join() method takes a separator string as an argument.
#In this case, we use "\n" (newline character) as the separator.
#By joining the list elements with "\n", the .join() method effectively inserts a newline character between each string in the list.


#now lets get into main function to get the image

if __name__ == "__main__":
    image_path = input("Enter the image path: ")
  #  try:
   #     image=PIL.Image.open(image_path)
   # except:
   #     print(image_path," is not valid ")
    
    ascii_art = image_to_ascii(image_path)
    print(ascii_art)
    with open("ascii_art.txt","w") as f:
        f.write(ascii_art)


  

