import random
import art


def game():
    def add_player_card():
        player_cards.append(cards[random.randint(0, len(cards) - 1)])

    def add_computer_card():
        computer_cards.append(cards[random.randint(0, len(cards) - 1)])

    def sum_player_cards():
        return sum(player_cards)

    def sum_computer_cards():
        return sum(computer_cards)

    def final_score():
        print(f"    Your final hand: {player_cards}, final score: {sum_player_cards()}")
        print(f"    Computer's final hand: {computer_cards}, final score: {sum_computer_cards()}")

    def current_score():
        print(f"    Your cards: {player_cards}, current score: {sum_player_cards()}")
        print(f"    Computer's first card: {computer_cards[0]}")

    def another_game():
        want_another = input("Do you want play another game? Type 'y' or 'n': ")
        if want_another == "y":
            print("\n" * 40)
            game()
        elif want_another == "n":
            return 0

    def compare(player_sum, computer_sum):
        if player_sum > computer_sum:
            final_score()
            print("You have more than computer, you win!")
            another_game()
        elif player_sum < computer_sum:
            final_score()
            print("You have less than computer, you lose")
            another_game()
        else:
            final_score()
            print("You have the same score as computer, draw")
            another_game()

    print(art.logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    game_continue = True

    player_cards = []
    computer_cards = []
    add_player_card()
    add_player_card()
    add_computer_card()
    add_computer_card()

    print(f"    Your cards: {player_cards}, current score: {sum_player_cards()}")
    print(f"    Computer's first card: {computer_cards[0]}")

    while game_continue:
        if sum_player_cards() == 21:
            final_score()
            print("Win, you have Blackjack")
            another_game()
        elif sum_computer_cards() == 21:
            final_score()
            print("Lose, opponent has Blackjack")
            another_game()

        if sum_player_cards() > 21:
            for number in player_cards:
                if number == 11:
                    if sum_player_cards() - 10 > 21:
                        final_score()
                        print("Lose, you have over 21")
                        another_game()
                    else:
                        answer = input("Do you want another card? Type 'y' or 'n': ")
                        if answer == "y":
                            add_player_card()
                            current_score()
                        elif answer == "n":
                            game_continue = False
                else:
                    final_score()
                    print("Lose, you have over 21")
                    another_game()
        else:
            answer = input("Do you want another card? Type 'y' or 'n': ")
            if answer == "y":
                add_player_card()
                current_score()
            elif answer == "n":
                game_continue = False
                while sum_computer_cards() < 17:
                    add_computer_card()
                if sum_computer_cards() > 21:
                    final_score()
                    print("Computer have over 21, you win!")
                    another_game()
                else:
                    compare(player_sum=sum_player_cards(), computer_sum=sum_computer_cards())


game()
