import random

def rollsDice():
    return random.randint(1, 6)

def playgame(player1, player2):
    scores = {player1: 0, player2: 0}
    turn = player1  # Start with player1

    while scores[player1] < 100 and scores[player2] < 100:
        roll = rollsDice()
        print(f"{turn}, you rolled a {roll}")

        if roll == 1:
            print(f"{turn}, you rolled a 1! Turn over.")
            turn = player1 if turn == player2 else player2  # Switch player
        else:
            scores[turn] += roll
            print(f"{turn}, your score is {scores[turn]}")

            if scores[turn] >= 100:
                print(f"Congratulations {turn}, you win with a score of {scores[turn]}!")
                break

        print("-" * 30)  # Separator for clarity

    print("\nFinal Scores:")
    for player, score in scores.items():
        print(f"{player}: {score}")

# Example usage
if __name__ == "__main__":
    playgame("Cypher", "Suo")