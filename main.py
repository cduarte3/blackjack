#from game import Game
import pygame
from button import *
from helper import *
from pygame import mixer
#g = Game()
pygame.init()
mixer.init()

song1 =  'audio/casino.mp3'
song2 = 'audio/casino 2.mp3'
songs = [song1, song2]
current_song = random.choice(songs)
mixer.music.set_volume(0.5)
mixer.music.load(current_song)
mixer.music.play(-1)

def song_change():
    global current_song
    mixer.music.stop()
    if current_song == song1:
        current_song = song2
    elif current_song == song2:
        current_song = song1
    mixer.music.load(current_song)
    mixer.music.play(-1)

def change_volume():
    if mixer.music.get_volume() == 0.5:
        mixer.music.set_volume(0)
    elif mixer.music.get_volume() == 0:
        mixer.music.set_volume(0.5)

SCREEN_W, SCREEN_H = 400, 630
screen = pygame.display.set_mode(((SCREEN_W, SCREEN_H)))
pygame.display.set_caption('Blackjack')
BLACK, WHITE, GREEN = (0,0,0), (255,255,255), (0, 100, 50)

cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
card_deck = 4 * cards
card_name = ''
dealer_card_name = ''
end_img = pygame.image.load('images/x.png').convert_alpha()
end_button = Button(SCREEN_W - 45, 8, end_img, 0.12)
song_image = pygame.image.load('images/song.png').convert_alpha()
song_button = Button(SCREEN_W - 140, 10, song_image, 0.15)
volume_img = pygame.image.load('images/volume.png').convert_alpha()
volume_button = Button(SCREEN_W - 90, 10, volume_img, 0.06)
mute_img = pygame.image.load('images/mute.png').convert_alpha()
mute_button = Button(SCREEN_W - 90, 10, mute_img, 0.06)
stand_img = pygame.image.load('images/stand.png').convert_alpha()
hit_img = pygame.image.load('images/hit.png').convert_alpha()
hit_button = Button(40, SCREEN_H - 80, hit_img, 0.4)
stand_button = Button(150,SCREEN_H - 80, stand_img, 0.4)
dealer_img = pygame.image.load('images/Dealer.png').convert_alpha()
dealer_button = Button(300, SCREEN_H - 500, dealer_img, 3)
machine_img = pygame.image.load('images/Card_Machine.png').convert_alpha()
machine_button = Button(280, SCREEN_H - 125, machine_img, 1.5)
stand = False
dealer_goes = False
again = False
quit = False
game_over = False
win = False
lose = False
draw = False
stand_click = True

class User():
    def __init__(self):
        self.user_hand = 0
        self.dealer_hand = 0
        self.card1_button, self.card2_button, self.dealer_card1_button, self.dealer_card2_button = None, None, None, None
        self.win_count = 0
        self.lose_count = 0
        self.draw_count = 0
        self.setup()

    def reset(self):
        self.user_hand = 0
        self.dealer_hand = 0
        self.card1_button, self.card2_button, self.dealer_card1_button, self.dealer_card2_button = None, None, None, None
        self.setup()

    def setup(self):
        temp_hand = 0
        temp_dealer_hand = 0
        
        user_hand_1, temp_hand = hit_card(temp_hand, card_deck)
        card1_img = pygame.image.load('images/cards/' + user_hand_1).convert_alpha()
        self.card1_button = Button(25, SCREEN_H - 230, card1_img, 1)
        
        user_hand_2, temp_hand = hit_card(temp_hand, card_deck)
        card2_img = pygame.image.load('images/cards/' + user_hand_2).convert_alpha()
        self.card2_button = Button(100, SCREEN_H - 230, card2_img, 1)

        # set the user hand after hitting twice to start the game
        self.user_hand = temp_hand

        dealer_hand_1, temp_dealer_hand = hit_card(temp_dealer_hand, card_deck)
        dealer_card1_img = pygame.image.load('images/cards/' + dealer_hand_1).convert_alpha()
        self.dealer_card1_button = Button(25, SCREEN_H - 475, dealer_card1_img, 1)

        dealer_hand_2, temp_dealer_hand = hit_card(temp_dealer_hand, card_deck)
        dealer_card2_img = pygame.image.load('images/cards/' + dealer_hand_2).convert_alpha()
        self.dealer_card2_button = Button(100, SCREEN_H - 475, dealer_card2_img, 1)

        # set the dealer hand after hitting twice to start the game
        self.dealer_hand = temp_dealer_hand
   
