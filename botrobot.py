import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os



engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print (voices)
engine.setProperty('voice',voices[0].id)
#engine.say("Afternoon boss ! I am Jaarvis ! How can i help you")


print(voices[0].id)

engine.runAndWait()


def Speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        Speak("Good morning !")

    elif hour>=12 and hour<18:
        Speak("good afternoon!")

    else:
        Speak("good eeveening!")

    Speak("hello sir !I am Your assistant ! ,How can i help you !sir")




def takeCommand():

 r=sr.Recognizer()
 with sr.Microphone() as source:
       print("Listening......")
       r.pause_threshold = 1
       audio=r.listen(source)

 try:
        print("Recognizing.......")
        query=r.recognize_google(audio,language= 'en-in')
        print(query)
        print("User said:, {query}\n")
 except Exception as e:
         print("say that again please........")
         #Speak("say that again please.........")
         print(e)
         return "none"
    
 return query

                

   



if __name__ == "__main__":
   wishMe()
   while 1:
       query=takeCommand().lower()

       if 'wikipedia' in query:
         Speak("sure sir! searching for the same on wikipedia......")
         query=query.replace("wikipedia","")
         results=wikipedia.summary(query,sentences=2)
         Speak("According to wikipedia")
         print(results)
         Speak(results)

       elif ' youtube' in query:
           Speak("okay! here you go for youtube")
           webbrowser.open("youtube.com")

       elif ' google' in query:
         Speak("Opening google! please wait")
         webbrowser.open("google.com")

       elif ' facebook' in query:
         Speak("okay ! I am Redirecting you to facebook")
         webbrowser.open("facebook.com")

       elif 'music' in query:
           Speak("I am Playing your favourite one ! I hope you will like it")
           music_dir = 'E:\\SACHIN\\JAVA\\memory card 32\\1\\Music'
           songs=os.listdir(music_dir)
           print(songs)
           os.startfile(os.path.join(music_dir,songs[5]))
        
            
            

            


          


 

        

            

            
        
    
         

       

           

           
        


       

     

      
  


