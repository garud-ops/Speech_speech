from googletrans import Translator
import speech_recognition as sr
import pyttsx3

#1. Speech Recognition

#define speech recoginition
r=sr.Recognizer()

mic=sr.Microphone()


#recoginize speech

with mic as source: 
   r.adjust_for_ambient_noise(source,duration=0.2) 
   audio = r.listen(source) 
result = r.recognize_google(audio)
print(result)      #it is just for the viewing purpose



#2. Building the Translator
p=Translator()
k=p.translate(result,dest="nepali")
translated = str(k.text)
print(translated)



#3. Text to Speech Engine
engine = pyttsx3.init()

engine = pyttsx3.init() 
voices = engine.getProperty('voices') 
for voice in voices: 
  print("Voice:") 
  print(" - ID: %s" % voice.id) 
  print(" - Name: %s" % voice.name) 
  print(" - Languages: %s" % voice.languages) 
  print(" - Gender: %s" % voice.gender) 
  print(" - Age: %s" % voice.age)


#Define the speaker languag
fr_voice_id = "com.apple.speech.synthesis.voice.thomas" 
engine.setProperty('voice', fr_voice_id)

engine.say(translated)
engine.runAndWait()