#voice ai bot 

#module to be installed    
#speech to text
#text to speech

#text to speech module python text to speech
#pip install pyttsx3
import pyttsx3  

#speech recongintion
#pip install speechrecognition
import speech_recognition as sr

#for searching in web_browser
#pip install web_browser
#webbrowser is a standard library in python
import webbrowser

#for realtime date and time
#import datetime module
#datetime is a standard library in python
import datetime

#install any additional python modules
import pyjokes

import os
import time
#define function to convert speech to text
def speech_to_text():
    #define variables "recognizer"
    #call's speech recongizer as 'sr' library functions
    recognizer = sr.Recognizer()
    #use class 'Recognizer' as recognizer from alias 'sr'
    # methods(or Functions) in 'sr' module Microphone()
    #methods in Recognizer
    #adjust_for_ambient_noise(),listen(),audio,data,recognize_google()
    
    with sr.Microphone() as source:
        print("Listerning.....")
        #adjust for ambient noise in source
        recognizer.adjust_for_ambient_noise(source)
        #listern and store source in audio var
        audio = recognizer.listen(source)
        #try exception handling
        try:
            print("Recognizing.....")
            #using google.recognizer()
            data = recognizer.recognize_google(audio)
        
            print(data)
            return data
        #exception handling
        except sr.UnknownValueError:
            print("Not Understanding....")
            

#define text to speech function
#install google_text_to_speech(gTTS) module and playsound
#pip install gTTS            
#pip install playsound
            #text_var the text to converted to speech
def text_to_speech(text_var):
    #use module 'pyttsx3' as engine
    #methods in pyttsx3 alias engine
    #getProperty(),setProperty(),voice,rate,say()
    #runAndWait()
    engine = pyttsx3.init()
    #get property of voice
    voices = engine.getProperty('voices')
    #set the properties of the voices 
    #need to install voices in the sysytem
    # 2 voices are present voices[0].id is male
    #voice[1].id is female 
    #other voice indexes if other voice option are present
    engine.setProperty('voices',voices[0].id)
    
    #to set the speed of the voice create a var 'rate'
    rate = engine.getProperty('rate')
    #set rate as 150 or any value of interest
    engine.setProperty('rate',150)
    #say(text_var) method speaks the vaariable text_var
    engine.say(text_var)
    #runAndWait() method waits till text is converted to speech
    engine.runAndWait()

#calling function speech to text
#speech_to_text()
#text_to_speech("Hello! Welcome Jose Ukken")
#using __name__ == '__main__' so the above and below functions called seperately    

if __name__ == '__main__':

    if "hey jarvis" in speech_to_text().lower():
        while True:       
            data1 = speech_to_text().lower()      

            #speaking with ai
            if "your name" in data1:
                name="My name is Jarvis"
                text_to_speech(name)
            elif "old are you" in data1:
                age="I am one day old!"
                text_to_speech(age)
            elif "time now" in data1:
                #datetime module ,datetime function ,now
                time = datetime.datetime.now().strftime("%I%M%p")
                text_to_speech(time)
            elif "open youtube" in data1:
                #text_to_speech("Opening YouTube")
                webbrowser.open("https://www.youtube.com")
            elif "joke" in data1:
                #text_to_speech("Let me think!")
                jokes = pyjokes.get_joke(language="en",category="neutral")
                #print(jokes)
                text_to_speech(jokes)

            
            #elif "play song" in data1:
            #    addrs = r"song folder address"
            #    listsong=os.listdir(addrs)
            #    #address and song number from the list 
            #    os.startfile(addrs,listsong[0])

           #if "exit" is read from data1 or speech to text
            elif "exit" in data1:
                text_to_speech("Thank you!")
                break
            #function repeats after time.sleep
            time.sleep(5)
                

    else:
        print("Thanks")
        text_to_speech("Thanks")


