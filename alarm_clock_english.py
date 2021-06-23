from microbit import *

import random
import datetime
import music

# Variables

hours = -1
minutes = -1
active = False #to alarm only if its active and not when only the default values are fullfilled

# Sentences (translated from German to English by deepl.com)

# https://the-heros-journey.at/365-lebensweisheiten/

Sprueche = ["Small things are responsible for big changes",
            "Always remember that there is only one important time: Today. Here. Now."
            "You don't discover new continents without the courage to lose sight of all the coasts",
            "Everywhere we are surrounded by wonders, if we have the eyes to see them.",
            "Life is what happens to you while you are busy making other plans",
            "Happiness is the only thing that doubles when you share it",
            "Fall down seven times and get up eight.",
            "You must try the impossible to achieve the possible.",
            "Nothing great has ever been created without enthusiasm",
            "All our dreams can come true if we have the courage to follow them",
            "Give every day the chance to be the best day of your life",
            "It is the encounters with people that make life worth living",
            "What matters is not what happens to us in life, but how we react to it.",
            "Have fun, be crazy, be weird. Get out and screw up. You are going to anyway, so you might as well enjoy the process.",
            "Yesterday you said tomorrow",
            "Willpower lasts about two weeks and is soluble in alcohol.",
            "It doesn't matter how far or where you've travelled, it's how alive you are",
            "The most important piece of luggage is, and always will be, a cheerful heart",
            "You cannot see your own image in flowing water, but you can in calm water. Only he who himself remains calm can become the resting place of all that needs calm.",
            "Never, never, never give up.",
            "I do not know the secret of success. But I do know the secret of failure: trying to please everyone.",
            "First do what is necessary, then what is possible, and suddenly you achieve the impossible.",
            "Existence is delicious, you just have to have the courage to live your own life.",
            "Every difficult situation you overcome now, you'll be spared in the future.",
            "A little friendship is worth more to me than the admiration of the whole world",
            "Sometimes all you need is 20 seconds of unbridled courage to follow your heart. Sometimes you have to make a complete fool of yourself for 20 seconds. But something great always comes out of it.",
            "Keep your heart free from hate and your mind free from fear and worry. Live simply, expect little, give much. Fill your life with love and spread cheerfulness. Forget yourself, think of others. Be as you wish others to be.",
            "If you set your goal ridiculously high and it is a failure, you will fail above everyone else's success.",
            "The weak cannot forgive. Forgiveness is a quality of the strong.",
            "There are no limits to the mind except those we recognise as such",
            "A pessimist sees the difficulty in every possibility, an optimist sees the possibility in every difficulty",
            "Fear can lead someone to greatness or limit them to safety and mediocrity. The choice is up to oneself",
            "If I feel like dancing, I dance. I don't care if anyone else is dancing or if everyone is laughing at me. I dance.",
            "We must love our neighbour - either because he is good, or so that he may become good.",
            "Choose such companions in the path of life as will enlarge your heart and mind.",
            "You can't do something great every day, but you can certainly do something good",
            "Don't look for mistakes, look for solutions",
            "The biggest mistake you can make in life is to always be afraid of making a mistake",
            "If you want to change your country, you must first change your village, if you want to change your village, you must first change your family, and if you want to change your family, you must first change yourself",
            "To get started, you have to stop talking and start acting.",
            "The way to happiness is not to worry about anything that is beyond our control",
            "The warmth and coldness of our world, its light and darkness, emanate from our hearts.",
            "Every pleasant moment has value for me. Bliss exists only in moments. I became happy because I learned that.",
            "I love life because I am infinitely interested in people and their becoming. Through my interest, my knowledge of them grows constantly. And this makes me believe that the ordinary human heart is inherently good.",
            "Thought is everything. Thought is the beginning of everything. And thought can be guided.",
            "The good time does not fall from the sky, we create it ourselves, it is locked in our hearts",
            "I go this way but once; all good and kindness, therefore, that I can do or show to any man, let me do it at once. Let me not put it off or neglect it, for I will not go this way a second time.",
            "There are people who want to start next week all their lives.",
            "Every new day is an undiscovered land that promises adventure, challenges and treasures.",
            "The key to people's hearts will never be our cleverness, but always our love.",
            "There are moments that carry the beauty of all of life."]

# Pictures

sun1 = Image('00000:'
             '00000:'
             '00900:'
             '00000:'
             '00000:')
sun2 = Image('00000:'
             '09990:'
             '09990:'
             '09990:'
             '00000:')
sun3 = Image('90909:'
             '09990:'
             '99999:'
             '09990:'
             '90909:')


# Functions

def alarm_check():
    if active == True and hours == datetime.datetime.now().hour and minutes == datetime.datetime.now().minute:
        return True
    else:
        return False


def delete_alarm():
    global hours, active, minutes
    if active == True:
        display.scroll("B zum abbrechen")
        sleep(1000)
        if button_b.get_presses():
            return
        else:
            hours, minutes = -1, -1
            active = False
    else:
        display.scroll("Es wurde kein Wecker gestellt")


def showsentence(sentence="undefined"):
    sentencesplit = sentence.split()
    for x in sentencesplit:
        sleep(500)
        if button_a.get_presses():
            display.clear()
            return
        display.scroll(x)


def set_hours():
    global hours
    display.scroll("Stunden:")
    while True:
        if button_a.get_presses():
            hours += 1
            if hours <= 9:
                display.show(str(hours))
            elif hours > 23:
                hours = 0
                display.show(str(hours))
            else:
                display.scroll(hours)
        elif pin_logo.is_touched():
            hours = -1
            return False
        elif button_b.get_presses():
            return True


def set_minutes():
    global minutes
    display.scroll("Minuten:")
    while True:
        if button_a.get_presses():
            minutes += 1
            if minutes <= 9:
                display.show(str(minutes))
            elif minutes == 60:
                minutes = 0
                display.show(str(minutes))
            else:
                display.scroll(minutes)
        elif pin_logo.is_touched():
            hours, minutes = -1, -1
            return False
        elif button_b.get_presses():
            return True


def set_clock():
    global active
    display.scroll("B zum abbrechen")
    sleep(1000)
    if button_b.get_presses():
        return
    while True:
        if set_hours():
            if set_minutes():
                active = True
                return
            else:
              return
        else:
          return 

        
def alarm():
    global hours, minutes
    Animation = [sun1, sun2, sun3]
    display.show(Animation, delay=500)
    for x in range(10):
        music.play(music.PRELUDE)
        if button_a.get_presses():
            active = False
            hours, minutes = -1, -1
            return
        elif pin_logo.is_touched():
            snooze()
            return


def snooze():
    global minutes, hours
    minutes += 10
    if minutes >= 60:
        minutes = minutes - 60
        hours += 1
        if hours == 24:
            hours = 0
            


# Loop

while True:
    display.scroll(datetime.datetime.today().strftime("%H:%M"))
    if alarm_check():
        alarm()
    elif button_a.get_presses():
        display.clear()
        showsentence(random.choice(Sprueche))
    elif button_b.get_presses():
        display.clear()
        set_clock()
    elif pin_logo.is_touched():
        delete_alarm()
