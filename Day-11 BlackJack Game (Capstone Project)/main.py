# ====== Blackjack Cards Game ====== #

# == Our Blackjack House Rules == #

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.
# Whoever have higher score he will win, though there is a limit of higher score and it's 21.
# If a persons score is 21 it means it's a Blackjack and no need to draw cards further, or he will lose.
# If Dealer(computer) gets a Blackjack you will lose even if you have Blackjack too.
# If score exceeds 21 it will be considered lose.
# If Dealers(computers) score is 16 or less he must have to draw another card.
# If a person has Ace(i.e. value 11) in his cards and his score exceeds 21 then Ace's value will shrink down to 1 so
# this is the special power of Ace and that way you won't lose.

import random
import os
from art import logo


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def deal_card():
    '''Returns a random card from the deck.'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a Draw"
    elif computer_score == 21:
        return "You lose. Opponent has Blackjack"
    elif user_score == 21:
        return "You win. It's a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    else:
        if user_score > computer_score:
            return "You win"
        else:
            return "You lose"


def play():
    cls()
    print(logo)
    user_cards = []
    computer_cards = []
    user_play = False
    computer_play = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"    Your cards: {user_cards}, current score: {user_score}")
    print(f"    Computer's first card: {computer_cards[0]}")

    if user_score == 21 or computer_score == 21 or user_score > 21:
        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's final hand: {computer_cards} final score: {computer_score}")
        print(compare(user_score, computer_score))
        user_play = True
        computer_play = True

    while not user_play:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if another_card == 'y':
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
            if user_score > 21:
                print(f"Your final hand: {user_cards}, final score: {user_score}")
                print(f"Computer's final hand: {computer_cards} final score: {computer_score}")
                print(compare(user_score, computer_score))
                computer_play = True
                user_play = True
            else:
                print(f"Your cards: {user_cards}, current score: {user_score}")
                print(f"Computer's first card: {computer_cards[0]}")

        else:
            user_play = True

    while not computer_play:
        if computer_score < 17 and computer_score != 21:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)
            if computer_score > 16:
                print(f"Your final hand: {user_cards}, final score: {user_score}")
                print(f"Computer's final hand: {computer_cards} final score: {computer_score}")
                print(compare(user_score, computer_score))
                computer_play = True
        else:
            print(compare(user_score, computer_score))


play_again = True
while play_again:
    and_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if and_again == 'y':
        play()
    else:
        play_again = False
