import time
hangover = True
inventory = [""]
locations = ["Bush", "Street", "Tavern"]
currentLocation = "Bush"
HP = 30

def action(user):
    if user == "Move" or "move":
        print("Move to:")
        for i in locations:
            if i != currentLocation:
                print(locations[i])
        currentLocation = input(": ")
    





input("Stupid story by Me (press enter to continue) ")
print("You awaken in a bush.")
print("You sit up and look around to realise you are sitting outside the tavern.")
print("About a second later, a splitting headache pierces through your thoughts.")
print("'Ah,' you manage to think, 'this must be because of those 16 beers I was...'")
print("That's about as far as your thinking goes before your mind starts to throb in pain.")
print("You should probably find a way to stop being hungover.")
print("")
action(input("Move/Look "))


