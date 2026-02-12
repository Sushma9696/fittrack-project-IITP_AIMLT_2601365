def game():
  player_name=input("Enter the player's name:")
  number_of_games=int(input("Number of games played:"))
  score=int(input("Total score achieved:"))
  average_score=score/number_of_games
  print(f"\nPlayer: {player_name}")
  print(f"Games Played: {number_of_games}")
  print(f"Total Score: {score}")
  print(f"Average Score: {average_score}")
  

game()

