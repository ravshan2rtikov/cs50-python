def main():
    difficulty = input("Difficult or Casual")
    if not (difficulty == "Difficult" or difficulty == "Casual"):
        print("Enter valid difficulty")
        return
    
    players = input("Single-player or Multiplayer")
    if not (players == "Single-player" or players == "Multiplayer"):
        print("Enter valid number of players")
        return
    
    if difficulty == "Difficult" and players == "Multiplayer":
        recommend("Poker")
    if difficulty == "Difficult" and players == "Single-player":
        recommend("Klondike")
    if difficulty == "Casual" and players == "Multiplayer":
        recommend("Hearts")
    else:
        recommend("Clock")

def recommend(game):
    print("You might like ", game)