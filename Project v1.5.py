'''
Version 1.5

Improved invalid input messages
Renamed check_user_input to user_input_is_valid
Renamed get_type_code to ask_meme_code
Renamed variable type_code to meme_type
Renamed everything to do with image_code to image_type
Renamed phrase and new_phrase to text and new_text
Renamed multi_line to text_wrap
Added "top" functionality to user_input_is_valid so that there aren't hard set parameters for a valid input
Slightly improved list calling through the use of eval()
Added ability to use your own image to the Meme Machine!
    Added stock_or_custom()
    Added upload_image()
    Added detectBadImages()
    Added resizeImage()
    Added select_uploaded_image()
    Added image_type_is_valid()
'''

import PIL, random, os
from PIL import ImageFont, Image, ImageDraw

#Lists of predetermined strings that are used when a random text is selected for an image
okay = ["Chrome is not saving any cookies for you", "When your teachers assign more homework", "Left on read", ]
troll = ["When you fart and blame it on someone else", "U mad bro?", "answering K to a long emotional text", ]
forever = ['Unattractiveness is a dating game on hard mode','Got a snapchat from Team Snapchat', "Bought an iPhone...  it's a $600 alarm clock", ]
realize = ["When the chocolate chip cookie has raisins", "When the bagels aren't artisan", "When your code works in the first try", "When you see your teacher at Target", "When you forget your homework at home"]
simply = ["One does not simply steal a cookie from the cookie jar", "One does not simply code without errors", "One does not simply take PARCC and stay sane", "One does not simply take the PSAT and not post memes","One does not simply walk into Mordor"]
hacker = []

font = ImageFont.truetype('impact.ttf', 67)
meme_codes = {'1':'okay', '2':'troll', '3':'forever', '4':'realize', '5':'simply', '6':'hacker'} #Associates a type of meme with a number - Useful for simplifiying code to filesystem interaction

#Indroduces the user to the program - First function to be called
def welcome():
    print("[Hello, welcome to the MEME-MESHEEN]")
    print('\nWhat will your order be?')
    ask_meme_type()

#Meme type determines which image the program will use for random text or if a custom meme will be created
def ask_meme_type():
    print("Okay (1) \nTroll Face (2) \nForever Alone (3) \nRealization (4) \nOne Does Not Simply (5) \nCreate Your Own! (6)") #Ask user for input
    meme_type = str(input())    #expects a number from 1-6
    random_or_custom(meme_type)

#Universal input validity checking that can be used for all functions
def user_input_is_valid(user_input, top):
    inputIsNotValid = user_input.isalpha() or not user_input.isdigit() or int(user_input) < 1 or int(user_input) > top
    if inputIsNotValid:
        return False
    else:
        return True

#Based on the meme_type selected by the user, determines if a random text meme or a custom meme will be made
def random_or_custom(meme_type):
    if user_input_is_valid(meme_type, 6):
        if int(meme_type) == 6:
            stock_or_upload_image()
        else:
            choose_random_text(meme_type)
    else:
        print("Invalid Input \nChoose between memes 1-5 or choose 6 to create your own\n")
        ask_meme_type()

#Asks the user if they would like to use a stock image or use their own
def stock_or_upload_image():
    print("\nWill you be using one of our hilarious stock images or upload your own? \nStock (1) \nUpload Your Own (2)")
    user_input = input()
    if user_input_is_valid(user_input, 2):
        if user_input is '1':
            custom_meme_image()
        else:
            upload_image()
    else:
        print("Invalid Input \nYou had two choices! 1 or 2! Make up your mind!")
        stock_or_upload_image()

#Walks the user through the process of uploading their own image
def upload_image():
    print("\nI see you want to bring your own meme-ific image into this beautiful Meme Meshine \nTo do this, copy and pasta any PNG image with a bit depth of 24 or lower into the images folder") 
    input("press any key to continue\n")
    print("I will now scan your images folder using sharks with laser beams on their heads to see if your images are compatible")
    badImages = detectBadImages()
    if len(badImages) is 0:
        print("Good Job! You have no bad images!")
    else:
        print("You have", len(badImages), "baaaad images")
        print("I will now fix your baaaad images")
        resizeImage(badImages)
        print("Resizing done")
    select_uploaded_image()
    
#Searches the images folder for any PNG files with a width that isn't 1280 pixels and flags them for resizing
def detectBadImages():
    badImages = []
    for file in os.listdir('images'):
        if file.endswith('.png'):
            image = Image.open('images/'+file)
            if image.size[0] != 1280:
                badImages.append(file)
    return badImages

#Resizes flagged images to have a width of 1280 pixels and maintains aspect ratio
def resizeImage(badImages):
    for image in badImages:
        img = Image.open('images/'+image)
        width, height = img.size
        new_width = 1280
        new_height = new_width * height / width
        img = img.resize((int(new_width), int(new_height)), Image.ANTIALIAS)
        img.save('images/'+image)

#Asks the user to select an image from the images folder to use for their meme
def select_uploaded_image():
    print("\nAlthough I am a computer, I do not know everything.\nFrom the list below, tell me the name of the image you want\nPssst: you can copy/paste")
    for file in os.listdir('images'):
        print(os.path.splitext(file)[0])
    image_type = str(input())
    if image_type_is_valid(image_type):
        custom_meme_text(image_type)
    else:
        print("I expected better from you... You're only wasting your own time by entering an invalid input\nThis time pick something from the list")
        select_uploaded_image()

#Validation for image name input from select_uploaded_image()
def image_type_is_valid(image_type):
    for file in os.listdir('images'):
        if os.path.splitext(file)[0] == image_type:
            return True
            break
    else:
        return False

#Asks the user which stock image to be used for their custom meme
def custom_meme_image():
    print("\nWhat image will you use for your meme? (refer to image numbers above)")
    image_type = input()      #expects a value from 1-5
    if user_input_is_valid(image_type, 6):
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
    text = random.choice(eval(meme_type)).upper()
    compile_meme(meme_codes[image_type], text)
    
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
welcome()
