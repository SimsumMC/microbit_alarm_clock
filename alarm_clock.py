from microbit import *

import random
import datetime
import music

# Variablen

global hours
global minutes
global active

hours = -1
minutes = -1
active = True #damit der Wecker nur klingelt, wenn er aktiv ist und nicht NUR wenn die Standartwerte z.b 0 und 0 erfüllt sind

# Sprüche

# https://the-heros-journey.at/365-lebensweisheiten/

Sprueche = ["Kleine Dinge sind verantwortlich für große Veränderungen.",
            "Denke immer daran, dass es nur eine wichtige Zeit gibt: Heute. Hier. Jetzt.",
            "Man entdeckt keine neuen Kontinente ohne den Mut, alle Küsten aus den Augen zu verlieren.",
            "Überall sind wir von Wundern umgeben, wenn wir die Augen haben sie zu sehen.",
            "Leben ist das, was passiert, während du fleißig dabei bist, andere Pläne zu schmieden.",
            "Das Glück ist das einzige, was sich verdoppelt, wenn man es teilt.",
            "Fall siebenmal hin und steh achtmal auf.",
            "Man muss das Unmögliche versuchen, um das Mögliche zu erreichen.",
            "Nichts Großes ist je ohne Begeisterung geschaffen worden.",
            "All unsere Träume können wahr werden, wenn wir den Mut haben ihnen zu folgen.",
            "Gib jedem Tag die Chance, der schönste deines Lebens zu werden.",
            "Es sind die Begegnungen mit Menschen, die das Leben lebenswert machen.",
            "Entscheidend ist nicht, was uns im Leben zustößt, sondern wie wir darauf regieren.",
            "Have fun, be crazy, be weird. Get out and screw up. You are going to anyway, so you might as well enjoy the process.",
            "Gestern hast du morgen gesagt.",
            "Willpower lasts about two weeks and is soluble in alcohol.",
            "Es spielt keine Rolle, wie weit oder wohin du gereist bist, sondern wie lebendig du bist.",
            "Das wichtigste Stück des Reisegepäcks ist und bleibt ein fröhliches Herz.",
            "In fließendem Wasser kann man sein eigenes Bild nicht sehen, wohl aber in ruhigem Wasser. Nur wer selbst ruhig bleibt, kann zur Ruhestätte all dessen werden, was Ruhe braucht.",
            "Geben sie niemals, niemals, niemals auf.",
            "Ich kenne das Geheimnis des Erfolges nicht. Aber ich kenne das Geheimnis des Misserfolges: es allen recht machen zu wollen.",
            "Tue erst das Notwendige, dann das Mögliche und plötzlich schaffst du das Unmögliche.",
            "Das Dasein ist köstlich, man muss nur den Mut haben, sein eigenes Leben zu führen.",
            "Jede schwierige Situation, die du jetzt meisterst, bleibt dir in Zukunft erspart.",
            "Ein bisschen Freundschaft ist mir mehr wert, als die Bewunderung der ganzen Welt.",
            "Manchmal braucht man nur 20 Sekunden den unbändigen Mut, seinem Herzen zu folgen. Manchmal muss man sich 20 Sekunden komplett zum Affen machen. Doch immer kommt etwas Großartiges heraus.",
            "Halte dein Herz frei von Hass und deinen Geist frei von Angst und Sorge. Lebe einfach, erwarte wenig, gib viel. Erfülle dein Leben mit Liebe und verbreite Fröhlichkeit. Vergiss dich selber, denke an andere. Sei so, wie              du es von anderen wünschst.",
            "If you set your goal ridiculously high and it is a failure, you will fail above everyone else’s success.",
            "Der Schwache kann nicht verzeihen. Verzeihen ist eine Eigenschaft des Starken.",
            "Dem Geist sind keine Grenzen gesetzt außer denen, die wir als solche anerkennen",
            "Ein Pessimist sieht die Schwierigkeiten in jeder Möglichkeit, ein Optimist sieht die Möglichkeiten in jeder Schwierigkeit.",
            "Angst kann jemanden zu Größe führen oder ihn auf Sicherheit und Mittelmäßigkeit beschränken. Die Entscheidung liegt bei einem selbst",
            "Wenn ich mich danach fühle zu tanzen, tanze ich. Ich kümmere mich nicht darum, ob irgendjemand sonst tanzt oder jeder über mich lacht. Ich tanze.",
            "Wir müssen unseren Nächsten lieben – entweder weil er gut ist, oder damit er gut werde.",
            "Solche wähle zu Begleitern auf des Lebens Bahn, die dein Herz und deinen Geist erweitern.",
            "Man kann nicht jeden Tag etwas Großes tun, aber gewiss etwas Gutes.",
            "Suche nicht nach Fehlern, suche nach Lösungen.",
            "Den größten Fehler, den man im Leben machen kann, ist, immer Angst zu haben, einen Fehler zu machen.",
            "Wenn du dein Land ändern willst, musst du erst einmal dein Dorf ändern, wenn du dein Dorf ändern willst, musst du erst einmal deine Familie ändern und wenn du deine Familie ändern willst, musst du erst einmal dich                    selbst ändern.",
            "Um loszulegen, muss man aufhören zu reden und anfangen zu handeln.",
            "Der Weg zum Glück besteht darin, sich um nichts zu sorgen, was sich unserem Einfluss entzieht.",
            "Wärme und Kälte unserer Welt, ihr Licht und ihre Dunkelheit gehen von unserem Herzen aus.",
            "Jeder angenehme Augenblick hat Wert für mich. Glückseligkeit besteht nur in Augenblicken. Ich wurde glücklich, da ich das lernte.",
            "Ich liebe das Leben, weil mich die Menschen und ihr Werden unendlich interessieren. Durch mein Interesse wächst mein Wissen um sie beständig. Und dieses lässt mich glauben, dass das gewöhnliche menschliche Herz von                  Natur aus gut ist.",
            "Der Gedanke ist alles. Der Gedanke ist der Anfang von allem. Und Gedanken lasen sich lenken.",
            "Die gute Zeit fällt nicht vom Himmel, sondern wir schaffen sie selbst, sie liegt in unseren Herzen eingeschlossen.",
            "Ich gehe diesen Weg nur ein einziges Mal; alles Gute und Freundliche, das ich irgendeinem Menschen erweisen oder bezeigen kann, lass mich deshalb sogleich tun. Lass es mich nicht hinausschieben und nicht                              vernachlässigen, denn ich werde diesen Weg kein zweites Mal gehen.",
            "Es gibt Leute, die ihr ganzes Leben lang „nächste Woche“ anfangen wollen.",
            "Jeder neue Tag ist ein unentdecktes Land, das Abenteuer, Herausforderungen und Schätze verheißt.",
            "Der Schlüssel zum Herzen der Menschen wird nie unsere Klugheit, sondern immer unsere Liebe sein.",
            "Es gibt Momente, die tragen die Schönheit des ganzen Lebens in sich."]

