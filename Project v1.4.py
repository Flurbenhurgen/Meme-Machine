'''
Version 1.4

Renamed checkfor_invalid_input to check_user_input
Renamed variable validity to inputIsNotValid
Changed check_user_input so that it returns a boolean
'''

import PIL, random, os
from PIL import ImageFont, Image, ImageDraw

#Lists of predetermined strings that are used when a random text is selected for an image
okay = ['okay', "Chrome is not saving any cookies for you", "When your teachers assign more homework", "Left on read", ]
troll = ['troll', "When you fart and blame it on someone else", "U mad bro?", "answering K to a long emotional text", ]
forever = ['forever', 'Unattractiveness is a dating game on hard mode','Got a snapchat from Team Snapchat', "Bought an iPhone...  it's a $600 alarm clock", ]
realize = ['realize', "When the chocolate chip cookie has raisins", "When the bagels aren't artisan", "When your code works in the first try", "When you see your teacher at Target", "When you forget your homework at home"]
simply = ['simply', "One does not simply steal a cookie from the cookie jar", "One does not simply code without errors", "One does not simply take PARCC and stay sane", "One does not simply take the PSAT and not post memes","One does not simply walk into Mordor"]
hacker = ['hacker']

font = ImageFont.truetype('impact.ttf', 67)
meme_code = {'1':okay, '2':troll, '3':forever, '4':realize, '5':simply, '6':hacker} #Associates a type of meme with a number - Useful for simplifiying code to filesystem interaction

#Indroduces the user to the program - First function to be called
def welcome():
    print("[Hello, welcome to the MEME-MESHEEN]")
    print()
    print('What will your order be?')
    get_type_code()

#Type Code determines which image the program will use for random text or if a custom meme will be created
def get_type_code():
    print("Okay (1) \nTroll Face (2) \nForever Alone (3) \nRealization (4) \nOne Does Not Simply (5) \nCreate Your Own! (6)") #Ask user for input
    type_code = str(input())    #expects a number from 1-6
    random_or_custom(type_code)

#Universal input validity checking that can be used for all functions
def check_user_input(user_input):
    inputIsNotValid = user_input.isalpha() or not user_input.isdigit() or int(user_input) < 1 or int(user_input) > 6
    if inputIsNotValid:
        return False
    else:
        return True

#Based on the type_code selected by the user, determines if a random text meme or a custom meme will be made
def random_or_custom(type_code):
    if check_user_input(type_code):
        if int(type_code) == 6:
            custom_meme_image()
        else:
            choose_random_text(type_code)
    else:
        print("Invalid Input - Try Again")
        get_type_code()

#Asks the user which image to be used for their custom meme
def custom_meme_image():
    print()
    print("What image will you use for your meme? (refer to image codes above)")
    image_code = input()      #expects a value from 1-5
    if check_user_input(image_code):
        custom_meme_text(image_code)
    else:
        print("Invalid Input - Try Again")
        custom_meme_image()

#Asks user to input the text to be displayed on their custom meme
def custom_meme_text(image_code):
    print("What will the text be?")
    chosen_text = input().upper()
    compile_meme(str(image_code), chosen_text)

#Grabs a random string from the appropriate list that will be put on the image
def choose_random_text(image_code):
    meme_type = meme_code[image_code]
    text = random.choice(meme_type[1:]).upper()
    compile_meme(image_code, text)
    
#Puts the text text on the image and opens the edited image in the computer's default image viewer
def compile_meme(image_code, text):
    x, y = 0, 0
    image = Image.open('images/' + meme_code[image_code][0] + '.png')
    draw = ImageDraw.Draw(image)
    draw.text((x+5,y),multi_line(text),(0,0,0),font=font,align="center")      #Black outline around white text
    draw.text((x-5,y),multi_line(text),(0,0,0),font=font,align="center")      #||
    draw.text((x,y+5),multi_line(text),(0,0,0),font=font,align="center")      #||
    draw.text((x,y-5),multi_line(text),(0,0,0),font=font,align="center")      #||
    draw.text((x,y),multi_line(text),(255,255,255),font=font,align="center")  #White text over black outline
    image.show()    
    os.system('cls')
    welcome() #Restart the program

#Allows for text-wrapping on the meme. When out of space, a new line will be created so that all text is visible on final image
def multi_line(phrase):
    splitted = phrase.replace(' ', '! !').split('!')    #Allows for the preservation of spaces
    use_list = []                                       
    limit_len = 35
    new_phrase = ''                                     
    for item in splitted:                                
        if len(new_phrase) <= limit_len:                
            use_list.append(item)                       
            new_phrase = ''.join(use_list)              
        elif len(new_phrase) > limit_len:               
            use_list.append('\n')                       
            limit_len = limit_len + limit_len           
    return new_phrase   


#Run Program
welcome()