u = User()
run = True
while run:
    #g.curr_menu.display_menu()
    #g.game_loop()
    screen.fill(GREEN)
    draw_text('Blackjack', 20, 110, SCREEN_H/2 - 250, screen, WHITE)
    draw_text('W' + str(u.win_count) + ' D' + str(u.draw_count) + ' L' + str(u.lose_count), 20, 300, SCREEN_H/2 - 250, screen, WHITE)
    if stand_click == True:
        if stand_button.draw(screen):
            stand = True
            dealer_goes = True
            stand_click = False
    elif stand_click == False:
        stand_button.draw(screen)
    if stand == False:
        if hit_button.draw(screen):
            temp_hand = 0
            card_name, temp_hand = hit_card(u.user_hand, card_deck)
            u.user_hand = temp_hand
            if (u.user_hand > 21):
                game_over = True
                lose = True
                u.lose_count += 1
                stand = True
                stand_click = False
    if dealer_goes == True:
        temp_dealer_hand = 0
        while (u.dealer_hand < 17):
            dealer_card_name, temp_dealer_hand = hit_card(u.dealer_hand, card_deck)
            u.dealer_hand = temp_dealer_hand
        if (u.dealer_hand > 21):
            win = True
            u.win_count += 1
        elif (u.dealer_hand > u.user_hand):
            lose = True
            u.lose_count += 1
        elif (u.dealer_hand < u.user_hand):
            win = True
            u.win_count += 1
        elif (u.dealer_hand == u.user_hand):
            draw = True
            u.draw_count += 1
        game_over = True
        dealer_goes = False
    if(card_name != ''):
        # display the card on screen
        card_img = pygame.image.load('images/cards/' + card_name).convert_alpha()
        card_button = Button(175, SCREEN_H - 230, card_img, 1)
        card_button.draw(screen)
    if(dealer_card_name != ''):
        # display the card on screen
        dealer_card_img = pygame.image.load('images/cards/' + dealer_card_name).convert_alpha()
        dealer_card_button = Button(175, SCREEN_H - 475, dealer_card_img, 1)
        dealer_card_button.draw(screen)
    if game_over == True:
        draw_text('Game Over', 20, SCREEN_W/2, SCREEN_H/2, screen, WHITE)
        if lose == True:
            draw_text('You Lose', 20, SCREEN_W/2, SCREEN_H/2 + 30, screen, WHITE)
        elif win == True:
            draw_text('You Win', 20, SCREEN_W/2, SCREEN_H/2 + 30, screen, WHITE)
        elif draw == True:
            draw_text('Draw', 20, SCREEN_W/2, SCREEN_H/2 + 30, screen, WHITE)
        if machine_button.draw(screen):
            u.reset()
            game_over = False
            stand = False
            dealer_goes = False
            win = False
            lose = False
            draw = False
            stand_click = True
            card_name = ''
            dealer_card_name = ''
    if mixer.music.get_volume() == 0.5:
        if volume_button.draw(screen):
            change_volume()
    elif mixer.music.get_volume() == 0:
        if mute_button.draw(screen):
            change_volume()
    if song_button.draw(screen):
        song_change()
    if end_button.draw(screen):
        run = False
    dealer_button.draw(screen)
    u.card1_button.draw(screen)
    u.card2_button.draw(screen)
    u.dealer_card1_button.draw(screen)
    u.dealer_card2_button.draw(screen)
    draw_text('Dealer Has ' + str(u.dealer_hand), 20, SCREEN_W/2, SCREEN_H/2 - 200, screen, WHITE)
    draw_text('You Have ' + str(u.user_hand), 20, 135, SCREEN_H - 110, screen, WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()