#############################################
# CSE 231
# Computer Project #6
#   Algorithm
#############################################

import cards

def less_than(c1,c2):
    '''Return 
           True if c1 is smaller in rank, 
           True if ranks are equal and c1 has a 'smaller' suit
           False otherwise'''
    if c1.rank() < c2.rank():
        return True
    elif c1.rank() == c2.rank() and c1.suit() < c2.suit():
        return True
    return False
    
def min_in_list(L):
    '''Return the index of the mininmum card in L'''
    min_card = L[0]  # first card
    min_index = 0
    for i,c in enumerate(L):
        if less_than(c,min_card):  # found a smaller card, c
            min_card = c
            min_index = i
    return min_index
        
def cannonical(H):
    ''' Selection Sort: find smallest and swap with first in H,
        then find second smallest (smallest of rest) and swap with second in H,
        and so on...'''
    for i,c in enumerate(H):
        # get smallest of rest; +i to account for indexing within slice
        min_index = min_in_list(H[i:]) + i 
        H[i], H[min_index] = H[min_index], c  # swap
    return H

def flush_7(H): # all have same suit
    '''Return a list of 5 cards forming a flush,
       if at least 5 of 7 cards form a flush in H, a list of 7 cards, 
       False otherwise.'''
    s1 = []
    s2 = []
    s3 = []
    s4 = []
    for card in H: #for cards in hand
        if card.suit() == 1: # if card has suit, add to suit list
            s1.append(card)
        if card.suit() == 2: 
            s2.append(card)  
        if card.suit() == 3: 
            s3.append(card)
        if card.suit() == 4: 
            s4.append(card)
    if len(s1) >= 5: # if list has 5 or more cards, return first 5 cards
        return s1[:5]
    if len(s2) >= 5:
        return s2[:5]
    if len(s3) >= 5:
        return s3[:5]
    if len(s4) >= 5:
        return s4[:5]
    return False
    
def straight_7(H): # run of 5, diff suits
    '''Return a list of 5 cards forming a straight,
       if at least 5 of 7 cards form a straight in H, a list of 7 cards, 
       False otherwise.'''
    H_sorted = cannonical(H)
    straight = []
    count = H_sorted[0].rank()
    for card in H_sorted:
        if card.rank() == count:
            straight.append(card)
            count +=1
    if len(straight) >= 5:
        return straight[:5]
    else:
        return False
        
# STRAIGHT FLUSH IS RANKED HIGHEST
def straight_flush_7(H): # run of 5, same suit
    '''Return a list of 5 cards forming a straight flush,
       if at least 5 of 7 cards form a straight flush in H, a list of 7 cards, 
       False otherwise.'''
    # call flush_7() and straight_7() and if both return a list, check to see if same list, and if so then straight flush is true, return straight flush
    flush = flush_7(H)
    straight = straight_7(H)
    if flush != False and straight != False:
        strt_flsh = []
        for card in flush:
            if card in straight:
                strt_flsh.append(card)
        return strt_flsh
    return False
                
def four_7(H): # 4 cards of same rank, diff suit
    '''Return a list of 4 cards with the same rank,
       if 4 of the 7 cards have the same rank in H, a list of 7 cards, 
       False otherwise.'''
    rank_dict = {}
    fours = []
    for card in H:
        rank = card.rank()
        if rank not in rank_dict:
            rank_dict[rank] = [card]
        else:
            rank_dict[rank].append(card)
    for val in rank_dict.values():
        if len(val) == 4:
            for i in val:
                fours.append(i)
    if len(fours) == 4:
        return fours
    else:
        return False
    
def three_7(H): # 3 cards of same rank, diff suit
    '''Return a list of 3 cards with the same rank,
       if 3 of the 7 cards have the same rank in H, a list of 7 cards, 
       False otherwise.
       You may assume that four_7(H) is False.'''
    threes = []
    rank_dict = {}
    for card in H:
        rank = card.rank()
        if rank not in rank_dict:
            rank_dict[rank] = [card]
        else:
            rank_dict[rank].append(card)
    for val in rank_dict.values():
        if len(val) == 3:
            for i in val:
                threes.append(i)
    if len(threes) >= 3:
        return threes[:3]
    else:
        return False
        
