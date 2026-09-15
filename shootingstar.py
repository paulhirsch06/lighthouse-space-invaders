datei = open("game_imports.txt", "r")
eingabe = datei.read()

exec(eingabe) #Exec ist eine Python-Funktion, mit der Pythoncode zur Laufzeit als String ausgefüfhrt wird

WIDTH = 560
HEIGHT = 700
# Verbindung mit Lighthouse herstellen
conn = Pyghthouse(username, token)
Pyghthouse.start(conn)

#Zustände definieren
STATE_START = "start"
STATE_GAME = "game"
STATE_GAME_OVER = "game_over"
STATE_SCORE = "score"

state = STATE_START

#variablen für Monster  
x_pos = 14
y_pos = 6

#Werden genutzt um das Monster auf dem Startbildschirm zu bewegen
dx = 1
dy = 1

#Für das Monster im Startbildschirm
frame_counter = 0
speed_divider = 6

#Position Kanone 
Kx_pos = 14
Ky_pos = 12


#monster shapes festlegen 
monster1 = [
        (0,0), (1,0), (1,1)
        ]
    
monster2 = [
        (0,0), (1,0),
        (0,1), (1,1),
        ]
    
monster3 = [
        (0,0), (1,0), (2,0), (0,1),
        ]
    
monster_list = [monster1, monster2, monster3]

monsters = []
spawn_clock = 0
    
farbe_play = (20,255,75)


monster_shape = [
(0,0),(1,0),(2,0),
(-1,1),(1,1),(3,1),
(-1,2),(0,2),(1,2),(2,2),(3,2),
(-1,3),(3,3),
]

farbe_monster = (188, 20, 255)

#mögliche Farben für Monster
colour_list = [
    (188, 20, 255), (235, 52, 161), (245, 245, 5), (255, 255, 255), (58, 235, 52)
    ]


frame_counter2 = 0
speed_divider2 = 30

frame_counter3 = 0
speed_divider3 = 5

frame_counter4 = 0
speed_divider4 = 4

#Kanonenkugel

farbe_kugel = (247, 2, 11)


kugel_liste = []

#Blinkcounter für das Game Over
blink_counter = 0
blink_speed = 30   # je größer, desto langsamer blinkt es
visible = True

farbe_game_over = (247, 2 , 11)

#Fallgeschwindigkeit
fall_speed = 1

#Variable Spielscore

score = 0

def kollisions_test():
    
    global monsters, kugel_liste, score
    
    #Kollision Kugel Monster innerhalb von der Bewegung der Kugel und der des Monsters um ein ,,Durchgleiten'' zu vermeiden
    for monster in monsters[:]:#Hier werden Kopien der Liste durch : erzeugt, da sonst bei iterieren über die Liste und gleichzeitigem Löschen aus dieser Elemente übersprungen werden könnten
        for kugel in kugel_liste[:]:
        
            for (mx, my) in monster["number"]:#Wir überprüfen jeden einzelnen Pixel des Monsters
                
                block_x = monster["x"] + mx
                block_y = monster["y"] + my
                
                if kugel["k1"] == block_x and kugel["k2"] == block_y:
                    kugel_liste.remove(kugel)
                    monsters.remove(monster)
                    
                    score += 1
                    
                    break
            
            else: #Wird nur ausgeführt, wenn die Schleife nicht vorher durch break abgebrochen wurde
                continue
            
            break #Beendet die Kugel Schleife, wenn das jeweilige Monster getroffen wurde
    

    

def draw_start():
    
    global x_pos, y_pos, dx, dy, frame_counter, speed_divider, play, farbe_play, monster_shape, farbe_monster
    
    image = Pyghthouse.empty_image()
    


   

    # PLAY zeichnen
    for (x,y) in play:
        image[y][x] = farbe_play

    # Monster zeichnen
    for (mx,my) in monster_shape:
        x = x_pos + mx
        y = y_pos + my

        if 0 <= x < 28 and 0 <= y < 14:
            image[y][x] = farbe_monster

    


   
    Pyghthouse.set_image(conn, image)
    
    for y in range(14):
        for x in range(28):
            color = image[y][x]
            screen.draw.filled_rect(Rect(x*20, y*50, 20, 30), color)
    
    
