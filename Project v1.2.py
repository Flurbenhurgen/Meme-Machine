'''
Version 1.2
Simplified generate_meme by splitting it into two seperate functions choose_text compile_meme
Simplified check_input through abstraction
'''

#Import the necessary libraries/modules needed to make certain functions work
import PIL, random, os
from PIL import ImageFont, Image, ImageDraw

#Lists of predetermined strings that are used when a random text is selected for an image
okay = ['okay', "Chrome is not saving any cookies for you", "When your teachers assign more homework", "Left on read", ]
troll = ['troll', "When you fart and blame it on someone else", "U mad bro?", "answering K to a long emotional text", ]
forever = ['forever', 'Unattractiveness is a dating game on hard mode','Got a snapchat from Team Snapchat', "Bought an iPhone...  it's a $600 alarm clock", ]
realize = ['realize', "When the chocolate chip cookie has raisins", "When the bagels aren't artisan", "When your code works in the first try", "When you see your teacher at Target", "When you forget your homework at home"]
simply = ['simply', "One does not simply steal a cookie from the cookie jar", "One does not simply code without errors", "One does not simply take PARCC and stay sane", "One does not simply take the PSAT and not post memes","One does not simply walk into Mordor"]

font = ImageFont.truetype('impact.ttf', 67) #Dictate the font and point size to be used on the images
meme_num = {'1':okay, '2':troll, '3':forever, '4':realize, '5':simply}    #Associate the different meme types with its number code

#Indroduction and saves user input to variable and calls check_input()
def welcome():
    print("[Hello, welcome to the MEME-MESHEEN]")
    print()
    print("What will your order be? \nOkay (1) \nTroll Face (2) \nForever Alone (3) \nRealization (4) \nOne Does Not Simply (5) \nCreate Your Own! (6)") #Ask user for input
    meme_type_num = str(input())    #expects a number from 1-6
    check_input(meme_type_num)  #Call the function below 

#Calls the proper function based on user input / expects a string
def check_input(meme_type_num):
    if int(meme_type_num) >= 1 and int(meme_type_num) <= 5:
        choose_text(meme_type_num)
    elif int(meme_type_num) == 6:
        custom_meme()
    else:
        print("invalid input... do you want a meme or not?") #Call out user for invalid input
        input("press ENTER to try again")
        welcome()

#user defines value for chosen_image variable and chosen_text variable
def custom_meme():
    print()
    print("What image will you use for your meme? (refer to image codes above)")
    chosen_image = input()      #expects a value from 1-5
    if chosen_image.isalpha() or int(chosen_image) < 1 or int(chosen_image) > 5 :   #Check for invalid input
        print("Invalid image code")
        custom_meme()
    if int(chosen_image) < 1 or int(chosen_image) > 5:  #Detect for invalid input
        print("invalid image code")
    else:
        print("What will the text be?")
        chosen_text = input().upper()
        compile_meme(str(chosen_image), chosen_text)   #Call custom_meme_gen function with parameters dictating image and text

def choose_text(image_code):
    meme_type = meme_num[image_code]
    text = random.choice(meme_type[1:]).upper()
    compile_meme(image_code, text)
    

def compile_meme(image_code, text):
    x, y = 0, 0
    image = Image.open('images/' + meme_num[image_code][0] + '.png')
    draw = ImageDraw.Draw(image)
    draw.text((x+5,y),multi_line(text),(0,0,0),font=font,align="center")     #Black outline around white text
    draw.text((x-5,y),multi_line(text),(0,0,0),font=font,align="center")     #||
    draw.text((x,y+5),multi_line(text),(0,0,0),font=font,align="center")     #||
    draw.text((x,y-5),multi_line(text),(0,0,0),font=font,align="center")     #||
    draw.text((x,y),multi_line(text),(255,255,255),font=font,align="center")  #White text over black outline
    image.show()      #Open edited image
    os.system('cls')    #clear console
    welcome()   #Restart program by calling the beginning function

#Expects a string - Outputs a string - Input must have spaces between words
def multi_line(phrase):
    splitted = phrase.replace(' ', '! !').split('!')    #Replace all spaces with '! !' and then splitting the string at every '!'.
    use_list = []                                       
    limit_len = 35
    new_phrase = ''                                     
    for item in splitted:                               #Start an if loop for every item in the splitted list 
        if len(new_phrase) <= limit_len:                #If new_phrase character length is less than or equal to character limit...
            use_list.append(item)                       #Add an item from splitted to use_list
            new_phrase = ''.join(use_list)              #Convert use_list to one string and set it to new_phrase
        elif len(new_phrase) > limit_len:               #If new_phrase character length is more than the character limit...
            use_list.append('\n')                       #Add '\n' to the end of use_list. \n tells python to use a new line
            limit_len = limit_len + limit_len           #Set the new limit length to adapt to the new line
    return new_phrase   


#Run Program
welcome()