def two_pair_7(H): # 2 of same rank and 2 of same rank -- two sets of 2
    '''Return a list of 4 cards that form 2 pairs,
       if there exist two pairs in H, a list of 7 cards, 
       False otherwise.  
       You may assume that four_7(H) and three_7(H) are both False.'''
    rank_dict = {}
    pairs = []
    for card in H:
        #rank = card.rank()
        if card.rank() not in rank_dict:
            rank_dict[card.rank()] = [card]
        else:
            rank_dict[card.rank()].append(card)
    for val in rank_dict.values():
       if len(val) == 2:
           for i in val:
               pairs.append(i)
    if len(pairs) == 4:
        return pairs
    else:
        return False 

def one_pair_7(H):
    '''Return a list of 2 cards that form a pair,
       if there exists exactly one pair in H, a list of 7 cards, 
       False otherwise.  
       You may assume that four_7(H), three_7(H) and two_pair(H) are False.'''
    rank_dict = {}
    pair = []
    for card in H:
        #rank = card.rank()
        if card.rank() not in rank_dict:
            rank_dict[card.rank()] = [card]
        else:
            rank_dict[card.rank()].append(card)
    for val in rank_dict.values():
       if len(val) == 2:
           for i in val:
               pair.append(i)
    if len(pair) == 2:
        return pair
    else:
        return False                    

def full_house_7(H): # 3 of same rank + 2 of same rank -- 1 set of 3 and 1 set of 2
    '''Return a list of 5 cards forming a full house,
       if 5 of the 7 cards form a full house in H, a list of 7 cards, 
       False otherwise.
       You may assume that four_7(H) is False.'''    
    full = []
    threes = []
    threes_count = 0
    twos = []
    twos_count = 0
    rank_dict = {}
    for card in H:
        rank = card.rank()
        if rank not in rank_dict:
            rank_dict[rank] = [card]
        else:
            rank_dict[rank].append(card)
    for val in rank_dict.values():
        if len(val) >= 3:
            threes_count +=1
            for i in val:
                threes.append(i)
        if len(val) == 2:
            twos_count +=1
            for i in val:
                twos.append(i)
    if threes_count >=1 and twos_count >=1:
        for i in range(2):
            full.append(twos[i])
        for i in range(3):
            full.append(threes[i])
        return full
        #return three_7(H) + one_pair_7(H)
    else:
        return False


