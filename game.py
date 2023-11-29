import pygame
import random
from menu import *
from button import *

cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
twos = ['2.1.png', '2.2.png', '2.3.png', '2.4.png', '2.5.png', '2.6.png', '2.7.png', '2.8.png']
threes = ['3.1.png', '3.2.png', '3.3.png', '3.4.png', '3.5.png', '3.6.png', '3.7.png', '3.8.png']
fours = ['4.1.png', '4.2.png', '4.3.png', '4.4.png', '4.5.png', '4.6.png', '4.7.png', '4.8.png']
fives = ['5.1.png', '5.2.png', '5.3.png', '5.4.png', '5.5.png', '5.6.png', '5.7.png', '5.8.png']
sixes = ['6.1.png', '6.2.png', '6.3.png', '6.4.png', '6.5.png', '6.6.png', '6.7.png', '6.8.png']
sevens = ['7.1.png', '7.2.png', '7.3.png', '7.4.png', '7.5.png', '7.6.png', '7.7.png', '7.8.png']
eights = ['8.1.png', '8.2.png', '8.3.png', '8.4.png', '8.5.png', '8.6.png', '8.7.png', '8.8.png']
nines = ['9.1.png', '9.2.png', '9.3.png', '9.4.png', '9.5.png', '9.6.png', '9.7.png', '9.8.png']
tens = ['10.1.png', '10.2.png', '10.3.png', '10.4.png', '10.5.png', '10.6.png', '10.7.png', '10.8.png']
jacks = ['J1.png', 'J2.png', 'J3.png', 'J4.png', 'J5.png', 'J6.png', 'J7.png', 'J8.png']
queens = ['Q1.png', 'Q2.png', 'Q3.png', 'Q4.png', 'Q5.png', 'Q6.png', 'Q7.png', 'Q8.png']
kings = ['K1.png', 'K2.png', 'K3.png', 'K4.png', 'K5.png', 'K6.png', 'K7.png', 'K8.png']
aces = ['A.1.png', 'A.2.png', 'A.3.png', 'A.4.png', 'A.5.png', 'A.6.png', 'A.7.png', 'A.8.png']
card_deck = 4 * cards
card_name = ''
fps = 60
timer = pygame.time.Clock()

class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 400, 600
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        pygame.display.set_caption('Blackjack')
        self.font_name = '8-BIT WONDER.TTF'
        self.BLACK, self.WHITE, self.GREEN = (0,0,0), (255,255,255), (0, 100, 50)
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu
        self.stand_img = pygame.image.load('images/stand.png').convert_alpha()
        self.hit_img = pygame.image.load('images/hit.png').convert_alpha()
        self.hit_button = Button(40, self.DISPLAY_H - 80, self.hit_img, 0.4)
        self.stand_button = Button(150,self.DISPLAY_H - 80, self.stand_img, 0.4)
        self.user_hand = 0
        self.dealer_hand = 0
        self.dealer_img = pygame.image.load('images/Dealer.png').convert_alpha()
        self.dealer_button = Button(300, self.DISPLAY_H - 500, self.dealer_img, 3)
        self.machine_img = pygame.image.load('images/Card_Machine.png').convert_alpha()
        self.machine_button = Button(300, self.DISPLAY_H - 100, self.machine_img, 1)
        self.stand = False
        self.again = False
        self.quit = False

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False
            self.draw_game()
            pygame.display.update()
            self.reset_keys()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface, text_rect)

    def draw_game(self):
        self.display.fill(self.GREEN)
        self.draw_text('Blackjack', 20, self.DISPLAY_W/2, self.DISPLAY_H/2 - 250)
        if self.stand_button.draw(self.display):
            self.stand = True
        if self.stand == False:
            if self.hit_button.draw(self.display):
                card_name = self.hit_card()
                # display the card on screen
                card_img = pygame.image.load('images/cards/' + card_name).convert_alpha()
                card_button = Button(100, self.DISPLAY_H - 300, card_img, 2)
                card_button.draw(self.display)
        self.dealer_button.draw(self.display)
        self.machine_button.draw(self.display)
        self.draw_text('Dealer Has ' + str(self.dealer_hand), 20, self.DISPLAY_W/2, self.DISPLAY_H/2 - 200)
        self.draw_text('You Have ' + str(self.user_hand), 20, 135, self.DISPLAY_H - 110)
        self.window.blit(self.display, (0,0))

    def hit_card(self):
        # call upon a random card from the deck
        random_card = random.choice(card_deck)

        # give a card a name to display the card with a random suit
        if random_card == '2':
            card_name = random.choice(twos)
        elif random_card == '3':
            card_name = random.choice(threes)
        elif random_card == '4':
            card_name = random.choice(fours)
        elif random_card == '5':
            card_name = random.choice(fives)
        elif random_card == '6':
            card_name = random.choice(sixes)
        elif random_card == '7':
            card_name = random.choice(sevens)
        elif random_card == '8':
            card_name = random.choice(eights)
        elif random_card == '9':
            card_name = random.choice(nines)
        elif random_card == '10':
            card_name = random.choice(tens)
        elif random_card == 'J':
            card_name = random.choice(jacks)
        elif random_card == 'Q':
            card_name = random.choice(queens)
        elif random_card == 'K':
            card_name = random.choice(kings)
        elif random_card == 'A':
            card_name = random.choice(aces)

        # add the card to the user's hand
        if random_card in ['2','3','4','5','6','7','8','9','10']:
            self.user_hand += int(random_card)
        elif random_card in ['J', 'Q', 'K']:
            self.user_hand += 10
        elif random_card == 'A':
            if self.user_hand + 11 > 21:
                self.user_hand += 1
            else:
                self.user_hand += 11
        return card_name