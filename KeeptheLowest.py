import random

def roll_dice(num_dice):
    return [random.randint(1, 6) for _ in range(num_dice)]

def play_turn():
    dice = roll_dice(5)
    kept_dice = []
    
    while dice:
        print(f"Rolled dice: {dice}")
        lowest = min(dice)
        kept_dice.append(lowest)
        print(f"Keeping lowest die: {lowest}")
        dice.remove(lowest)
        if dice:
            dice = roll_dice(len(dice))
    
    print(f"Kept dice: {kept_dice}")
    return sum(kept_dice)

def play_game():
    scores = [0, 0]  # Player 1 and Player 2 scores
    player = 0  # Start with player 1
    
    while max(scores) < 20:
        print(f"\nPlayer {player + 1}'s turn:")
        turn_score = play_turn()
        scores[player] += turn_score
        print(f"Player {player + 1} scored {turn_score}, total score: {scores[player]}")
        
        if scores[player] >= 20:
            print(f"Player {player + 1} loses! Game over.")
            break
        
        player = 1 - player  # Switch turns

if __name__ == "__main__":
    play_game()