def draw_game():
    
    global Kx_pos, Ky_pos, monsters, farbe_kugel, kugel_x, kugel_y, kugel_liste
    image = Pyghthouse.empty_image()
    
    #kanone erzeugen
    Kanone = [
        (0,0), (0,1),
        (-1,1),(1,1),
        ]
   
    Kanone_farbe = (3, 252, 215)
    
    for (kx,ky) in Kanone:
        kanone_x = Kx_pos + kx
        kanone_y = Ky_pos + ky
        image[kanone_y][kanone_x] = Kanone_farbe
    
    
    
    #Monster zeichnen
    for monster in monsters:#Monsters ist eine anfangs leere Liste
        for (mx,my) in monster["number"]: #Im Wörtbuch monster, greifen wir auf die Variable number zu, welche für das jeweilioge Monster aus monster_list steht
            x = monster["x"] + mx
            y = monster["y"] + my
            
            
            image[y][x] = monster["colour"]
                
    #Kanonenkugel zeichen
    for kugel in kugel_liste:#kugel_liste ist anfangs ebenfalls leer
        
        image[kugel["k2"]][kugel["k1"]] = farbe_kugel
    
    Pyghthouse.set_image(conn, image)
    
    for y in range(14):
        for x in range(28):
            color = image[y][x]
            screen.draw.filled_rect(Rect(x*20, y*50, 20, 30), color)
 
def draw_game_over():
    

    image = Pyghthouse.empty_image()

    if visible:
        for (x,y) in game_over:
            image[y][x] = farbe_game_over

    Pyghthouse.set_image(conn, image)

    for y in range(14):
        for x in range(28):
            color = image[y][x]
            screen.draw.filled_rect(Rect(x*20, y*50, 20, 30), color)

def draw_score():
     
     global score, zahlen
     
     image = Pyghthouse.empty_image()
     
     score_str = str(score)# Damit wir auf beide Ziffern der Zahl zugreifen können/ iterieren können
     
     #Startposition Score
     score_x = 10
     score_y = 4
     
     for index, digit in enumerate(score_str): # Hier durchläuft die Schleife sowohl die Anzahl der Ziffern , als auch 
                                                # die wirkliche Zahlen z.B 3 und 4 bei 34, enumerate gibt also die Position und die Ziffer selbst zurück
         for (sx, sy) in zahlen[digit]:         #enumerate liefert Tupel mit zwei Werten (index, digit) = (0, "3"), (1, "4")
             
            x = score_x + sx + index * 4
            y = score_y + sy
            
            
            image[y][x] = (255,255,255)
     
     Pyghthouse.set_image(conn, image)
     
     for y in range(14):
         
        for x in range(28):
            color = image[y][x]
            screen.draw.filled_rect(Rect(x*20, y*50, 20, 30), color)
 # Zeichne Bildschirm (wird ca. 60-mal pro Sekunde aufgerufen) der drei Zustände
def draw():

    if state == STATE_START:
        draw_start()
    
    elif state == STATE_GAME:
        draw_game()
        
    elif state == STATE_GAME_OVER:
        draw_game_over()
        
    elif state == STATE_SCORE:
        draw_score()


def update_start():
    
    global x_pos, y_pos, dx, dy, frame_counter, speed_divider 
    
    
    frame_counter += 1
    if frame_counter % speed_divider == 0: #speed_divider = 6
        x_pos += dx
        y_pos += dy

        #Rechte Wand
        if x_pos + 3 >= 27:
            dx *= -1

        # Linke Wand
        if x_pos - 1 <= 0:
            dx *= -1

        # Untere Wand
        if y_pos + 3 >= 13:
            dy *= -1

        # Obere Wand
        if y_pos <= 0:
            dy *= -1
        
        

