from discord.utils import get
from discord.ext import tasks
from discord.ext import commands
import cv2
import pytesseract
import pyautogui
import json

pytesseract.pytesseract.tesseract_cmd = "OCR/tesseract.exe"
screenWidth, screenHeight = pyautogui.size()

if(screenHeight == 1080): #1920x1080 
    Center = (100, 100, 1500, 300)
    Center2 = (500, 100, 800, 90)
    Left_Top = (30 , 15, 300, 78)
# elif(screenHeight == 768): #1366x768
#     Center = (100, 100, 1500, 300)
#     Left_Top = (30 , 15, 300, 78)

def Image2Text(Region, _Color=cv2.COLOR_BGR2GRAY, _2blackandwhite=True, debug=False):
    pyautogui.screenshot("Temp/temp.png", region = Region)
    screen_shot = cv2.imread('Temp/temp.png')
    screen_shot = cv2.cvtColor(screen_shot, _Color)
    if(_2blackandwhite):
        screen_shot = cv2.adaptiveThreshold(screen_shot, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)
    Text = pytesseract.image_to_string(screen_shot).split("\n")
    if(debug):
        print(Text)
    return Text[0]


global Mute_Member
global Channel_ID

client = commands.Bot(command_prefix = '#')

@client.event
async def on_ready():
    print("Bot is Ready")

@client.command()
async def start(ctx):
    await ctx.send("I'm Ready!")
    global Channel_ID
    Channel_ID = get(ctx.guild.channels, name = "amongus").id
    await amongus()

async def amongus():
    NewGame = True
    Mute_Member = False
    while True:
        if(NewGame):
            CMorIM = Image2Text(Center,_2blackandwhite=False)
            if("Impostor" == CMorIM or "Crewmate" == CMorIM):
                for member in list(client.get_channel(Channel_ID).members):
                    await member.edit(mute = True)
                NewGame = False
                Mute_Member = True
                while True:
                    if("TOTAL TASKS COMPLETED" == Image2Text(Left_Top, _2blackandwhite=False, _Color=cv2.COLOR_BGR2RGB)):
                        break
        
        else:
            if(Mute_Member):
                while "wmngmg" != Image2Text(Center2):
                    if("Uictoru" == Image2Text(Center,_2blackandwhite=False) or "Defeat" == Image2Text(Center,_2blackandwhite=False)):
                        for member in list(client.get_channel(Channel_ID).members):
                            await member.edit(mute = False)
                        NewGame = True
                        break

                for member in list(client.get_channel(Channel_ID).members):
                    await member.edit(mute = False)
                Mute_Member = False
            else:
                while "wmngmg" == Image2Text(Center2):
                    pass
                while("TOTAL TASKS COMPLETED" != Image2Text(Left_Top, _2blackandwhite=False, _Color=cv2.COLOR_BGR2RGB)):
                    if("Uictoru" == Image2Text(Center,_2blackandwhite=False) or "Defeat" == Image2Text(Center,_2blackandwhite=False)):
                        for member in list(client.get_channel(Channel_ID).members):
                            await member.edit(mute = False)
                        NewGame = True
                        break

                for member in list(client.get_channel(Channel_ID).members):
                    await member.edit(mute = True)
                Mute_Member = True

with open("token.json") as token_file:
    token = json.load(token_file)["token"]
if token: 
    client.run(token)
else: 
    print ("[*] Please add token to token.json and restart !!!")
