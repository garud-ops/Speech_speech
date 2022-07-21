from logging.config import listen
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import os
import datetime




r=sr.Recognizer()
translator= Translator()

#step 1
#speech to text
print("Speak: ")
while True:
    # r=sr.Recognizer()
    with sr.Microphone() as source:
        # print("Speak Now",end=" ")
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio=r.listen(source)#The ,phrase_time_limit=8 parameter is the maximum number of seconds that this will allow a phrase to continue before stopping and returning the part of the phrase processed before the time limit was reached. The resulting audio will be the phrase cut off at the time limit. If phrase_timeout is None, there will be no phrase time limit.
        try:
            speech_text=r.recognize_google(audio,language="en-US")
            # print(speech_text,end=" ")
            # print("done",end=" ")
        except sr.RequestError:
            print("Could not find the request from google") 
        except sr.UnknownValueError:
            # print("Speech not Recognize")
            # print("Are you there if yes speak Now")
            # print("~~~~~~~~~~~~~~Recording")
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio=r.listen(source)   #,phrase_time_limit=8
            try:
                speech_text=r.recognize_google(audio,language="en-US")
                # print(speech_text,end=" ")
                # print("Done")
            except sr.UnknownValueError:
                print("Speech not Recognize")
                break
            except sr.RequestError:
                print("Could not find the request from google")
        # if speech_text=="exit": #when using translation comment if condition
        #     break
        

        

    #step 2
    #txt to text translation
        translated_text=translator.translate(speech_text,dest="zh-cn")
        # print(translated_text)
        text=translated_text.text
        if text=="Exit" or text=="Stop" or text=="Halt": #rukh jaao: Halt
            print("Microphone Stopped")
            break
        print(text)
        
        


    #step 3
    #translated text to translated language
        # voice=gTTS(text,lang="en")
        
        # voice.save("voice.mp3")
        # playsound("voice.mp3")


        #step 3
    # #translated text to translated language
        tts=gTTS(text,lang="en-IN")
        # if voice=="exit":
        # break
        date_string = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
        filename = "voice"+date_string+".mp3"
        tts.save(filename)
        playsound(filename)
        os.remove(filename)
        # os.close(source)
        
        

        
   
        

 