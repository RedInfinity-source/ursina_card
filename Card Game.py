# this is a ursina card game, the objective is to lower the other players' health as soon as possible

# imports
import random
from ursina import *

# time limit
min = 0
# play game
game = True
# click
click = False
# update
def update():
    global time,min,game,play_1,play_2,hp,hp_2,deck,deck_2,finder,hit_amount,click
    timer.background = True
    # death
    if hp <= 0 or hp_2 <= 0:
        click = True
        game = False
        # menu
        if hp > hp_2:
            timer.text = 'Player 1 has won'.format(time)
        elif hp_2 > hp:
            timer.text = 'Player 2 has won'.format(time)
        else:
            timer.text = 'Tye'.format(time)
    # click
    if click == True:
        exit_game.color = color.red
        exit_game.text = 'Exit Game'

    # not dead
    if game == True:
        # player 1
        if play_1 == True:
            # hit animation
            hit_box_2.animate_color((255, 0, 0, 255), duration=2)
            hit_box_2.animate_color((0, 0, 0, 0), duration=1)
            # deck script
            if deck > 0:
                deck -= 1
                card = Card(finder,attack = random.randint(1,9))
                hand.append(card)
            # text display update
            deck_size.text = 'Deck: {}'.format(deck)
            # fight
            hp_2 -= hit_amount
            # player 2 health update
            health_2.text = 'Player Health {}'.format(round(hp_2))
            play_1 = False
        # player 2
        if play_2 == True:
            # hit animation
            hit_box.animate_color((255, 0, 0, 255), duration=2)
            hit_box.animate_color((0, 0, 0, 0), duration=1)
            # deck script
            if deck_2 > 0:
                deck_2 -= 1
                card = Card(finder,attack = random.randint(1,9))
                card.y = 0.38
                # update hand list
                hand_2.append(card)
            # text display update
            deck_size_2.text = 'Deck: {}'.format(deck_2)
            # update finder
            hp -= hit_amount
            # player 1 health update
            health.text = 'Player Health {}'.format(round(hp))
            play_2 = False

        # time
        min += 1
        if min >= 60:
            min = 0
            time -= 1
        elif time < 1:
            timer.text = 'Timer has ran out'.format(time)
            game = False
            # menu
            click = True
        else:
            timer.text = 'Timer: {}'.format(time)
    # general updates
    finder = 0
    hit_amount = 0

app = Ursina()
# make the cards
class Card(Button):
    def __init__(self, x,attack):
        super().__init__()
        self.parent = camera.ui
        self.model = 'quad'
        self.texture = 'white_cube'
        self.scale = 0.2
        self.highlight_color = color.gray
        self.x = x
        self.y = -0.38
        self.attack = attack
        R, G, B = 0, 0, 0
        chance = random.randint(1, 3)
        if chance == 1:
            R = 255
            G = 0
            B = 0
        if chance == 2:
            R = 0
            G = 255
            B = 0
        if chance == 3:
            R = 0
            G = 0
            B = 255
        self.color = color.rgb(R,G,B)
        self.text = 'Attack: {}'.format(attack)
        self.text_color = color.black
        self.text_origin = (-0.4, -0.4)

    # what card is in play and how it should react
    def input(self, key):
        global game, play_1,play_2,finder,hit_amount
        if self.hovered:
            # which side is playing
            if key == 'left mouse down':
                if game == True:
                    # check mouse position
                    if mouse.y < -0.28:
                        play_1 = True
                        finder = self.x
                        # animation
                        self.animate_position((self.x,1,0),duration = 1)
                        self.animate_rotation((0,0,-90),duration = 0.9)
                        self.fade_out(0,duration = 0.89)
                        hit_amount = self.attack
                        # remove card
                        destroy(self,delay = 2)
                    elif mouse.y > 0.28:
                        play_2 = True
                        finder = self.x
                        # animation
                        self.animate_position((self.x,-1,0),duration = 1)
                        self.animate_rotation((0,0,90),duration = 0.9)
                        self.fade_out(0,duration = 0.89)
                        hit_amount = self.attack
                        # remove card
                        destroy(self,delay = 2)
# Exit
def exit():
    global game,click
    if click == True:
        game = False
        exit()

exit_game = Button(parent = camera.ui,color = color.clear,scale = 0.2,y = -0.15,text = '')
exit_game.on_click = exit
# timer
line = Entity(model = 'line',scale = 16)
time = 60
timer = Text(parent = camera.ui,text = 'Timer: {}'.format(time),size = 0.04,origin = (0,0),color = color.gold,background = True)

# card information
finder = 0 # this will be used to replace the old card
hit_amount = 0

# player
play_1 = False # if they are playing a card
hp = 100
deck = 50
# display on screen
health = Text(text = 'Player Health {}'.format(hp),y = -0.3,color = color.white,x = -0.86)
deck_size = Text(text = 'Deck: {}'.format(deck),y = -0.35,color = color.white,x = -0.86)
hit_box = Entity(parent = camera.ui,model = 'quad',scale = (16,0.26),y = -0.37,color = color.clear)

# player 1 hand
hand = []
x = -0.5
for y in range(6):
    # deck size
    deck -= 1
    # making the hand
    card = Card(x,attack = random.randint(1,10))
    x += 0.25
    # hand
    hand.append(card)

# computer ----------------------------------------------------------------------------------------------------------
# player 2
play_2 = False
hp_2 = 100
deck_2 = 50
# display on screen
health_2 = Text(text = 'Player Health {}'.format(hp_2),y = 0.3,color = color.white,x = -0.86)
deck_size_2 = Text(text = 'Deck: {}'.format(deck_2),y = 0.35,color = color.white,x = -0.86)
hit_box_2 = Entity(parent = camera.ui,model = 'quad',scale = (16,0.26),y = 0.37,color = color.clear)

# player 2 hand
hand_2 = []
x2 = -0.5
for y2 in range(6):
    # deck size
    deck_2 -= 1
    # making the hand
    card = Card(x2,attack = random.randint(1,10))
    card.y = 0.38
    x2 += 0.25
    # hand
    hand_2.append(card)
app.run()
