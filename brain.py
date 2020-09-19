from tkinter import *
def speak(str):#speaking (text to speech)
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.spVoice")#dispatching the voice of sapi
    speak.Speak(str)#making sapi speak the string passed to it
    print(str)
def takeCommand():#taking command from user (speech to text)
    import pyaudio
    import speech_recognition as sr
    r=sr.Recognizer()
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        print("J A R V I S : Listening...\n")
        audio_data = r.listen(source)
        r.pause_threshold=1
        print("R e c o g n i z i n g . . . .\n")
        # convert speech to text
        try:
            text = r.recognize_google(audio_data)
        except:
            text = "Couldn't Recognise Sir.."
    print("You Said     : "+text+"\n")
    return text
def wish():#wishing the user
    import datetime
    fulldatetime=datetime.datetime.now()#getting todays date and time
    time=fulldatetime.strftime("%H")#getting hours of the day
    time=int(time)#converting the hours to int
    wish=""
    if time>=6 and time<=11:#morning
        wish="Good Morning Sir!."
    elif time>=12 and time<=16:#afternoon
        wish="Good Afternoon Sir!."
    elif time>=17 and time<=20:#evening
        wish="Good Evening Sir!."
    else:#night
        wish="Good Night Sir!"
    speak(wish)#wishing the user
class DateTime:#datetime
    import datetime
    try:
        import androidhelper
        droid=androidhelper.Android()
    except:
        pass
    fulldatetime=datetime.datetime.now()
    year=str(fulldatetime.year)
    day=fulldatetime.strftime("%A")
    month=fulldatetime.strftime("%B")
    date=fulldatetime.strftime("%d")
    time=fulldatetime.strftime("%I")+":"+fulldatetime.strftime("%M")+" "+fulldatetime.strftime("%p")
    def sayDate(self):
        saydate="Today is "+self.date+" of "+self.month+" "+self.year+" , Sir"
        speak(saydate)
    def sayYear(self):
        sayyear="This is the Year "+self.year+" , Sir"
        speak(sayyear)
    def sayDay(self):
        sayday="Today is "+self.day
        speak(sayday)
    def sayMonth(self):
        saymonth="This is the Month of "+self.month+" , Sir"
        speak(saymonth)
    def sayTime(self):
        saytime="Now is "+self.time+" , Sir"
        speak(saytime)
def norms():#normalities like yes ok etc
    import random
    norm=['Ok','Yes','Yeah','Okay']
    ran=random.randint(0,len(norm)-1)
    speak(norm[ran])    
def introduce():#introduces himself
    import random
    introds=['I am JARVIS your personal assistant, nice to meet you!',"I am JARVIS the ultimate A.I. and your personal assistant, tell me what to do!"] 
    ran=random.randint(0,len(introds)-1)
    speak(introds[ran])   
def readNews():#tells news
    import json
    import requests
    url=("http://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=5137d7ad84594010a3dbb6880a38434f")
    response = requests.get(url)
    text = response.text
    my_json = json.loads(text)
    speak("On the top of the headlines today we have.")
    speak(my_json['articles'][0]['title'])
    speak(my_json['articles'][0]['description'])
    speak("That's all for today, Sir")
def notifyWeather():#tells about todays weather
    import json
    import requests
    speak("Okay sir, let me check.")
    url=("http://api.weatherapi.com/v1/current.json?key= e703eb7e730245e6ae0135222202407&q=22.5726,88.3639")
    response = requests.get(url)
    text = response.text
    my_json = json.loads(text)
    weather="Today outside in "+my_json['location']['name']+" the weather is "+my_json['current']['condition']['text']+"y and the temperature has reached "+str(int(my_json['current']['temp_c']))+" degree celcius and, "+str(int(my_json['current']['humidity']))+" percent of humidity and, the sky is "+str(int(my_json['current']['cloud']))+" percent covered with cloud"
    speak(weather)
    if int(my_json['current']['temp_c'])>=26:
        speak('It\'s a hot sunny day outside!')               
def greet():#greets the user
    import random
    greets=['Hi Sir, tell me what to do','Hello Sir, I have been waiting for you']
    ran=random.randint(0,len(greets)-1)   
    gg=greets[ran]
    speak(gg)
def thank():#thanks the user
    import random
    thnx=["Thank you sir!","Thanks, sir"]
    ran=random.randint(0,len(thnx)-1)
    speak(thnx[ran])
def welcome():#welcomes the user
    speak('Your most welcome sir!')
def sendEmail():
    import webbrowser
    speak("Okay sir sending mail.")
    webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"))
    Openwb=webbrowser.get('chrome')
    Openwb.open("https://mail.google.com/mail/u/0/#inbox?compose=new")
    speak("What would you like to send sir?")
def translate():#for translation
    import googletrans
    languages=googletrans.LANGUAGES
    translator=googletrans.Translator()
    speak('Say your words,Sir!')
    source_text=takeCommand()
    if "couldn't recognise sir.." in source_text:
        speak(source_text) 
    else:
        try:
            source_lang=str(translator.detect(source_text).lang)
        except:
            speak("Couldn't detect the language")
        source_lang_formal=languages[source_lang]
        speak(f"Source language detected as {source_lang_formal}")
        speak("In which language do you want to translate it in Sir")
        target_lang=takeCommand()
        target_lang=target_lang.lower()
        if "couldn't recognise sir.." not in target_lang:
            if 'in ' in target_lang:
                target_lang=target_lang[3: ]
            else:
                target_lang=target_lang
            try:
                target_lang=get_key(target_lang,languages)
                target_text=translator.translate(source_text,dest=target_lang).text
                target_lang_formal=languages[target_lang]
                speak(f'In {target_lang_formal} it is said as {target_text}')
            except:
                speak('Couldn\'t detect this language sir.')
        else:
            speak(target_lang)
