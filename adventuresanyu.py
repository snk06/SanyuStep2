health = 10
hunger = 5
if health<4:
    print("Warning:Low health")
if health==0:
    print("You died. Game over. Try again?")
if hunger<4:
    print("Warning: Low hunger.")
if hunger==0:
    print("You died from hunger. Game over. Try again?")
bag = []
print("Welcome to a text adventure to find a lost amulet.")
print("Good Morning! You awaken feeling rested.")
a=input("You feel a bit hungry. Do you eat some bread?")
if a=="yes" or a=="Yes":
    hunger+=3
    print("Hunger is now", hunger)
    print("You grab a piece of bread on your way out of the house. You save some for later.")
    bag.append('bread')
    print("'bread' has been added to bag")
    print("You leave the house feeling satisfied. A villager tells you that a valuable amulet has been stolen.")
    c = input("They offer you money to find it. Do you accept the offer?")
    if c=="yes" or c=="Yes":
        print("They are grateful! They give you 10 gold coins as a start.")
        bag.append('coins')
        print("'coins' has been added to bag.")
        print("You start your journey into the woods.")
        e = input("You come across a wolf cub. Do you a.try to tame it, or do you b.leave it alone?")
        if e=="a" or e=="A":
            print("You walk closer to the cub, but you are being watched by a larger wolf. You angered it! It chases you further into the woods.")
            f = input("You find a cottage hidden behind some trees. Do you a.hide inside, or b.try to fight the wolf?")
            if f=="a" or f=="A":
                print("You  decide to hide inside the cottage. The wolf tries to get inside, but eventually gives up. You catch your breath.")
            else:
                print("You decide to fight the wolf. [A bad decision if you ask me, but I'm just the narrator!] You look around for a weapon.")
                j = input("Do you pick a. a stick, b. some rocks, or c.change your mind and climb up a tree? [Here's a tip. The tree looks pretty fragile].")
                if j=="a" or j=="A":
                    print("You pick the stick. You throw it at the wolf, hoping it will go fetch. It's not a dog! The wolf just ignores the stick and moves closer.")
                    print("You wolf gets angrier and runs toward you. You are paralyzed with fear.")
                    print("The wolf growls and mauls you. You died. Game over. Try again?")
                elif j=="b" or j=="B":
                    print("You decided to grab some rocks off the ground to throw at the wolf. [Are you kidding me?]")
                    print("You throw the rocks at the wolf, but it only gets angrier.")
                    print("It leaps at you. [Lesson of the day: don't touch wolf cubs.]")
                    print("You died. Game over. Try again?")
                else:
                    print("You choose to climb up the tree. [I lied. Looks like you're light enough for the tree not to break.]")
                    print("Lucky for you, this particular wolf can't jump that high. It gives up and goes away.")
                    print("Once you are sure it's gone, you jump down.")
                    print("You hear a noise and you think it could be the wolf looking for revenge so you run until you're sure the wolf can't reach you.")
                    k = input("You come across a cottage. Do you go inside? [By the way, it's getting dark out.]")
                    if k=="yes" or k=="Yes":
                        print("You go inside.")
                    else:
                        print("For some odd reason, you decide not to go in and get shelter.")
                        print("[I mean, there may be seven dwarves for all we know.] You come across a large stick. [Excellent for self defense, hint hint!]")
                        l = input("Do you a.pick up the stick or b.accept your deat--[I mean,] or do you b.choose not to pick up the stick?")
                        if l=="a" or l=="A":
                            bag.append('stick')
                            print("'stick' has been added to bag.")
                            print("[Who knows what could be out ther--] Aaaaand there's a snake in front of you.")
                            m = int(input("You're fighting it, no choice. Pick a number. Any number."))
                            if m%2==0:
                                print("Oof. Except that one. The snake hisses and lashes out at you. It knocks the stick out of your hand and bites you.")
                                print("Darn it. It's venomous. You died. Game over. Try again?")
                            else:
                                print("Lucky you. You manage to hit the snake with the stick before it notices you. [Good for you! I think it was venomous!]")
                                print("Unfortunately, your luck soon runs out as you are cold, tired, and hungry.")
                                hunger-=4
                                print("Hunger is now", hunger)
                                n = input("Do you a. eat and sleep here or b.keep wandering around the forest?")
                                if n=="a" or n=="A":
                                    print("You decide to settle down where you are. You eat your remaining bread.")
                                    hunger+=3
                                    print("Hunger is now", hunger)
                                else:
                                    ("You decide to keep wandering around the forest")
        else:
            print("You leave the wolf alone. You wander further into the woods. You hear a rustling in the trees.")
            g = input("Do you a.Try and figure out what it is or b.ignore it?")
            if g=="a" or g=="A":
                print("You try to find out what made the noise. You shake the tree from which the noise came. Its an owl! And it does not look happy.")
                h = input("You have no choice but to defend yourself. You look around for potential weapons. Do you pick a.A stick, b.Throw your bread at it, or c., try to run away?")
                if h=="a" or g=="A":
                    print("You grab the stick and try to hit the owl, but the stick you have found is merely a twig. It snaps and the owl attacks you.")
                    print("You died. Game Over. Try Again?")
                elif h=="b" or h=="B":
                    print("You grab your leftover bread from your bag and throw it at the owl.") 
                    print("It distracts it just long enough for you to run away, but you have no food.")
                    bag.remove("bread")
                    print("'bread' has been removed from bag.")
                    print("You keep wandering around the forest, hungry and scared.")
                else:
                    ("You attempt to run away but the owl follows you. It pecks at you, and you are in extreme pain.")
                    print("You died. Game over. Try again?")
            else:
                print("You ignore the noise.")
    else:
        print("They accuse you of stealing the amulet. You are thrown in jail. oof. Try again?")    
