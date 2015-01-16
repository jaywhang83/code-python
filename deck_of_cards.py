__author__ = 'student'
# lists of, suits, ranks, color you can iterate through. Also empty list called decks to hold decks of cards
suits = ["spade", "diamond", "club", "heart"]
ranks = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
color = ["black", "red"]
decks = []
matched_cards_color = []

for card in suits:

    for j in ranks:
        if card == "heart" or card == "diamond":
            color = "red"
        else:
            color = "black"
        decks.append((card, j, color)) # adding multiple elements to list.

print decks

# function for finding and printing cards by ranks
def search_suit():
    matched_cards = []
    user_search_term = raw_input("what suit do you want?")
    for card in decks:
        if user_search_term == card[0]:
            matched_cards.append(card)
    print(matched_cards)

# function for finding and printing cards by ranks
def search_rank():
    user_search_term_ranks = raw_input("What rank do you want?")
    for j in decks:
        if user_search_term_ranks == j[1]:
            print(j)

# fuction for finding and printing cards by color
def search_color():
    user_search_term_color = raw_input("what color do you want?")
    for color in decks:
        if user_search_term_color == color[2]:
            print(color)

# main function for running search function for suit, rank, and color
def menu():
    while True:
        search_suit()
        search_rank()
        search_color()
        option = raw_input("DO you want to continue? ")
        if option == "no":
            break
menu()
exit()
