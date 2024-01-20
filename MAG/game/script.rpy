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

    if day == 1:
        date = "1th"
    elif day == 2:
        date = "2nd"
    elif day == 3:
        date = "3rd"
    else:
        date = "%sth" % day

# Characters
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

    if day_str == "Mon" or "Tue" or "Wed" or "Thu" or "Fri":
        "Its [days] so [player_name] is expected to attend his classes at Donash university."
    elif day_str == "Sat" or "Sun":
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


return