def update_game():
    global spawn_clock, monsters, colour_list, frame_counter2, speed_divider2, Kx_pos, frame_counter3, speed_divider3, kugel_liste, frame_counter4, speed_divider4, state, STATE_GAME, score, fall_speed 
    
    
    #Liste mit zufällig erstellten Monstern erzeugen
    frame_counter2 += 1 
    spawn_clock += 1
    
    if spawn_clock == 120:
        spawn_clock = 0
        
        add_monster = {
            "x" : random.randint(1,25),
            "y" : 0,
            "number" : random.choice(monster_list),
            "colour" : random.choice(colour_list)
            
        }
        
        monsters.append(add_monster)
        
        
    
    frame_counter3 += 1
    
    
    # Bewegt Spielfigur nach links, falls Taste <- gerade gedrückt ist
    if keyboard[keys.LEFT]:
        if frame_counter3 % speed_divider3 == 0:#speed_devider3 = 3
            if Kx_pos > 1:
                Kx_pos -= 1
    # Bewegt Spielfigur nach rechts, falls Taste -> gerade gedrückt ist
    elif keyboard[keys.RIGHT]:
        if frame_counter3 % speed_divider3 == 0:
            if Kx_pos < 26:
                Kx_pos += 1
    
    #Kugel am Ende des Spielfeldes verschwinden lassen
    frame_counter4 += 1
    
    if frame_counter4 % speed_divider4 == 0:#speed_divider4 = 4
    
        for kugel in kugel_liste[:]:   
            kugel["k2"] -= 1
            if kugel["k2"] <= 0:
                kugel_liste.remove(kugel)
    
    kollisions_test()
    
    
    if frame_counter2 % speed_divider2 == 0: #speed_divider2 = 30
        for monster in monsters[:]:
            monster["y"] += 1
            if monster["y"] >= 13:
                monsters.remove(monster)
                state = STATE_GAME_OVER
    
       
    kollisions_test() 
    
    if 10 <= score < 20 :
        speed_divider2 = 25

    if 20 <= score < 30:
        speed_divider2 = 15
        

    if 30 <= score < 40:
        speed_divider2 = 10
        speed_divider3 = 4

    if 40 <= score < 50:
        speed_divider2 = 8
        speed_divider3 = 3

    if 50 <= score < 60:
        speed_divider2 = 6
        speed_divider3 = 3

    if 60 <= score < 70:
        speed_divider2 = 4
        speed_divider3 = 2
        
    if 70 <= score:
        speed_divider2 = 3
        speed_divider3 = 2
    
    
def update_game_over():
    
    global blink_counter, visible

    blink_counter += 1

    if blink_counter % blink_speed == 0:
        visible = not visible
        

def reset_game():
    
    global monsters, kugel_liste, spawn_clock, score, frame_counter2, frame_counter3, frame_counter4, Kx_pos, Ky_pos, blink_counter, visible, state, speed_divider2, speed_divider3
    

    monsters = []
    kugel_liste = []
    spawn_clock = 0
    score = 0
    
    speed_divider2 = 30
    speed_divider3 = 5

    frame_counter2 = 0
    frame_counter3 = 0
    frame_counter4 = 0

    Kx_pos = 14
    Ky_pos = 12

    blink_counter = 0
    visible = True

    state = STATE_START


def update():  
    
    if state == STATE_START:
        update_start()
        
    elif state == STATE_GAME:
        update_game()
        
    elif state == STATE_GAME_OVER:
        update_game_over()
    

        
        
def on_key_down(key):
    global state, kugel_x, kugel_y
    
    if key == keys.ESCAPE:
        Pyghthouse.close(conn)
        exit()
    
    if state == STATE_START:
        if key == keys.SPACE:
            state = STATE_GAME
     
    elif state == STATE_GAME:
        if key == keys.SPACE:
            
            add_kugel = { "k1" : Kx_pos, "k2" : Ky_pos -1}
            
            kugel_liste.append(add_kugel)
    
    if state == STATE_GAME_OVER:
        if key == keys.SPACE:
            state = STATE_SCORE
    
    
    elif state == STATE_SCORE:
        if key == keys.SPACE:
            reset_game()
            state = STATE_START
            
    
            
            
                        
            
            
            
            
        
    
    
    
        
        


pgzrun.go()
    