# Bilder

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


# Funktionen

def alarm_check():
    if active == True and hours == datetime.datetime.now().hour and minutes == datetime.datetime.now().minute:
        return True
    else:
        return False


def delete_alarm():
    global hours
    global active
    if active != False:
        display.scroll("B zum abbrechen")
        sleep(1000)
        if button_b.get_presses():
            return
        else:
            hours = 0
            minutes = 0
            active = False
    else:
        display.scroll("Es wurde kein Wecker gestellt")


def showsentence(sentence="undefined"):
    sentencesplit = sentence.split()
    for x in sentencesplit:
        sleep(500)
        if button_a.get_presses() >= 1:
            display.clear()
            break
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
                display.scroll(str(hours))
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
                display.scroll(str(minutes))
        elif pin_logo.is_touched():
            hours = -1
            minutes = -1
            return False
        elif button_b.get_presses():
            return True


def set_clock():
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

def get_time_str():
    time = datetime.datetime.today().strftime("%H:%M")
    return time


def alarm():
    Animation = [sun1, sun2, sun3]
    display.show(Animation, delay=500)
    for x in range(10):
        music.play(music.PRELUDE)
        if button_a.get_presses():
            active = False
            return
        elif pin_logo.is_touched():
            snooze()
            return


def snooze():
    global minutes
    global hours
    minutes += 10
    if minutes >= 60:
        minutes = minutes - 60
        hours += 1
        if hours == 24:
            hours = 0


# Endlosschleife

while True:
    display.scroll(get_time_str())
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