else: 
    print("You leave the house without eating. A villager approaches you. They say that a valuable amulet has been stolen.")
    d = input("They are offering you money to find it. Do you accept?")
    if d=="yes" or d=="Yes":
        print("You accept their offer. They thank you and give you 10 gold coins for the journey.")
        bag.append('10 coins')
        print("'coins' has been added to bag.")
        print("You start your journey into the woods.")
        e = input("You come across a wolf cub. Do you a.try to tame it, or do you b.leave it alone?")
        if e=="a" or e=="A":
            print("You walk closer to the cub, but you are being watched by a larger wolf. You angered it! It chases you further into the woods.")
            f = input("You find a cottage hidden behind some trees. Do you a.hide inside, or b.try to fight the wolf?")
            if f=="a" or f=="A":
                print("You  decide to hide inside the cottage. The wolf tries to get inside, but eventually gives up. You catch your breath.")
            else:
                print("You decide to fight the wolf. [A bad decision if you ask me, but I'm just the narrator!] You look around for a weapon.")
                j = input("Do you pick a. a stick, b. some rocks, or c.change your mind and climb up a tree? [Here's a tip. The tree looks pretty fragile].")
                if j=="a" or j=="A":
                    print("You pick the stick. You throw it at the wolf, hoping it will go fetch. It's not a dog! The wolf just ignores the stick and moves closer.")
                    print("You wolf gets angrier and runs toward you. You are paralyzed with fear.")
                    print("The wolf growls and mauls you. You died. Game over. Try again?")
                elif j=="b" or j=="B":
                    print("You decided to grab some rocks off the ground to throw at the wolf. [Are you kidding me?]")
                    print("You throw the rocks at the wolf, but it only gets angrier.")
                    print("It leaps at you. [Lesson of the day: don't touch wolf cubs.]")
                    print("You died. Game over. Try again?")
                else:
                    print("You choose to climb up the tree. [I lied. Looks like you're light enough for the tree not to break.]")
                    print("Lucky for you, this particular wolf can't jump that high. It gives up and goes away.")
                    print("Once you are sure it's gone, you jump down.")
                    print("You hear a noise and you think it could be the wolf looking for revenge so you run until you're sure the wolf can't reach you.")
                    k = input("You come across a cottage. Do you go inside? [By the way, it's getting dark out.]")
                    if k=="yes" or k=="Yes":
                        print("You go inside.")
                    else:
                        print("For some odd reason, you decide not to go in and get shelter.")
                        print("[I mean, there may be seven dwarves for all we know.] You come across a large stick. [Excellent for self defense, hint hint!]")
                        l = input("Do you a.pick up the stick or b.accept your deat--[I mean,] or do you b.choose not to pick up the stick?")
                        if l=="a" or l=="A":
                            bag.append('stick')
                            print("'stick' has been added to bag.")
                            print("[Who knows what could be out ther--] Aaaaand there's a snake in front of you.")
                            m = int(input("You're fighting it, no choice. Pick a number. Any number."))
                            if m%2==0:
                                print("Oof. Except that one. The snake hisses and lashes out at you. It knocks the stick out of your hand and bites you.")
                                print("Darn it. It's venomous. You died. Game over. Try again?")
                            else:
                                print("Lucky you. You manage to hit the snake with the stick before it notices you. [Good for you! I think it was venomous!]")
                                print("Unfortunately, your luck soon runs out as you are cold, tired, and hungry.")
                                hunger-=4
                                print("Hunger is now", hunger)
                                n = input("Do you a. eat and sleep here or b.keep wandering around the forest?")
                                if n=="a" or n=="A":
                                    print("You decide to settle down where you are. You eat your remaining bread.")
                                    hunger+=3
                                    print("Hunger is now", hunger)
                                else:
                                    ("You decide to keep wandering around the forest.")
        else:
            print("You leave the wolf alone. You wander further into the woods. You hear a rustling in the trees.")
            g = input("Do you a.Try and figure out what it is or b.ignore it?")
            if g=="a" or g=="A":
                print("You try to find out what made the noise. You shake the tree from which the noise came. Its an owl! And it does not look happy.")
                h = input("You have no choice but to defend yourself. You look around for potential weapons. Do you pick a.A stick, b.Throw your bread at it, or c., try to run away?")
                if h=="a" or g=="A":
                    print("You grab the stick and try to hit the owl, but the stick you have found is merely a twig. It snaps and the owl attacks you.")
                    print("You died. Game Over. Try Again?")
                elif h=="b" or h=="B":
                    print("You grab your leftover bread from your bag and throw it at the owl.") 
                    print("It distracts it just long enough for you to run away, but you have no food.")
                    bag.remove("bread")
                    print("'bread' has been removed from bag.")
                    print("You keep wandering around the forest, hungry and scared.")
                else:
                    ("You attempt to run away but the owl follows you. It pecks at you, and you are in extreme pain.")
                    print("You died. Game over. Try again?")
            else:
                print("You ignore the noise.")
    else:
            print("They accuse you of stealing the amulet. You are thrown in jail. oof. Try again?")

#abcdefghjklmn