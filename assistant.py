#There are 3 major functions this assistant can perform
#Ask 1: any sentence using 'time' word to get the current time
#Ask 2: any sentence using 'play' word and then the name of the song to play it on youtube
#Ask 3: any sentence using 'about' word and then the name of the object you are searching for

#Note:
#Please try to give instruction only after the assistant finishes talking


import speech_recognition as sr #importing the speech recognition package
import pyttsx3 as pt #importing text to speech package
import datetime as dt #import this package to track the current time
import pywhatkit as kit #import this package to play song on youtube
import wikipedia #import wikipedia package to retrieve some info from wiki


#initializing objects for the functions of the packages
listener = sr.Recognizer()
assistant= pt.init()


#this piece of code turns the default male voice into woman's voice
voices = assistant.getProperty('voices')
assistant.setProperty('voice', voices[1].id)

#function fot the assistant to speak
def talk(text):
    assistant.say(text)
    assistant.runAndWait()


#fucntion for the assistant to be able to take command
def takeCommand():

 try:
    with sr.Microphone() as source:
        start= 'You can ask me time, to play song or about any info after I finish.'

        talk(start)

        voice = listener.listen(source) #the listener is listening to the source

        command= ''
        command = listener.recognize_google(voice) #translating the instruction into text by google
        command = command.lower()

 except:
    pass

 return command


#this is the main program that runs the assistant
def run_assistant():



    command= takeCommand()
    print(command) #displays the command spoken by the user

    if 'assistant' in command:
        command = command.replace('assistant', '')

#to speak the time by assistant
    if 'time' in command:
        timeSt= dt. datetime. now(). strftime('%I and %M')

        talk('Current time is '+timeSt) #telling the time

#to play any song by the assistant on youtube
    elif 'play' in command:
        song= command.replace('play', '')

        kit.playonyt(song) #playing the song

#to read any information from wikipedia
    elif 'about' in command:
        item= command.replace('search', '')
        info= wikipedia.summary(item,2)

        talk(info) #telling the information

#to shut down the system
    elif 'exit' in command:
        exit(0) #ending the session

#if there is any other task out of these ones
    else:
        talk('I cannot hear anything from you or I do not have this function to serve.')


#this assistant will keep asking for the instruction till user says exit
while True:
 run_assistant() #calling the main function
