try:
    from brain import *
    import webbrowser
    import wikipedia
    import os
    import json
    import time
except:
    print('Please install speechrecognition,pyaudio,wikipedia,pywin32,googletrans modules')
path=open('C:\\Users\\HP\\Desktop\\PROJECTS\\J A R V I S\\paths.json','r+')
path=path.read()
paths=json.loads(path)
try:
    webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(paths['chrome']))
    Openwb=webbrowser.get('chrome')
except:
    speak('Please change your default directory paths from paths.json')
    exit()
wish()
speak("tell me what to do")
date=DateTime()#instance of DateTime class
listening=True

while listening:
    query=" "+takeCommand()+" "
    query=query.lower()
    if ' news ' in query or ' head ' in query or 'headline' in query or 'slime' in query or 'precious' in query or 'read' in query or 'online' in query:#reads news
        if 'news' not in query:
            print("Recognised as : News")
        readNews()
    elif 'good morning' in query or 'goodmorning' in query or 'morning' in query or 'good night' in query or 'goodnight' in query or 'night'in query or 'good afternoon' in query or 'goodafternoon' in query or 'afternoon' in query or 'good evening' in query or 'goodevening' in query or 'evening' in query:
        wish()
    elif 'trivia' in query or 'quiz' in query:
        getTrivia()
    elif 'bore' in query or 'fact' in query:
        randomFact()
    elif 'hard' in query:
        speak('Yes I know')
    elif 'show me' in query or 'search' in query or 'what is' in query:
        speak('Showing sir')
        s='https://www.google.com/search?q='+query
        Openwb.open(s)
    elif 'created' in query:
        speak('Saptarshi Basu!, this is who created me')
    elif 'respond' in query:
        speak('Yes sir, I am here')
    elif 'dance' in query:
        speak('CHA CHA CHA, I like dancing')
    elif 'sing' in query:
        speak('La la la la, singing is my favourite part')
    elif 'what can you do' in query or 'what else can you do' in query:
        speak('I can cook some delicious dishes for you, sir')
    elif 'corona' in query or 'covid' in query:
        coronaVirusStats()
    elif 'transl' in query:
        translate()
    elif 'really' in query:
        speak('Really Sir!')
    elif ' eat ' in query:
        speak('I WANT TO EAT A LOT OF DATA SIR!!')
    elif ' saptarshi ' in query:
        speak("YES OFCOURSE, HE IS MY BEST FRIEND")
    elif 'joke' in query:
        tellAJoke()
    elif 'like you' in query:
        speak('I like you too, sir!')
    elif 'like' in query:
        speak('Oh I see!')
    elif ' emotions ' in query:
        speak('No I don\'t have emotions, I have errors')
    elif 'iron man' in query:
        speak('Yes! He is like a father to me..')
    elif 'avengers' in query:
        speak('How could I forget about the END-GAME')
    elif 'good day' in query or 'nice day' in query or 'great day' in query or 'excellent day' in query:
        speak("Yes sir, Indeed!")
    elif 'who are you' in query or ' name ' in query or 'wario' in query or 'wally' in query or 'dt' in query:
        introduce()
    elif 'who' in query and ' i ' in query:
        speak('You\'re a HUMAN, Sir')
    elif ' mail ' in query or ' gmail ' in query or ' email ' in query or ' google mail ' in query:
        sendEmail()
    elif ' time ' in query or 'tanga' in query:
        date.sayTime()
    elif 'horoscope' in query or 'future' in query or 'zodiac' in query or 'luck' in query:
        if 'future' in query:
            speak('Let me take a glimpse of the future sir')
            time.sleep(2)
            speak('Wooaahh It was such a great sight , our future is really bright sir!')
        else:
            speak('This is your luckiest day sir, as I could see!')
    elif ' year ' in query:
        date.sayYear()
    elif ' day ' in query or ' week' in query or ' weekday ' in query:
        date.sayDay()
    elif " couldn't recognise " in query:
        speak(query)
    elif ' hi ' in query or ' hello ' in query or ' hey ' in query or ' hii ' in query:
        greet()
    elif 'weather' in query or 'outside' in query or 'temperature' in query or 'humidity' in query or 'climate' in query:
        if 'weather' not in query:
            print("Recognised as : Weather\n")
        notifyWeather()
    elif 'I love' in query:
        speak('I LOVE YOU TOO')
    elif 'check your' in query or 'test your' in query:
        speak('Hello hello mic testing, It is working fine sir')
    elif 'password' in query:
        getPassword()
    elif ' wikipedia ' in query or 'me something about' in query or 'meaning of' in query or 'do you know' in query:
        speak("Okay sir, let me find....")
        if "tell me something about" in query:
            query=query[24: ]
        if "jarvis tell me something about" in query:
            query=query[31: ]
        if ' do you know ' in query:
            query=query[13: ]
        if ' do you know about ' in query:
            query=query[19: ]
        if ' jarvis do you know ' in query:
            query=query[20: ]
        if ' jarvis do you know about ' in query:
            query=query[26: ]
        try:
            print(query)
            speak((wikipedia.summary(query, sentences=2)))
        except:
            speak("Sorry Sir I couldn't find it")
    elif 'battery' in query:
        getBattery()
    elif 'wifi' in query or 'wi-fi' in query:
        getWifiName()
    elif ' date ' in query or 'torete' in query or 'just these words will smith' in query or '3d' in query or 'lisboa' in query or 'box' in query or 'fox' in query or 'dc' in query or ' de ' in query or 'vidal' in query or 'respetar' in query or 'dead' in query or 'desde' in query or ' et ' in query or 'ente' in query or ' te ' in query or 'fred' in query:
        if 'date' not in query:
            print("Recognised as : Date\n")
        date.sayDate()
    elif ' gmeet ' in query or ' google meet ' in query:
        Openwb.open("meet.google.com")
    elif ' mother ' in query:
        speak("Your mother is mother india, sir")
    elif ' father ' in query:
        speak("Your father is father india, sir")
    elif 'how are you' in query:
        speak("I am fine sir, how are you?")
    elif 'like me' in query:
        speak("Yes sir I do")
    elif ' facebook ' in query:
        speak("Okay sir")
        Openwb.open("facebook.com")
    elif ' very good ' in query or ' good ' in query or ' nice ' in query:
        thank()
    elif ' music ' in query:
        import random
        speak("Playing music sir")
        music_dir=paths['music_directory']
        songs=os.listdir(music_dir)
        ran=random.randint(0,len(songs)-1)
        try:
            os.startfile(os.path.join(music_dir,songs[ran]))
        except:
            speak("You have no music stored in that directory sir.")
    elif ' bad ' in query or 'wors' in query:
        speak('I\'am sorry sir')
    elif ' google ' in query or 'browser' in query or 'net' in query or 'chrome' in query:
        speak("Okay sir")
        Openwb.open("google.com")
    elif ' youtube ' in query:
        speak("Okay sir")
        Openwb.open("youtube.com")
        speak("What do you want to watch, sir")
        queryinyt=takeCommand()
        if 'funny' in queryinyt:
            Openwb.open('https://www.youtube.com/watch?v=GHhFtkGfaWU&list=PLtDp75hOzOlaQcPfx-Za_Dd1sOBPtdBw3')
            speak('Hope you would find it funny sir!')
    elif 'doing' in query:
        speak('I have been doing a lot of research on A.I. sir!')
    elif 'map' in query:
        Openwb.open('https://www.google.com/maps')
    elif ' thanks ' in query or ' thank you ' in query:
        welcome()
    elif ' quit ' in query or 'quinn' in query or 'shutdown' in query or 'biscuit' in query or 'bye' in query or 'puig' in query or 'quiz' in query or 'kuwait' in query or ' close ' in query or ' end ' in query:
        if 'quit' not in query:
            print('Recognised as : Quit')
        speak("Okay Sir, bye")
        listening=False
    elif ' jarvis ' in query:
        speak('Yes Sir!')
    else:
        norms()
