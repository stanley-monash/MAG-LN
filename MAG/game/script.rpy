init python:
    import time

    year, month, day, hour, minute, second, dow, doy, dst = time.localtime()

    day_str = time.asctime(time.localtime())[0:3]

    if month == 1:
        month ="January"
    elif month == 2:
        month ="February"
    elif month == 3:
        month ="March"
    elif month == 4:
        month ="April"
    elif month == 5:
        month ="May"
    elif month == 6:
        month ="June"
    elif month == 7:
        month ="July"
    elif month == 8:
        month ="August"
    elif month == 9:
        month ="September"
    elif month == 10:
        month ="October"
    elif month == 11:
        month ="November"
    elif month == 12:
        month ="December"

    if day_str.lower() == "mon":
        days = "Monday"
    elif day_str.lower() == "tue":
        days = "Tuesday"
    elif day_str.lower() == "wed":
        days = "Wednesday"
    elif day_str.lower() == "thu":
        days = "Thurday"
    elif day_str.lower() == "fri":
        days = "Friday"
    elif day_str.lower() == "sat":
        days = "Saturday"
    elif day_str.lower() == "sun":
        days = "Sunday"
    else: days = "error"

    if day == 1 or day == 21 or day == 31:
        date = str(day) + "st"
    elif day == 2 or day == 22:
        date = "2nd"
    elif day == 3:
        date = "3rd"
    else:
        date = "%sth" % day

# Side Characters
define lecturer = Character("Lecturer")
define unknown = Character("???")

# Main Characters
define maou = Character("Maou chan")
define rika = Character("Tsumori Rika")
define towa = Character("Minami Towa")
define asahi = Character("Iwasaki Asahi")
define yuito = Character("Mitarai Yuito")

# The game starts here.

label start:

    scene bg sky with dissolve        
    $ player_name = renpy.input("What would you like to be called?")
    define mc = Character("[player_name]")

    play music "audio/cicadas.mp3" fadein 3.5 volume 0.7 loop

    narrator "Today the [date] of [month] [year], just another monotonous ever repetitive day."

    "[player_name], a university student at the zenith of normalcy begins his day."

    if days == "Monday" or days == "Tuesday" or days == "Wednesday" or days == "Thursday" or days == "Friday":
        "Its [days] so [player_name] is expected to attend his classes at Donash university."
    else:
        "Although its [days], there are still extra classes to attend at Donash university."

    scene bg street1 with fade
    play music "audio/bgm1.mp3" fadein 3.5 volume 0.15 loop
        
    mc "Looks like I'm definitely gonna be late for class (´Д`)."

    mc "I swear day in and day out learning something that I'll never put into use."

    mc "Not like I'll amount to anything anyways."

    mc "But I don't think I can skip another class, my lecturer will probably bring this up with the faculty head."

    mc "Ah the train station is right ahead."

    #TODO add foot step sfx

    scene bg train_station with fade
    play music "audio/train_station_noise.mp3" fadein 3 volume 0.3 loop

    mc "The train station is packed as always... I can't believe people are willing to consort to this mundane routine."

    window hide
    play sound "audio/train_jingle.mp3" volume 0.4
    $ renpy.pause(5.8, hard=True)

    mc "Looks like the train's arriving."

    #TODO add train door opening sounds

    scene bg inside_train with fade

    #TODO add inside train sounds

    mc "Looks like the morning rush is gone."

    #TODO add bump sounds
    show bg inside_train with vpunch

    mc "But yet there are still people bumping into me"

    mc "I swear I cannot catch a break."

    mc "Ah those 3 are from my class..."

    mc "Its kinda awkward I'll just pretend to be asleep"

    show bg black with dissolve
    $ renpy.pause(5, hard=False)
    #TODO add train announcement
    scene bg inside_train with fade

    mc "Looks like I've arrived at Donash University"
    #TODO add train opening sound 
    #TODO add walking sound 

    scene bg school_entrance with fade
    #TODO play some bgm
    mc "I swear Donash looks like your ordinary anime high school."

    mc "But can you believe it? It's a freakin university!"

    mc "Oh shit can't afford to waste any time, looks like I'm already 10 minutes late."

    #TODO play running sounds

    scene bg classroom with fade
    #TODO play door opening sounds

    mc "Sorry I'm late!"

    show lecturer normal at right
    
    lecturer "You are 15 minutes late!!!"

    lecturer "I don't really care if you show up to my class but I do have to follow regulations to report you if you miss more than 5 classes."

    mc "Sorry I won't miss class again."

    #TODO add walking and sitting down sfx

    scene bg classroom_sitting with fade

    lecturer "Ok sorry for the disruption class! We will be talking about Coloumb's law today."

    lecturer "So Coloumb's law is actually also called the inverse square law, can anybody tell me why?"

    mc "I'm falling asleep already just listening to that old hag babble on."

    mc "I guess I'll take a short nap and wake up before class ends."

    scene bg black with fade
    $ renpy.pause(3, hard=False)

    unknown "Hey are you ok?!"

    mc "zzz"

    unknown "Looks like he's still alive but the clothes he's wearing seems strange."

    mc "Who the hell is disturbing my damn nap!"

    scene bg forest with fade
    show maou normal at right

    unknown "!?!?!"

return
