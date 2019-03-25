#This is start of the system I will use for my final project
#My idea for the final project is a simple Turn-Based game
#The user selects a Player (the superclass) Type (one of 3 subclasses)
#Then fights the "Enemy" with that selected type in a turn-based game mode until one side has 0 HP (hit points)
#I'll use this assignment to start building that structure out

class Player():
    def __init__(self, kind, hpAmount):
        self.kind = kind
        if hpAmount == 'k':
            self.hpAmount = 150
        elif hpAmount == 'a':
            self.hpAmount = 125
        else:
            self.hpAmount = 100
    
    def get_hp(self):
        return self.hpAmount
    
    def damage_hp(self, amount):
        self.hpAmount -= amount
        return self.hpAmount
    
    def heal_hp(self, amount):
        self.hpAmount += amount
        return self.hpAmount

class Knight(Player):
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon
        Player.__init__(self, "Knight", 'k')
    
    def get_description(self):
        return print("You've chosen to play as a Knight! You have Melee and Shield abilities.")
    
    def getallinfo(self):
        print("%s is a %s with a %s, and has %s Hit Points" % (self.name, self.kind, self.weapon, self.hpAmount))
    
    def get_Name(self):
        return self.name
    
    def get_Weapon(self):
        return self.weapon
      
class Archer(Player):
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon
        Player.__init__(self, "Archer", 'a')
    
    def get_description(self):
        return print("You've chosen to play as an Archer! You have a Ranged Shot and Critical Hit abilities.")
    
    def getallinfo(self):
        print("%s is a %s with a %s, and has %s Hit Points" % (self.name, self.kind, self.weapon, self.hpAmount))
    
    def get_Name(self):
        return self.name
    
    def get_Weapon(self):
        return self.weapon
    
class Mage(Player):
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon
        Player.__init__(self, "Mage", 'm')
    
    def get_description(self):
        return print("You've chosen to play as a Mage! You have Spell and Heal abilities.")
    
    def getallinfo(self):
        print("%s is a %s with a %s, and has %s Hit Points" % (self.name, self.kind, self.weapon, self.hpAmount))
    
    def get_Name(self):
        return self.name
    
    def get_Weapon(self):
        return self.weapon

def main():
    #Get User Info to Start 
    getName = input("Tell us your name: ")
    getType = input("Choose your type: Knight(k), Archer(a), or Mage(m): ")
    
    #Check that the getType is valid, loop until input is valid
    validTypes = ["k", "a", "m"] #array of valid inputs
    while getType not in validTypes: #check input against array
        print("only lowercase 'k', 'a', or 'm' are valid, please try again.") #print error message
        getType = input("Choose your type: Knight(k), Archer(a), or Mage(m): ") #request another input

    #now that we have our valid input, we can continue and instantiate our objects based on Type selected
    if getType == "k":
        player1 = Knight(getName, "Sword")
        player1.get_description()
        print(player1.get_Name())
        player1.getallinfo()
        player1.damage_hp(25)
        player1.getallinfo() 
    elif getType == "a":
        player1 = Archer(getName, "Bow")
        Archer.get_description(player1)
        print(player1.get_Name())
        player1.getallinfo()
        player1.damage_hp(25)
        player1.getallinfo() 
    else:
        player1 = Mage(getName, "Wand")
        Mage.get_description(player1)
        print(player1.get_Name())
        player1.getallinfo()        
        player1.damage_hp(25)
        player1.getallinfo() 
main()