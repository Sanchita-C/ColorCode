

# 3 libraries used: 'openCV' , 'pandas: used to read the csv file'
import cv2
import pandas as pd
import argparse

# argument parser: takes image path from ther terminal/command line
#arg_parse = argparse.ArgumentParser()
#arg_parse.add_argument('-i','--image' , required=True, help="path of image" )

# using 'vars' function to parse the argument in command line; returns dictionary attribute of our object
#args = vars(arg_parse.parse_args())


# make image path var by indexing into image attribute
image_path = r'pic.jpg'

#read image with opencv
img = cv2.imread(image_path)

#image dimentions:

dimensions = img.shape
height = img.shape[0]
width = img.shape[1]
area = width * height


#global variables 
img_clicked = False
r = 0
g = 0
b = 0
x_position = 0
y_position = 0

# using 'pandas' to read csv file and naming column

index = ["color", "color_name", "hex-code", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names = index, header = None)


# function to get approximate color match

def colorName(R,G,B):
    min = 1000  
    col_name = ""

    # looping over every color in csv file ; find color that is closest
    for i in range(len(csv)):
        # compute abs value distance btwn color we clicked and the color we are searching
        dist = abs(R - int(csv.loc[i,"R"])) + abs(G - int(csv.loc[i,"G"])) + abs(B - int(csv.loc[i,"B"]))
        if dist <= min:
            min = dist
            col_name = csv.loc[i,"color_name"]
    return col_name


# function to get x,y coordinates of mouse double click
def draw(event, x, y, flags, param):
    # if left mouse button is clicked down; img_clicked value is set to 'true'
    if event == cv2.EVENT_LBUTTONDOWN:
        global b, g, r, x_position, y_position, img_clicked
        img_clicked = True
        x_position = x
        y_position = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)

# create window , specify area of window, if area of image is <= 662000 make it not resizable

cv2.namedWindow('image')


# set mouse handler for specifies window
cv2.setMouseCallback('image',draw)

# while loop with only break if a certain condition is met

while(True):
    cv2.imshow("image", img)
    if img_clicked:
          # cv2.rectangle(image, start point, endpoint, color, thickness)-1 fills entire rectangle
        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)

        # text string display RGB values and name of color
        text = colorName(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)

        # cv2.putText(img,text,start,Hershey_TRIPLEX font has (0-7) choices,fontScale,color,thickness,lineType )
        cv2.putText(img, text, (50, 50), cv2.FONT_HERSHEY_TRIPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

        # display text in black for light shades
        if r + g + b >= 600:
            cv2.putText(img, text, (50, 50), cv2.FONT_HERSHEY_TRIPLEX, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

        img_clicked = False

 
    
    # break out from loop when 'esc' key is clicked
    # delay of 20 ms , function returns code of the key pressed ; '0xFF' is hexadecimal constant of 8 1's
    if cv2.waitKey(20) & 0xFF == 27:
        break
# destroy all windows
cv2.destroyAllWindows()











