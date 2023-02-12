import random
from tabulate import tabulate


def calculate_points(player_hand):
    # Define a dictionary to map each rank to its point value
    rank_points = {
        'Ace': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5,
        'Six': 6,
        'Seven': 7,
        'Eight': 8,
        'Nine': 9,
        'Ten': 10,
        'Jack': 10,
        'Queen': 10,
        'King': 10
    }
    # Initialize a variable to keep track of the total points
    total_points = 0
    # Iterate over the player's hand
    for rank, suit in player_hand:
        if (rank == 'King' and suit == 'Spades') or (rank == 'King' and suit == 'Clubs') or (rank == 0 and suit == 0):
            total_points += 0
        else:
            total_points += rank_points[rank]
    # Return the total points
    return total_points


# Displays current round hand details
def display_details():
    player1_hand = player_hands[:4]
    player2_hand = player_hands[4:8]
    player3_hand = player_hands[8:12]
    player4_hand = player_hands[12:16]

    # Displaying using tabulate
    table1 = [['Player 1', player1_hand, calculate_points(player1_hand)],
              ['Player 2', player2_hand, calculate_points(player2_hand)],
              ['Player 3', player3_hand, calculate_points(player3_hand)],
              ['Player 4', player4_hand, calculate_points(player4_hand)]]
    print(tabulate(table1, tablefmt='fancy_grid'))
    # Displaying seen cards
    table2 = [['Player 1 Seen', player1_seen, calculate_points(player1_seen)],
              ['Player 2 Seen', player2_seen, calculate_points(player2_seen)],
              ['Player 3 Seen', player3_seen, calculate_points(player3_seen)],
              ['Player 4 Seen', player4_seen, calculate_points(player4_seen)]]
    print(tabulate(table2, tablefmt='rounded_grid'), end="\n")
    # print(player_hands)


def play_game(i):
    display_details()
    global current_player
    current_player = current_player % 4
    current_player += 1
    if i == (len(draw_deck) - 1):
        random.shuffle(draw_deck)
        i = 0
    print("\n")
    print("Player", current_player, "has to play.")
    while True:
        print("1. Pickup")
        print("2. Declare!")
        ch_0 = int(input("Enter your choice: "))
        print("\n")
        if ch_0 == 1:
            break
        # End game
        elif ch_0 == 2:
            print("Player", current_player, "has declared.")
            player_points = [
                calculate_points(player_hands[:4]),
                calculate_points(player_hands[4:8]),
                calculate_points(player_hands[8:12]),
                calculate_points(player_hands[12:16])
            ]
            # Print player hands
            table1 = [
                ['Player 1', player_hands[:4], player_points[0]],
                ['Player 2', player_hands[4:8], player_points[1]],
                ['Player 3', player_hands[8:12], player_points[2]],
                ['Player 4', player_hands[12:16], player_points[3]]
            ]
            print(tabulate(table1, tablefmt='fancy_grid'))

            # Determine the winning player
            winning_player = player_points.index(min(player_points)) + 1
            # Check if current player is the winning player
            if winning_player != current_player:
                print("Player", current_player, "has LOST.")
            else:
                print("Player", current_player, "has WON.")
            return True
        else:
            print("Invalid choice.")

    player_pickup_hand = draw_deck[i]
    print("Player", current_player, "has picked up", player_pickup_hand)

    # Display the menu options
    while True:
        print("1. Swap and toss a card from your hand")
        print("2. Toss picked up card")
        # Prompt the player to choose an option
        choice = int(input("Enter your choice: "))
        # Swap a card
        if choice == 1:
            while True:
                try:
                    # Get the swap position from user input
                    swap_position = int(input("Enter the swap position of your choice: "))
                    # Check if the swap position is valid
                    if swap_position in range(4 * (current_player - 1), 4 * current_player):
                        break
                    else:
                        # Raise an error if the input is not valid
                        raise ValueError("Invalid input")
                except ValueError as error:
                    # Print the error message and prompt the user to enter a valid input
                    print(error, "Enter a valid swap position: ")
            # Swap the card at the chosen position with the pickup card
            tmp = player_hands[swap_position]
            player_hands[swap_position] = player_pickup_hand

            # Update player seen card
            if current_player == 1:
                player1_seen[swap_position] = player_pickup_hand
            elif current_player == 2:
                player2_seen[swap_position] = player_pickup_hand
            elif current_player == 3:
                player3_seen[swap_position] = player_pickup_hand
            else:
                player4_seen[swap_position] = player_pickup_hand

            # Discard the replaced card to toss_deck pile
            toss_deck.append(tmp)
            # Display the current tossed deck
            print("Current Tossed card is:", tmp)
            print("\n")
            break

        # Throw a card
        elif choice == 2:
            toss_deck.append(player_pickup_hand)
            print("Current Tossed card is:", player_pickup_hand)
            print("\n")
            check_power(player_pickup_hand)
            break

        else:
            print("Invalid choice.")
    i += 1
    play_game(i)


