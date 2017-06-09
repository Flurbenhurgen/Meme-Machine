'''
Version 1.3.0

* Changed the user_input_is_valid parameter "top" to a tuple called valid_range consisting of a lower limit [0] and an upper limit [1]
* Removed hackerman as an easter egg and added it as an official option
* Changed instances of pascalCase to underscore seperation
* Removed functions
  * stock_or_custom()
  * upload_image()
  * select_uploaded_image()
  * image_type_is_valid()
* Added support for a dynamic filesystem in the images folder. Program will adapt to the amount of images in the folder.
  * Added function set_up_images
  * Added function variable_exists
'''

import PIL, random, os
from PIL import ImageFont, Image, ImageDraw

#Lists of predetermined strings that are used when a random text is selected for an image
okay = ["Chrome is not saving any cookies for you", "When your teachers assign more homework", "Left on read", ]
troll = ["When you fart and blame it on someone else", "U mad bro?", "answering K to a long emotional text", ]
forever = ['Unattractiveness is a dating game on hard mode','Got a snapchat from Team Snapchat', "Bought an iPhone...  it's a $600 alarm clock", ]
realize = ["When the chocolate chip cookie has raisins", "When the bagels aren't artisan", "When your code works in the first try", "When you see your teacher at Target", "When you forget your homework at home"]
simply = ["One does not simply steal a cookie from the cookie jar", "One does not simply code without errors", "One does not simply take PARCC and stay sane", "One does not simply take the PSAT and not post memes","One does not simply walk into Mordor"]

font = ImageFont.truetype('impact.ttf', 67)
meme_codes = {} #Associates a type of meme with a number - Useful for simplifiying code to filesystem interaction
number_of_images = 0

#Scans the images folder and saves the existing PNG files to be used by the program
def set_up_images():
    badImages = []
    global number_of_images
    for file in os.listdir('images'):
        if file.endswith('.png'):
            number_of_images += 1
            meme_codes[str(number_of_images)] = os.path.splitext(file)[0]

#Searches the images folder for any PNG files with a width that isn't 1280 pixels and flags them for resizing
def detect_bad_images():
    badImages = []
    for file in os.listdir('images'):
        if file.endswith('.png'):
            image = Image.open('images/'+file)
            if image.size[0] != 1280:
                badImages.append(file)
    return badImages

#Resizes flagged images to have a width of 1280 pixels and maintains aspect ratio
def resize_image(bad_images):
    for image in bad_images:
        img = Image.open('images/'+image)
        width, height = img.size
        new_width = 1280
        new_height = new_width * height / width
        img = img.resize((int(new_width), int(new_height)), Image.ANTIALIAS)
        img.save('images/'+image)

#Indroduces the user to the program - First function to be called
def welcome():
    print("[Hello, welcome to the MEME-MESHEEN]\nWhat will your order be?")
    ask_meme_type()

#Meme type determines which image the program will use for random text or if a custom meme will be created
def ask_meme_type():
    for item in meme_codes:
        print('(' + item + ')', meme_codes[item].capitalize())
    print('(' + str(number_of_images + 1) + ') Make your own')
    random_or_custom(str(input()))

#Universal input validity checking that can be used for all functions
def user_input_is_valid(user_input, valid_range):
    inputIsNotValid = user_input.isalpha() or not user_input.isdigit() or int(user_input) < valid_range[0] or int(user_input) > valid_range[1]
    if inputIsNotValid:
        return False
    else:
        return True

#Based on the meme_type selected by the user, determines if a random text meme or a custom meme will be made
def random_or_custom(meme_type):
    if user_input_is_valid(meme_type, (1, number_of_images + 1)):
        if int(meme_type) == number_of_images + 1:
            custom_meme_image()
        else:
            choose_random_text(meme_type)
    else:
        print("Invalid Input \nChoose between memes 1-5 or choose 6 to create your own\n")
        ask_meme_type()

#Asks the user which stock image to be used for their custom meme
def custom_meme_image():
    print("\nWhat image will you use for your meme? (refer to image numbers above)")
    image_type = input()      #expects a value from 1-5
    if user_input_is_valid(image_type, (1, number_of_images)):
        custom_meme_text(meme_codes[image_type])
    else:
        print("Invalid Input \nHey! Do you want a meme? You've got some options here, one through five. Choose wisely!")
        custom_meme_image()

#Asks user to input the text to be displayed on their custom meme
def custom_meme_text(image_type):
    print("\nWhat will the text be?")
    chosen_text = input().upper()
    compile_meme(image_type, chosen_text)

#Grabs a random string from the appropriate list that will be put on the image
def choose_random_text(image_type):
    meme_type = meme_codes[image_type]
    if variable_exists(meme_type):        
        text = random.choice(eval(meme_type)).upper()
        compile_meme(meme_codes[image_type], text)
    else:
        print("For this image you will have to create your own text")
        custom_meme_text(meme_type)

#Checks if a variable exists
def variable_exists(variable):
    if str(variable) in globals():
        return True
    else:
        return False
#Puts the text text on the image and opens the edited image in the computer's default image viewer
def compile_meme(image_type, text):
    x, y = 0, 0
    image = Image.open('images/' + image_type + '.png')
    draw = ImageDraw.Draw(image)
    draw.text((x+5,y),text_wrap(text),(0,0,0),font=font,align="center")      #Black outline around white text
    draw.text((x-5,y),text_wrap(text),(0,0,0),font=font,align="center")      #||
    draw.text((x,y+5),text_wrap(text),(0,0,0),font=font,align="center")      #||
    draw.text((x,y-5),text_wrap(text),(0,0,0),font=font,align="center")      #||
    draw.text((x,y),text_wrap(text),(255,255,255),font=font,align="center")  #White text over black outline
    image.show()    
    os.system('cls')
    welcome() #Restart the program

#Allows for text-wrapping on the meme. When out of space, a new line will be created so that all text is visible on final image
def text_wrap(text):
    splitted = text.replace(' ', '! !').split('!')    #Allows for the preservation of spaces
    use_list = []                                       
    limit_len = 35
    new_text = ''                                     
    for item in splitted:                                
        if len(new_text) <= limit_len:                
            use_list.append(item)                       
            new_text = ''.join(use_list)              
        elif len(new_text) > limit_len:               
            use_list.append('\n')                       
            limit_len = limit_len + limit_len           
    return new_text   


#Run Program
set_up_images()
bad_images = detect_bad_images()
resize_image(bad_images)
welcome()
