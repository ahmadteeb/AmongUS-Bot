# Ahmadteeb | Among US Auto Mute Bot for Discord

This bot mute/unmute s players in a specific server's channel named 'amongus'.  
It uses [Tesseract OCR](https://sourceforge.net/projects/tesseract-ocr/files/latest/download) which is a commercial quality OCR engine originally developed at HP between 1985 and 1995. In 1995, this engine was among the top 3 evaluated by UNLV. 

## Installation
1- Create an application from [Discord Developers](https://discord.com/developers/applications)  
2- Copy the application token to 'token.json'
3- Start the bot using the compiled file 'bot.exe'  
4- Start the bot from chat using the command mentioned

## Discord Commands 
* #start : starts the bot 

## How it works
The executable waits for the start command on the server's chat channel then waits for the game to start by detecting 'Impostor' or 'Crewmate' and immediately mutes everyone until a dead body is reported or an emergency meeting is called where it unmutes everyone after detecting 'who is the impostor' at the top. 

## Known Issues 
* The bot mutes everyone if the player running the bot opened in-game chat
* The bot might not work on screens with resolution other than 1920x1080 