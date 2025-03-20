import random

def roll_dice(num_dice=10):
    return [random.randint(1, 6) for _ in range(num_dice)]

def play_turn(player):
    print(f"\n{player}'s turn:")
    target = random.randint(1, 6)  # Player predicts a target number
    print(f"Predicted number: {target}")
    
    dice_rolls = roll_dice()
    print(f"Rolled dice: {dice_rolls}")
    
    if dice_rolls.count(target) >= 2:
        print(f"{player} found a matching pair and stays in the game!")
        return True  # Player stays in the game
    else:
        print(f"{player} found no matching pair and is eliminated!")
        return False  # Player is eliminated

def play_game():
    players = ["Player 1", "Player 2", "Player 3"]
    
    while len(players) > 1:
        for player in players[:]:  # Iterate over a copy to allow removal
            if not play_turn(player):
                players.remove(player)
        
        print(f"Remaining players: {players}")
    
    print(f"\nGame Over! {players[0]} is the winner!")

if __name__ == "__main__":
    play_game()
