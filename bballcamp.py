first_name = input("What is your first name? ")
team_name = input("What is your team name? ")

print()

# jersey_color = input ("What is your jersey color? ")
#team_name = "cougars"
#first_name = "Jack"

if  team_name == "AQA":
  jersey_color = "blue"
 #  print ("Your team jersey is AQA")
elif team_name == "OLS":
  jersey_color = "green"
 #  print ("Your team color is green")
else :
  jersey_color = "gray"
 #  print ("Well it looks like your jersey color is gray")

print ("Your team jersey is " + jersey_color)

print()

if team_name == "AQA":
  print("Hello", first_name, "Welcome to camp!")
  print("Your team practices on Court A today. Here is your", jersey_color, "uniform.")
elif team_name == "OLS":
  print("Hello", first_name, "Welcome to camp!")
  print("Your team practices on Court B today. Here is your", jersey_color, "uniform.")
else: 
  print("Wait a minute, something's not right. Your team isn't practicing here today!")
