'''
Version 1.1
custom_meme_gen and meme_gen are combined into one function called generate_meme
'''

#Import the necessary libraries/modules needed to make certain functions work
import PIL, random, os
from PIL import ImageFont, Image, ImageDraw

font = ImageFont.truetype('impact.ttf', 67) #Dictate the font and point size to be used on the images
meme_num = {'1':'okay', '2':'troll', '3':'forever', '4':'realize', '5':'simply'}    #Associate the different meme types with its number code

#Lists of predetermined strings that are used when a random text is selected for an image
okay = ['okay', "Chrome is not saving any cookies for you", "When your teachers assign more homework", "Left on read", ]
troll = ['troll', "When you fart and blame it on someone else", "U mad bro?", "answering K to a long emotional text", ]
forever = ['forever', 'Unattractiveness is a dating game on hard mode','Got a snapchat from Team Snapchat', "Bought an iPhone...  it's a $600 alarm clock", ]
realize = ['realize', "When the chocolate chip cookie has raisins", "When the bagels aren't artisan", "When your code works in the first try", "When you see your teacher at Target", "When you forget your homework at home"]
simply = ['simply', "One does not simply steal a cookie from the cookie jar", "One does not simply code without errors", "One does not simply take PARCC and stay sane", "One does not simply take the PSAT and not post memes","One does not simply walk into Mordor"]

#Indroduction and saves user input to variable and calls check_input()
def welcome():
    print("[Hello, welcome to the MEME-MESHEEN]")
    print()
    print("What will your order be? \nOkay (1) \nTroll Face (2) \nForever Alone (3) \nRealization (4) \nOne Does Not Simply (5) \nCreate Your Own! (6)") #Ask user for input
    meme_type_num = str(input())    #expects a number from 1-6
    check_input(meme_type_num)  #Call the function below 
    
#Calls the proper function based on user input / expects a string
def check_input(meme_type_num):
    if meme_type_num == '1':
        generate_meme(False, okay, 0, 0)
    elif meme_type_num == '2':
        generate_meme(False, troll, 0, 0)
    elif meme_type_num == '3':
        generate_meme(False, forever, 0, 0)
    elif meme_type_num == '4':
        generate_meme(False, realize, 0, 0)
    elif meme_type_num == '5':
        generate_meme(False, simply, 0, 0)
    elif meme_type_num == '6':
        custom_meme()
    elif meme_type_num == "":   #If meme_type_num has no value...
        print("No input given")
    else: #If meme_type_num is not valid...
        print("invalid input... do you want a meme or not?") #Call out user for invalid input
        input("press ENTER to try again")
        welcome()   #Call the function above           

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
        generate_meme(True, 0, meme_num[str(chosen_image)], chosen_text)   #Call custom_meme_gen function with parameters dictating image and text

#Expects integer, integer, string, and string - Outputs edited image
def generate_meme(is_custom, meme_type, chosen_image, chosen_text):
    print("Generating your new DANK meme...")
    x, y = 0, 0
    if is_custom is True:                                           #If the meme is custom
        img = Image.open('images/' + str(chosen_image) + '.png')    #Access image file from relative directory
        text = chosen_text
    else:                                                           #If the meme used the predefined lists above
        img = Image.open('images/' + meme_type[0] + '.png')         #Open image file from relative directory
        text = random.choice(meme_type[1:]).upper()
    draw = ImageDraw.Draw(img)
    draw.text((x+5,y),multi_line(text),(0,0,0),font=font,align="center")     #Black outline around white text
    draw.text((x-5,y),multi_line(text),(0,0,0),font=font,align="center")     #||
    draw.text((x,y+5),multi_line(text),(0,0,0),font=font,align="center")     #||
    draw.text((x,y-5),multi_line(text),(0,0,0),font=font,align="center")     #||
    draw.text((x,y),multi_line(text),(255,255,255),font=font,align="center")  #White text over black outline
    img.show()      #Open edited image
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

    
          
#Old verisons of functions below


#Old version of transposing text on images - archived due to length
'''
def okay_gen(meme_type):
    im = Image.open('images/okay.png')
    new_meme = PIL.ImageDraw.Draw(im).multiline_text((0,0), random.choice(okay), fill = (255,255,255), font = fnt, align = 'center')
    new_meme.show()


def haters_gen(meme_type):
    im = Image.open('images/haters.png')
    new_meme = PIL.ImageDraw.Draw(im).multiline_text((0,0), random.choice(haters), fill = (255,255,255), font = fnt, align = 'center')
    Image.show(title=new_meme,command=None)

def forever_gen():
    im = Image.open('images/forever.png')
    new_meme = PIL.ImageDraw.Draw(im).multiline_text((0,0), random.choice(forever), fill = (255,255,255), font = fnt, align = 'center')
    Image.show(title=new_meme,command=None)
    
def realize_gen():
    im = Image.open('images/realize.png')
    new_meme = PIL.ImageDraw.Draw(im).multiline_text((0,0), random.choice(realize), fill = (255,255,255), font = fnt, align = 'center')
    Image.show(title=new_meme,command=None)
    
def simply_gen():
    im = Image.open('images/simply.png')
    new_meme = PIL.ImageDraw.Draw(im).multiline_text((0,0), random.choice(simply), fill = (255,255,255), font = fnt, align = 'center')
    Image.show(title=new_meme,command=None)
'''

#Old function that would designate text line character length based on image dimensions to allow for text wrapping - archived due to lack of functionality
'''
def line_len(meme_type):
    img = Image.open('images/' + meme_type[0] + '.png')
    width, height = img.size
    return int(width / 15)
'''

#Old function that would allow text wrapping on image - archived due to complexity
'''
def multi_line(str, meme_type):
    newphrase = '\n'.join([str[i:i+line_len(meme_type)] for i in range(0, len(str), line_len(meme_type))])
    return newphrase
'''