def get_key(key,my_dict):
    # list out keys and values separately 
    key_list = list(my_dict.keys()) 
    val_list = list(my_dict.values())
    #returning key of the value
    return (key_list[val_list.index(key)]) 
def tellAJoke():
    import json
    import requests
    speak('Let me tell you a really funny joke sir..')
    url = "https://joke3.p.rapidapi.com/v1/joke"

    headers = {
        'x-rapidapi-host': "joke3.p.rapidapi.com",
        'x-rapidapi-key': "4c4d89c18fmsh993ccbad4172cf5p164f80jsn9623322f0546"
        }

    response = requests.request("GET", url, headers=headers).text

    my_json=json.loads(response)
    speak(my_json['content']+", hehehe! hope you find it funny sir")
def coronaVirusStats():
    import requests
    import json
    country='India'
    speak('Of which country\'s corona stats you want sir?')
    country=takeCommand()
    if 'of ' in country:
        country=country[3: ]
    url = "https://covid-193.p.rapidapi.com/statistics"

    querystring = {"country":country}

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "4c4d89c18fmsh993ccbad4172cf5p164f80jsn9623322f0546"
        }
    try:
        response = requests.request("GET", url, headers=headers, params=querystring).text
        text=json.loads(response)  
        speak('Till date in '+text['response'][0]['country']+' there are '+text['response'][0]['cases']['new']+' new covid-19 cases, with '+str(text['response'][0]['cases']['active'])+' active cases, and '+str(text['response'][0]['cases']['critical'])+' critical cases, among which '+str(text['response'][0]['cases']['recovered'])+' pupils have succesfully recovered, with a total death of '+str(text['response'][0]['deaths']['total'])+' peoples')
        if text['response'][0]['cases']['active']!=0:
            speak('Don\'t worry sir we will soon get a way out of it!')
    except:
        speak('Couldn\'t find this region\' stats sir')
def getPassword():
    import random
    speak('Can you tell me the length of your password sir?')
    try:
        length=takeCommand()
        length=int(length)
        pwd='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$&?><[]'
        created=''
        for i in range(length):
            ran=random.randint(0,len(pwd)-1)
            created+=pwd[ran]
        speak("Here's your password on your screen sir.")
        class Window(Frame):
            def __init__(self, master=None):
                Frame.__init__(self, master)
                self.master = master
                self.pack(fill=BOTH, expand=1)
                
                text = Label(self, text=created)
                text.place(x=70,y=90)
                #text.pack()
                
        root = Tk()
        app = Window(root)
        root.wm_title("Password window")
        root.geometry("200x200")
        root.mainloop()  

    except:
        speak('Sorry sir couldn\'t recognise the length')
def getBattery():
    import psutil
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)
    if plugged==False: plugged="Not Plugged In"
    else: plugged="Plugged In"
    speak(" Your battery is "+percent+' percent charged and it is '+plugged)
    if int(percent)<30 and plugged!='Plugged In':
        speak('You should charge your computer as soon as possible sir')
    elif int(percent)>98:
        speak('Your computer is fully charged sir!')
def getWifiName():
    import subprocess
    results = subprocess.check_output(["netsh", "wlan", "show", "network"])
    results = results.decode("ascii") # needed in python 3
    results = results.replace("\r","")
    ls = results.split("\n")
    ls = ls[4:]
    ssids = []
    x = 0
    while x < len(ls):
        if x % 5 == 0:
            ssids.append(ls[x])
        x += 1
    speak("You are currently connected to, the wifi named "+ssids[0][9: ])
def randomFact():
    import requests
    import json
    import time
    import random
    types=['trivia','math','date','year']
    ran=random.randint(0,3)
    typee=types[ran]
    url = "https://numbersapi.p.rapidapi.com/random/"+typee

    querystring = {"max":"20","fragment":"true","min":"10","json":"true"}

    headers = {
        'x-rapidapi-host': "numbersapi.p.rapidapi.com",
        'x-rapidapi-key': "4c4d89c18fmsh993ccbad4172cf5p164f80jsn9623322f0546"
        }

    response = requests.request("GET", url, headers=headers, params=querystring).text

    my_json=json.loads(response)
    if typee=='trivia':
        speak('Let me tell you a '+my_json['type']+' sir')
        speak(my_json['text'])
        speak('Think it, I would give you time')
        time.sleep(6)
        speak('Dont you get it, it is the number '+str(my_json['number']))
    else:
        speak('Let me tell you a '+my_json['type']+' fact sir!')
        speak(my_json['text'])
        speak('Think it, I would give you time')
        time.sleep(6)
        speak('Dont you get it, it is the number '+str(my_json['number']))
def getTrivia():
    import requests
    import json
    import time
    import random
    typee='trivia'
    url = "https://numbersapi.p.rapidapi.com/random/"+typee

    querystring = {"max":"20","fragment":"true","min":"10","json":"true"}

    headers = {
        'x-rapidapi-host': "numbersapi.p.rapidapi.com",
        'x-rapidapi-key': "4c4d89c18fmsh993ccbad4172cf5p164f80jsn9623322f0546"
        }

    response = requests.request("GET", url, headers=headers, params=querystring).text

    my_json=json.loads(response)
    speak('Let me tell you a '+my_json['type']+' sir')
    speak(my_json['text'])
    speak('Think it, I would give you time')
    time.sleep(6)
    speak('Dont you get it, it is the number '+str(my_json['number']))

if __name__ == "__main__":
    randomFact()