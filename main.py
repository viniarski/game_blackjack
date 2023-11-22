import random
from replit import clear
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_score = 0
dealer_score = 0

def blackjack():

    player_cards = random.sample(cards, 2)
    dealer_cards = random.sample(cards, 2)

    print(f"Your cards: {player_cards} \
          Your score: {sum(player_cards)}")
    print(f"Dealer first card: [{dealer_cards[0]}]")

    active = True
    while active:
        player_score = sum(player_cards)
        dealer_score = sum(dealer_cards)

        while dealer_score < 17:
            dealer_next_card = random.choice(cards)
            dealer_cards.append(dealer_next_card)
            dealer_score += dealer_next_card

        more_cards = True
        while more_cards:
            if player_score > 21 and 11 in player_cards:
                player_cards.remove(11)
                player_cards.append(1)
            elif player_score == 21 or player_score > 21 and 11 not in player_cards:
                break
            another_card = input("Would you like another card: 'y' or 'n'? ")
            if another_card == 'n':
                more_cards = False
            else:
                player_next_card = random.choice(cards)
                if player_next_card == 11:
                    player_cards.append(player_next_card)
                    player_score = sum(player_cards)
                    if player_score > 21:
                        player_cards.remove(11)
                        player_score -= 10
                        player_next_card = 1
                    elif player_score == 21:
                        more_cards = False
                elif player_next_card != 11 and 11 in player_cards and player_score + player_next_card > 21:
                    player_cards.remove(11)
                    player_cards.append(1)

                player_cards.append(player_next_card)
                player_score = sum(player_cards)
                print(f"Your next card is {player_next_card}. \
                      Your cards:{player_cards} \
                      Your score: {player_score}.")

        print(f"Dealer cards: {dealer_cards}. \
              Dealer score: {dealer_score}.")

        if player_score > 21:
            print("You went over. You lose!")
        elif player_score > dealer_score and player_score < 21:
            print("You won!")
        elif player_score < dealer_score and dealer_score <= 21:
            print("You lose!")
        elif player_score < 21 and dealer_score > 21:
            print("You won!")
        elif player_score > dealer_score and player_score == 21:
            print("You won with a Blackjack on hand!")
        elif player_score < dealer_score and player_score == 21:
            print("You won with a Blackjack on hand!")
        elif player_score == dealer_score:
            print("It's a draw.")

        active = False

        again = input("Would you like to play again? 'y' or 'n'")
        if again == 'y':
            clear()
            blackjack()
        else:
            print("Goodbye!")

print(logo)
play = input("\nWould you like to play Blackjack? 'y' or n': ")

if play == 'y':
    blackjack()
else:
    print("Goodbye!")