def check_power(played_card):
    global current_player
    if (played_card[0] == 'Seven') or (played_card[0] == 'Eight'):
        # see own
        print("You can see 1 of your own cards.")
        print("Select a card index to see")
        while True:
            try:
                # Get the swap position from user input
                swap_position = int(input("Enter the position of your choice: "))
                # Check if the swap position is valid
                if swap_position in range(4 * (current_player - 1), 4 * current_player):
                    break
                else:
                    # Raise an error if the input is not valid
                    raise ValueError("Invalid input")
            except ValueError as error:
                # Print the error message and prompt the user to enter a valid input
                print(error, "Enter a valid swap position: ")
        if current_player == 1:
            player1_seen[swap_position] = player_hands[swap_position]
        elif current_player == 2:
            player2_seen[swap_position] = player_hands[swap_position]
        elif current_player == 3:
            player3_seen[swap_position] = player_hands[swap_position]
        else:
            player4_seen[swap_position] = player_hands[swap_position]

    elif (played_card[0] == 'Nine') or (played_card[0] == 'Ten'):
        # see someone else's
        print("You can see 1 of your opponents cards.")
        print("Select a card index to see")
        while True:
            try:
                # Get the swap position from user input
                swap_position = int(input("Enter the position of your choice: "))
                # Check if the swap position is valid
                if swap_position not in range(4 * (current_player - 1), 4 * current_player) and swap_position in range(
                        0, 16):
                    break
                else:
                    # Raise an error if the input is not valid
                    raise ValueError("Invalid input")
            except ValueError as error:
                # Print the error message and prompt the user to enter a valid input
                print(error, "Enter a valid swap position: ")
        if current_player == 1:
            player1_seen[swap_position] = player_hands[swap_position]
        elif current_player == 2:
            player2_seen[swap_position] = player_hands[swap_position]
        elif current_player == 3:
            player3_seen[swap_position] = player_hands[swap_position]
        else:
            player4_seen[swap_position] = player_hands[swap_position]
    elif played_card[0] == 'Jack':
        # Skip Next player
        current_player += 1
        print("Player", current_player, "has been skipped.")
    elif played_card[0] == 'Queen':
        # Direct Swap
        print("You can directly swap 2 cards.")
        print("Select a card index to see")
        swap_position1 = int(input("Enter the position of CARD 1: "))
        swap_position2 = int(input("Enter the position of CARD 2: "))

        # Swap CARD 1 with CARD 2
        tmp = player_hands[swap_position1]
        player_hands[swap_position1] = player_hands[swap_position2]
        player_hands[swap_position2] = tmp

        # Update seen values for everyone
        tmp = player1_seen[swap_position1]
        player1_seen[swap_position1] = player1_seen[swap_position2]
        player1_seen[swap_position2] = tmp
        tmp = player2_seen[swap_position1]
        player2_seen[swap_position1] = player2_seen[swap_position2]
        player2_seen[swap_position2] = tmp
        tmp = player3_seen[swap_position1]
        player3_seen[swap_position1] = player3_seen[swap_position2]
        player3_seen[swap_position2] = tmp
        tmp = player4_seen[swap_position1]
        player4_seen[swap_position1] = player4_seen[swap_position2]
        player4_seen[swap_position2] = tmp

    elif played_card[0] == 'King':
        # See and Swap
        print("You can see and swap 2 cards.")
        print("Select a card index to see")
        swap_position1 = int(input("Enter the position of CARD 1: "))
        print("CARD 1: ", player_hands[swap_position1])
        swap_position2 = int(input("Enter the position of CARD 2: "))
        print("CARD 2: ", player_hands[swap_position2])

        while True:
            print("Do you want to swap cards?")
            print("1. Yes")
            print("2. No")
            ch_0 = int(input("Enter your choice: "))
            print("\n")
            if ch_0 == 1:
                # Swap CARD 1 with CARD 2
                tmp = player_hands[swap_position1]
                player_hands[swap_position1] = player_hands[swap_position2]
                player_hands[swap_position2] = tmp

                # Update seen values for everyone
                tmp = player1_seen[swap_position1]
                player1_seen[swap_position1] = player1_seen[swap_position2]
                player1_seen[swap_position2] = tmp
                tmp = player2_seen[swap_position1]
                player2_seen[swap_position1] = player2_seen[swap_position2]
                player2_seen[swap_position2] = tmp
                tmp = player3_seen[swap_position1]
                player3_seen[swap_position1] = player3_seen[swap_position2]
                player3_seen[swap_position2] = tmp
                tmp = player4_seen[swap_position1]
                player4_seen[swap_position1] = player4_seen[swap_position2]
                player4_seen[swap_position2] = tmp
                break
            # End game
            elif ch_0 == 2:
                if current_player == 1:
                    player1_seen[swap_position1] = player_hands[swap_position1]
                    player1_seen[swap_position2] = player_hands[swap_position2]
                elif current_player == 2:
                    player2_seen[swap_position1] = player_hands[swap_position1]
                    player2_seen[swap_position2] = player_hands[swap_position2]
                elif current_player == 3:
                    player3_seen[swap_position1] = player_hands[swap_position1]
                    player3_seen[swap_position2] = player_hands[swap_position2]
                else:
                    player4_seen[swap_position1] = player_hands[swap_position1]
                    player4_seen[swap_position2] = player_hands[swap_position2]
                break
            else:
                print("Invalid choice.")
                print("\n")


# Define a list of suits
suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']

# Define a list of ranks
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']

# Create a deck of cards
deck = [(rank, suit) for rank in ranks for suit in suits]
# Shuffle the deck
random.shuffle(deck)
draw_deck = deck[16:]
toss_deck = []
# Deal 4 cards to each player and Store the hands of all the players in a list
player_hands = deck[:16]

# Initializing seen cards for each player
player1_seen = player_hands[:2]
player1_seen.extend([(0, 0)] * 14)
player2_seen = [(0, 0)] * 4
player2_seen.extend(player_hands[4:6])
player2_seen.extend([(0, 0)] * 10)
player3_seen = [(0, 0)] * 8
player3_seen.extend(player_hands[8:10])
player3_seen.extend([(0, 0)] * 6)
player4_seen = [(0, 0)] * 12
player4_seen.extend(player_hands[12:14])
player4_seen.extend([(0, 0)] * 2)

current_player = 0

play_game(0)
'''
Developer Notes:
Haven't added error handling for tossing Q or K and selecting indexes to choose from. 
'''
