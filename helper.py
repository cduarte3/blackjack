import pygame
import random

font_name = '8-BIT WONDER.TTF'

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

def draw_text(text, size, x, y, display, colour):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, colour)
    text_rect = text_surface.get_rect()
    text_rect.center = (x,y)
    display.blit(text_surface, text_rect)


def hit_card(user_hand, card_deck):
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
        user_hand += int(random_card)
    elif random_card in ['J', 'Q', 'K']:
        user_hand += 10
    elif random_card == 'A':
        if user_hand + 11 > 21:
            user_hand += 1
        else:
            user_hand += 11
    return card_name, user_hand