def find_winner(player1,player2):
    '''
    player1 : list
        cards passed to player 1 plus community cards 
    player2 : list
        cards passed to player 2 plus community cards
    loops through each category, starting with highest category
    looks to see if either players hand fits in category
    if either one or both return a list from the function, looks which one(s) do
    if neither hands in category, moves to test next highest category function
    Returns:
        winner (str), winning category (str) winning hand (list) 
    '''
    bool = False
    while not bool:
        if straight_flush_7(player1) != False or straight_flush_7(player2) != False: # if one or both have it
            winning_type = 'straight flush' 
            if straight_flush_7(player1) != False: # if player 1 has it
                winning_hand = straight_flush_7(player1) # printing player 1 hand if they win or if tie
                if straight_flush_7(player2) != False: # if player 1 AND player 2 have it
                    winner = 'TIE'
                else: # Only player 1 has it
                    winner = 'Player 1 wins'
            else: # the or statement is true bc of player 2/ player 2 has it but player 1 doesnt
                winning_hand = straight_flush_7(player2)
                winner = 'Player 2 wins'
            bool = True
            
        elif four_7(player1) != False or four_7(player2) != False: 
            winning_type = 'four of a kind' 
            if four_7(player1) != False: 
                winning_hand = four_7(player1)
                if four_7(player2) != False: 
                    winner = 'TIE'
                else: 
                    winner = 'Player 1 wins'
            else: 
                winning_hand = four_7(player2)
                winner = 'Player 2 wins' 
            bool = True
            
        elif full_house_7(player1) != False or full_house_7(player2) != False: 
            winning_type = 'a full house' 
            if full_house_7(player1) != False: 
                winning_hand = full_house_7(player1) 
                if full_house_7(player2) != False: 
                    winner = 'TIE'
                else: 
                    winner = 'Player 1 wins'
            else: 
                winning_hand = full_house_7(player2)
                winner = 'Player 2 wins' 
            bool = True
    
        elif flush_7(player1) != False or flush_7(player2) != False: 
            winning_type = 'a flush' 
            if flush_7(player1) != False: 
                winning_hand = flush_7(player1) 
                if flush_7(player2) != False: 
                    winner = 'TIE'
                else:
                    winner = 'Player 1 wins'
            else: 
                winning_hand = flush_7(player2)
                winner = 'Player 2 wins'
            bool = True        
            
        elif straight_7(player1) != False or straight_7(player2) != False: 
            winning_type = 'a straight'
            if straight_7(player1) != False:
                winning_hand = straight_7(player1)
                if straight_7(player2) != False: 
                    winner = 'TIE'
                else: 
                    winner = 'Player 1 wins'
            else: 
                winning_hand = straight_7(player2)
                winner = 'Player 2 wins'
            bool = True
    
        elif three_7(player1) != False or three_7(player2) != False: 
            winning_type = 'three of a kind' 
            if three_7(player1) != False:
                winning_hand = three_7(player1) 
                if three_7(player2) != False: 
                    winner = 'TIE'
                else: 
                    winner = 'Player 1 wins'
            else: 
                winning_hand = three_7(player2)
                winner = 'Player 2 wins'
            bool = True
    
        elif two_pair_7(player1) != False or two_pair_7(player2) != False: 
            winning_type = 'two pairs' 
            if two_pair_7(player1) != False:
                winning_hand = two_pair_7(player1) 
                if two_pair_7(player2) != False: 
                    winner = 'TIE'
                else: 
                    winner = 'Player 1 wins'
            else: 
                winning_hand = two_pair_7(player2)
                winner = 'Player 2 wins'
            bool = True
    
        elif one_pair_7(player1) != False or one_pair_7(player2) != False: 
            winning_type = 'one pair' 
            if one_pair_7(player1) != False:
                winning_hand = one_pair_7(player1) 
                if one_pair_7(player2) != False: 
                    winner = 'TIE'
                else: 
                    winner = 'Player 1 wins'
            else: 
                winning_hand = one_pair_7(player2)
                winner = 'Player 2 wins'
            bool = True
        
        else:
            winning_type = 'high card'
            winner = 'TIE'
            winning_hand = player1[:5]
            bool = True

    return winner, winning_type, winning_hand


def main():
    D = cards.Deck()
    D.shuffle()
    remaining = D.__len__()
    bool = True
    
    while bool:
        if remaining < 9:
            print('Deck has too few cards so game is done.')
            break
        if remaining >= 9: #instead of 'while True' - may not be what that was there for
            community_list = []
            hand_1_list = []
            hand_2_list = []
             
            for i in range(5):
                community_list.append(D.deal())
            for i in range(2):
                hand_1_list.append(D.deal())
            for i in range(2):
                hand_2_list.append(D.deal())
                 
            player1 = community_list + hand_1_list
            player2 = community_list + hand_2_list
             
            print("-"*40)
            print("Let's play poker!\n")
            print("Community cards:",community_list)
            print("Player 1:",hand_1_list)
            print("Player 2:",hand_2_list)
            
            c1 = cards.Card(2,3)
            c2 = cards.Card(3,3)
            c3 = cards.Card(1,4)
            c4 = cards.Card(2,1)
            c5 = cards.Card(3,4)
            c6 = cards.Card(2,2)
            c7 = cards.Card(1,2)
            
            test = [c1,c2,c3,c4,c5,c6,c7]
            
            winner, winning_type, winning_hand = find_winner(player1, player2)
            print('\n{} with {}: {}'.format(winner, winning_type, winning_hand))
            # print(test)
            # print(full_house_7(test))
            print()
             
            remaining = remaining - 9
            if remaining >=9:
                another_hand = input('Do you wish to play another hand?(Y or N) ').lower()
      #      if another_hand == 'y':
       #         remaining = remaining - 9
                if another_hand == 'n': # then no longer True
                    bool = False


if __name__ == "__main__":
    main()