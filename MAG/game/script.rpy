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
define a = Character("A-chan")
define yagoo = Character("Yagoo")

define aqua = Character("Minato Aqua")
define pekora = Character("Usada Pekora")
define matsuri = Character("Natsuiro Matsuri")
define suisei = Character("Hoshimachi Suisei")
define watame = Character("Tsunomaki Watame")

define nene = Character("Momosuzu Nene")
define polka = Character("Omaru Polka")
define lamy = Character("Yukihana Lamy")
define watame = Character("Shishiro Botan")

define subaru = Character("Oozora Subaru")
define mio = Character("Ookami Mio")
define okayu = Character("Nekomata Okayu")
define korone = Character("Inugami Korone")

define haachama = Character("Haachama")
define choco = Character("Yuzuki Choco")

define sora = Character("Tokino Sora")
define fubuki = Character("Shirakami Fubuki")

define asahi = Character("Asahi")


# The game starts here.

label start:

    scene bg sky with dissolve        
    play music "audio/cicadas.mp3" fadein 3.5 volume 0.7 loop

    narrator "Today the [date] of [month] [year], just another monotonous ever repetitive day."

    "Takumi Asahi, a university student at the zenith of normalcy begins his day."

    if day_str == "Mon" or "Tue" or "Wed" or "Thu" or "Fri":
        "Its [days] so Asahi is expected to attend his classes at his university."
    elif day_str == "Sat" or "Sun":
        "Although its [days], there are still extra classes to attend at his university."

    scene bg street1 with fade
    play music "audio/bgm1.mp3" fadein 3.5 volume 0.15 loop
        
    asahi "Looks like I'm definitely gonna be late for class (´Д`)."

    asahi "I swear day in and day out learning something that I'll never put into use."

    asahi "Not like I'll amount to anything anyways."

    asahi "But I don't think I can skip another class, my lecturer will probably bring this up with the faculty head."

    asahi "Ah the train station is right ahead."

    scene bg train_station with fade
    play music "audio/train_station_noise.mp3" fadein 3 volume 0.3 loop

    asahi "The train station is packed as always... I can't believe people are willing to consort to this mundane routine."

    scene bg train_station with fade
    play sound "audio/train_jingle.mp3" volume 0.4
    $ renpy.pause(5.8, hard=True)

    asahi "Looks like the train's arriving."

    scene bg inside_train with fade

    asahi "Looks like the morning rush is gone."

    show bg inside_train with vpunch

    asahi "But yet there are still people bumping into me"

    asahi "I swear I cannot catch a break."



    sora "Ohayoooo! (o^▽^o)" 

    sora "Oh, looks like I'm the first one here today..."

    sora "Maybe A-chan is here today, lemme search the office for a bit."

    "Sora proceeds to head towards the recording room"

    scene bg recording_room with Dissolve(time=1)

    # TODO: Add a left to right look around
    transform rightview:
        subpixel True zoom 0.98
        xpos -1.61
        yalign 0.5
    
    transform centerview:
        xpos -0.79
        yalign 0.5
        subpixel True zoom 0.98

    transform leftview:
        subpixel True zoom 0.98
        xpos -0.0
        yalign 0.5

    transform viewlowerright(duration=0):
        subpixel True zoom 1.24
        linear duration align(0.0,0.0)
    
    transform viewupperleft(duration=0):
        subpixel True zoom 1.24
        linear duration pos (1.04, 1.15) anchor (1.0,1.0)

    transform left_to_right:
        xalign 0.0
        linear 2.0 xalign 1.0

    transform pan_scene_right:
        xpos 0
        linear 2 xpos -800

    scene bg recording_room_large2
    camera:
        perspective True
        xpos 0
        linear 3.0 xpos 500

    sora "It doesn't look like a-chan is here either"

    camera:
        perspective True
        xpos 0
        linear -3.0 xpos -500

    scene bg black

    image text_effect:
                    "bg recording_room.png"
                    linear 0.1 xoffset -2 yoffset 2
                    linear 0.1 xoffset 3 yoffset -3
                    linear 0.1 xoffset 2 yoffset -2
                    linear 0.1 xoffset -3 yoffset 3
                    linear 0.1 xoffset 0 yoffset 0
                    repeat

    show text_effect
    "*Rustling sounds*"
    
    scene bg recording_room with fade
    show sora normal_half

    sora "What on earth is that sound?"

    sora "A-chan is that you???"

    show sora normal_half at right
    show a-chan normal_half at left

    a "Oh Sora you're here early today."

    sora "Yeah I came early to prepare for tonight's big 3D live event."

    a "That's hardworking of you!"

    a "But as of now I think we are still setting up the 3D live studio."

    a "I think you can go right ahead and eat something before the rehersal."

    sora "Sure thing! I'll grab something from the pantry."

label pantry:
    scene bg pantry with pixellate

    show sora normal_half

    sora "Lalalala..."

    scene bg black

    koyo "Guess who?"

    scene bg pantry

    show koyo normal

    koyo "Konkoyo~~"

    show koyo normal at left

    show sora normal_half at right 

    sora ""

    return
