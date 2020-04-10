import card_deck
import bank_roll
import time


def loading_delay():
    for num in range(10):
        print("*****", end='')
        time.sleep(0.25)
    print("\n")


player1_bank = bank_roll.BankRoll(100)
computer_bank = bank_roll.BankRoll(10)
play_again = "y"
while (play_again.lower() == "y"):
    winner = None
    player1_card = card_deck.Card()
    computer_card = card_deck.Card()
    if player1_bank.balance() == 0:
        print("\nPlayer1 has no balance")
        print("The computer has own")
        break
    if computer_bank.balance() == 0:
        print("\nComputer has no balance")
        print("Player1 WON!!!!!!")
        print("Please start a new round")
        break
    my_bet = input("How much would you like to bet:")
    print("Player 1 balance...............")
    if (int(my_bet) > player1_bank.balance()):
        player1_bank.bet(int(my_bet))
        print("\n")
        continue
    else:
        player1_bank.bet(int(my_bet))
        print("\n")
        loading_delay()
        print('Computer balance...............')
    if (int(my_bet) > computer_bank.balance()):
        print(f"\ncomputer balance is {computer_bank.balance()}")
        print("Please bet less or start a new round!!!!")
        print("\nPlayer 1 balance...............")
        player1_bank.win(int(my_bet))
        continue
    else:
        computer_bank.bet(int(my_bet))
    print('\n')
    print("Shuffling the deck please wait!!!!")
    loading_delay()
    computer_card.suffle()
    print('\n')
    computer_card.pull_card(2)
    print(f"Computer's Hand ({len(computer_card.player_hand)} cards)...........")
    print(f"{computer_card.player_hand[1]}, Hidden Card!!!")
    print("\nPlayer1's turn................")
    player1_card.pull_card(1)
    print(f"Player1's Hand ({len(player1_card.player_hand)} cards)...........")
    print(f"{player1_card.player_hand}")
    while player1_card.total_value() <= 21:
        my_choice = input("Press 'h' if you want to hit or press 's' if you want to stay: ")
        if (my_choice.lower() != 'h') and (my_choice.lower() != 's'):
            print("Invalid entry!!!! Please try again")
            continue
        while my_choice == 'h' or my_choice == 'H':
            player1_card.pull_card(1)
            print(f"Player1's Hand ({len(player1_card.player_hand)} cards)...........")
            print(f"{player1_card.player_hand}")
            break
        while (my_choice.lower() == 's'):
            loading_delay()
            print(f"Computer's Hand ({len(computer_card.player_hand)} cards)...........")
            print(computer_card.player_hand)
            while computer_card.total_value() < 17:
                print('Computer is hitting........')
                loading_delay()
                computer_card.pull_card(1)
                print(f"Computer's Hand ({len(computer_card.player_hand)} cards)...........")
                print(computer_card.player_hand)
                if computer_card.total_value() > 21:
                    loading_delay()
                    print(f"Computer's Hand ({len(computer_card.player_hand)} cards)...........")
                    print(computer_card.player_hand)
                    print('Computer is BUST!!!!')
                    print('Player1 WINS!!!')
                    print('Player1 balance...............')
                    player1_bank.win(int(my_bet) * 2)
                    winner = 'Player1'
                    break
                else:
                    continue
            if computer_card.total_value() > 21:
                break
            elif computer_card.total_value() < player1_card.total_value():
                loading_delay()
                print("Player 1 wins!!!!!!!!")
                player1_bank.win(int(my_bet) * 2)
                winner = 'Player1'
                break
            elif computer_card.total_value() > player1_card.total_value():
                loading_delay()
                print("Player 1 lose!!!!!!!!")
                print(f"Player 1 lost {my_bet} Euros\n")
                print('Computer balance...............')
                computer_bank.win(int(my_bet) * 2)
                winner = 'Computer'
                print('\n')
                break
            else:
                print("It's a TIE!!!!")
                player1_bank.win(int(my_bet))
                computer_bank.win(int(my_bet))
                winner = 'Tie'
                break
        if ((winner == 'Player1') or (winner == 'Computer') or (winner == 'Tie')):
            break
    if player1_card.total_value() > 21:
        loading_delay()
        print(f"Player 1 is BUST!!!!!!!! and lost {my_bet} Euros\n")
        print('Computer balance...............')
        computer_bank.win(int(my_bet) * 2)
    play_again = input("Play again?,Press 'y' for YES or any other key for NO: ")
