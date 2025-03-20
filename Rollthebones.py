import random

def roll_dice():
    return [random.randint(1, 6) for _ in range(3)]

def play_round(player1_score, player2_score):
    print("\nNew Round:")
    
    # Player 1 rolls and calculates total
    player1_roll = roll_dice()
    player1_total = sum(player1_roll)
    print(f"Player 1 rolls: {player1_roll} (Total: {player1_total})")
    
    # Player 2 makes a guess
    guess = input("Player 2, guess 'Over' or 'Under': ").strip().lower()
    
    # Player 2 rolls and calculates total
    player2_roll = roll_dice()
    player2_total = sum(player2_roll)
    print(f"Player 2 rolls: {player2_roll} (Total: {player2_total})")
    
    # Determine winner
    if (guess == "over" and player2_total > player1_total) or (guess == "under" and player2_total < player1_total):
        print("Player 2 wins this round!")
        player2_score += 1
    else:
        print("Player 1 wins this round!")
        player1_score += 1
    
    print(f"Score - Player 1: {player1_score}, Player 2: {player2_score}")
    return player1_score, player2_score

def play_game():
    player1_score = 0
    player2_score = 0
    round_count = 1
    
    while player1_score < 6 and player2_score < 6:
        print(f"\n--- Round {round_count} ---")
        player1_score, player2_score = play_round(player1_score, player2_score)
        round_count += 1
        
        # Swap roles
        player1_score, player2_score = player2_score, player1_score
    
    print("\nGame Over!")
    if player1_score >= 6:
        print("Player 1 wins the match!")
    else:
        print("Player 2 wins the match!")

if __name__ == "__main__":
    play_game()
