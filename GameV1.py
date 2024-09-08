# commands #

answer_n = ["North", "N", "north", "n", "NORTH"]
answer_s = ["South", "S", "south", "s", "SOUTH"]
answer_e = ["East", "E", "east", "e", "EAST"]
answer_w = ["West", "W", "west", "w", "WEST"]

answer_y = ["Yes", "YES", "Y", "yes", "y"]
answer_no = ["No", "NO", "N", "no", "n"]
decision = [answer_y, answer_no]

directions = [answer_n, answer_s, answer_e, answer_w]

win_game = ["exit", "Exit", "EXIT", "X", "x"]

player_belt = ["", ]

flags = {8, }

Backpack = ["", ]


# rooms #
def start():
    if 1 not in flags:  # First time in the room
        print("\nThe room is pitch black.")
        flags.add(1)
    else:
        print("\nThis is where you started from.")
        print("\nThe room is pitch black.")
    userInput = ""
    while userInput not in directions:
        print("\nOptions: north/east/west")
        userInput = input()
        if userInput in answer_e:
            gotoroom1()
        elif userInput in answer_w:
            gotoroom2()
        elif userInput in answer_n:
            gotoroom4()
        elif userInput in answer_s:
            print("\nI can't go back...")
        else:
            print("\nI can't do that")


def gotoroom1():
    print("\nYou see a simple room with stone walls. "
          "\nA message has been written in what looks like dried blood:")
    print('\nSHE FEARS IRON')  # Player hint for Fairy Queen encounter
    if 2 not in flags:
        print("... who is 'She'?")
    flags.add(2)
    userInput = ""
    while userInput not in directions:
        print("\nOptions: north/west")
        userInput = input()
        if userInput in answer_n:
            gotoroom3()
        elif userInput in answer_w:
            start()
        else:
            print("I can't do that")


def gotoroom2():
    print("\nYou see a room with walls thickly coated in green moss. "
          "\nA message has been carved into it:")
    print("\nDO NOT GIVE HER YOUR NAME")  # Player hint for Fairy Queen encounter
    userInput = ""
    while userInput not in directions:
        print("\nOptions: north/east")
        userInput = input()
        if userInput in answer_n:
            gotoroom5()
        elif userInput in answer_e:
            start()
        else:
            print("\nI can't do that")


def gotoroom3():
    if 3 not in flags:  # If you haven't got the hint yet
        print(
            "\nThere is something faintly glowing on the wall, but it is impossible to make out in the light from your lantern."
            "\nWould you like to blow out your lantern?")
        userInput = ""
        while userInput not in decision:
            print("\nOptions: Yes/No")
            userInput = input()
            if userInput in answer_y:
                print("\nPainted on the wall in phosphorescent paint is a picture:")
                print('\nUnderneath it is the name "Fairy Tear".')
                print("\nYou re-light your lantern.")
                flags.add(3)
                userInput = ""
                while userInput not in directions:
                    print("\nOptions: south/west")
                    userInput = input()
                    if userInput in answer_s:
                        gotoroom1()
                    elif userInput in answer_w:
                        gotoroom4()
                    else:
                        print("\nI can't do that.")
            elif userInput in answer_no:
                print("\nYou keep your lantern lit.")
                while userInput not in directions:
                    print("\nOptions: south/west")
                    userInput = input()
                    if userInput in answer_s:
                        gotoroom1()
                    elif userInput in answer_w:
                        gotoroom4()
                    else:
                        print("\nI can't do that.")
            else:
                print("\nI can't do that.")
    else:
        print("\nThere's a faint glow on the wall from the hidden painting.")
        print("\nSo the Fairy Tear is a flower...")
        userInput = ""
        while userInput not in directions:
            print("\nOptions: south/west")
            userInput = input()
            if userInput in answer_s:
                gotoroom1()
            elif userInput in answer_w:
                gotoroom4()
            else:
                print("\nI can't do that.")


def gotoroom4(riddle=["CAT", "Cat", "cat"]):  # Riddle/Sphinx room, only needed if amulet lost in Fairy encounter
    print("\nThere is statue of a sphinx made of obsidian in the middle of the room.")
    if 4 in flags:
        print("\nThere's nothing else to do here.")
    else:
        print("\nThere's something written on the base of the statue:\n"
              "\nTiny hunter, silent steps"
              "\nWith daggers sheathed, eyes gleaming"
              "\nFearless, stalking darkest night"
              "\nSlips through my window, barely open"
              "\nI wake again to gentle kneading"
              "\nTo rumbling warmth upon my chest\n")
        print("\nWHAT AM I?")
        userInput = ""
        while userInput not in decision:
            print("\nWill you answer: Yes/No")
            userInput = input()
            if userInput in answer_y:
                print("\nYou ponder the riddle, and prepare to speak.")
                userInput = ""
                while userInput not in riddle:
                    print("\nWHAT IS YOUR ANSWER?")
                    userInput = input()
                    if userInput in riddle:
                        print("\nA gold coin falls from the sphinx's mouth."
                              "\nYou pick it up and put it in your backpack.")
                        Backpack.append("Gold Coin")  # Needed for the Wishing Well
                        flags.add(4)
                        userInput = ""
                        while userInput not in directions:
                            print("\nOptions: north/south/east")
                            userInput = input()
                            if userInput in answer_n:
                                gotoroom7()
                            elif userInput in answer_e:
                                gotoroom3()
                            elif userInput in answer_s:
                                start()
                            else:
                                print("\nI can't do that.")
                    else:
                        print("\nThat wasn't right.")
            elif userInput in answer_no:
                print("\nYou choose to leave the sphinx alone for now.")
                userInput = ""
                while userInput not in directions:
                    print("\nOptions: north/south/east")
                    userInput = input()
                    if userInput in answer_n:
                        gotoroom7()
                    elif userInput in answer_e:
                        gotoroom3()
                    elif userInput in answer_s:
                        start()
                    else:
                        print("\nI can't do that.")
            else:
                print("\nI can't do that.")
    userInput = ""
    while userInput not in directions:
        print("\nOptions: north/south/east")
        userInput = input()
        if userInput in answer_n:
            gotoroom7()
        elif userInput in answer_e:
            gotoroom3()
        elif userInput in answer_s:
            start()
        else:
            print("\nI can't do that.")


def gotoroom5():
    print("\nThe floor in this room is made of loosely packed earth.")
    if "Gold Key" in Backpack:
        print("\nThere's nothing else here.")
    else:
        print("\nThere is something shiny buried in the dirt.")
        print("\nIt's a gold key! You pick it up and put it in your Backpack.")
        Backpack.append("Gold Key")  # Needed to open Gold Gate in Room 13
    userInput = ""
    while userInput not in directions:
        print("\nOptions: south")
        userInput = input()
        if userInput in answer_s:
            gotoroom2()
        else:
            print("\nI can't do that.")


def gotoroom6():
    print(
        "\nThere is a skeleton laying on the floor; a few scraps of rusted chainmail cling to its frame. "
        "\nIt looks like they crawled here from the room to the north...")
    userInput = ""
    while userInput not in directions:
        print("\nOptions: north/west")
        userInput = input()
        if userInput in answer_n:
            gotoroom9()
        elif userInput in answer_w:
            gotoroom7()
        else:
            print("\nI can't do that.")


def gotoroom7():
    print(
        '\nThis room is well-lit by floating balls of light.')
    if 6 not in flags:  # Fairy Queen dealt with
        print("\nA woman stands in front of the exit to the west.")
        if 5 not in flags:  # first time in room
            print(
                "\nShe's tall, stunningly beautiful, and judging by her pointed ears (and equally pointy teeth) clearly not human."
                "\nShe smiles, and gestures for you to come forward.")
            print("\nWill you approach?")
            flags.add(5)
            userInput = ""
            while userInput not in decision:
                print("\nOptions: Yes/No")
                userInput = input()
                if userInput in answer_y:  # Talking to the Fairy Queen
                    print("\nYou cautiously approach the woman."
                          "\nShe smiles at you again, clearly trying to be friendly, but something about it sends chills down your spine...\n"
                          "\n'Greetings little one. Another come seeking the Fairy Tear, I assume?'\n"
                          "\nYou nod warily.\n"
                          "\n'Well then, I'm happy to give it to you, but I will have to ask for something in exchange."
                          "\nNothing major, just a little bit of courtesy.'"
                          "\nShe smiles impossibly wider."
                          "\n'Simply give me your name.'\n")
                    print("\nWill you give her your name?")
                    userInput = ""
                    while userInput not in decision:
                        print("\nOptions: Yes/No")
                        userInput = input()
                        if userInput in answer_y:
                            print("\nI am Ser " + player_name + ", a knight of the kingdom.")
                            print(
                                "\nHer smile twists cruelly, as if laughing at a joke made at your expense."
                                "\n'Thank you Ser knight, and please do enjoy your prize.'")
                            print("\nYou blink, and she vanishes."
                                  "\nPeering ahead into the room she was guarding, you can't help but feel as though you have lost something...")
                            Backpack.remove(Amulet)
                            flags.remove(8)
                            flags.add(6)  # Fairy Queen dealt with
                            userInput = ""
                            while userInput not in directions:
                                print("\nOptions: north/south/east/west")
                                userInput = input()
                                if userInput in answer_n:
                                    gotoroom10()
                                elif userInput in answer_e:
                                    gotoroom6()
                                elif userInput in answer_s:
                                    gotoroom4()
                                elif userInput in answer_w:
                                    gotoroom8()
                                else:
                                    print("\nI can't do that")
                        elif userInput in answer_no:
                            print("\nShe shrugs."
                                  "\n'Then I cannot let you pass.'")
                            if "Rusty Sword" in player_belt:
                                print("\nFor a second, you see her eyes flicker to the sword on your belt.")
                                userInput = ""
                                while userInput not in decision:
                                    print("\nWill you draw your sword?"
                                          "\nOptions: Yes/No")
                                    userInput = input()
                                    if userInput in answer_y:
                                        print("\nYou pull out the Rusty Sword."
                                              "\nThe woman's eyes immediately flicker red, her beautiful face twisting into a monstrous visage."
                                              "\nHer entire body elongates with a cracking of bones, her fingertips now capped with gnarled claws."
                                              "\nShe lunges at you, her claws aimed straight at your eyes as you instinctively swing the dulled blade."
                                              "\nIt passes through her body with shockingly little resistance."
                                              "\nHer form shudders like ripples on the surface of a disturbed pond before bursting into silvery mist, her final scream ringing in your ears."
                                              "\nYour hands shake as you tie the sword back to your belt."
                                              "\nYou are now free to explore the room beyond.")
                                        flags.add(6)  # Fairy Queen dealt with
                                        userInput = ""
                                        while userInput not in directions:
                                            print("\nOptions: north/south/east/west")
                                            userInput = input()
                                            if userInput in answer_n:
                                                gotoroom10()
                                            elif userInput in answer_e:
                                                gotoroom6()
                                            elif userInput in answer_s:
                                                gotoroom4()
                                            elif userInput in answer_w:
                                                gotoroom8()
                                            else:
                                                print("\nI can't do that")
                                    elif userInput in answer_no:
                                        print(
                                            "\nYou're not sure if violence is the answer, especially with such a poor weapon."
                                            "\nShe smiles at you once more."
                                            "\nCome back if you change your mind.")
                                        userInput = ""
                                        while userInput not in directions:
                                            print("\nOptions: north/south/east")
                                            userInput = input()
                                            if userInput in answer_n:
                                                gotoroom10()
                                            elif userInput in answer_e:
                                                gotoroom6()
                                            elif userInput in answer_s:
                                                gotoroom4()
                                            else:
                                                print("\nI can't do that.")
                                    else:
                                        print("\nI can't do that.")
                            else:
                                print("\nShe smiles at you once more."
                                      "\nCome back if you change your mind.")
                                userInput = ""
                                while userInput not in directions:
                                    print("\nOptions: north/south/east")
                                    userInput = input()
                                    if userInput in answer_n:
                                        gotoroom10()
                                    elif userInput in answer_e:
                                        gotoroom6()
                                    elif userInput in answer_s:
                                        gotoroom4()
                                    else:
                                        print("\nI can't do that.")
                        else:
                            print("\nI can't do that.")
                elif userInput in answer_no:
                    print("\nYou choose to stay away from her for now.")
                    userInput = ""
                    while userInput not in directions:
                        print("\nOptions: north/south/east")
                        userInput = input()
                        if userInput in answer_n:
                            gotoroom10()
                        elif userInput in answer_e:
                            gotoroom6()
                        elif userInput in answer_s:
                            gotoroom4()
                        else:
                            print("\nI can't do that.")
                else:
                    print("\nI can't do that.")
        else:
            print("\nWill you approach?")
            flags.add(5)
            userInput = ""
            while userInput not in decision:
                print("\nOptions: Yes/No")
                userInput = input()
                if userInput in answer_y:
                    print("\nYou cautiously approach the woman."
                          "\nShe smiles at you again, clearly trying to be friendly, but something about it sends chills down your spine..."
                          "\n'Greetings little one. Another come seeking the Fairy Tear, I assume?'"
                          "\nYou nod warily."
                          "\n'Well then, I'm happy to give it to you, but I will have to ask for something in exchange."
                          "\nNothing major, just a little bit of courtesy.'"
                          "\nShe smiles impossibly wider."
                          "\n'Simply give me your name.'")
                    print("\nWill you give her your name?")
                    userInput = ""
                    while userInput not in decision:
                        print("\nOptions: Yes/No")
                        userInput = input()
                        if userInput in answer_y:
                            print("I am Ser " + player_name + ", a knight of the kingdom.")
                            print(
                                "\nHer smile twists cruelly, as if laughing at a joke made at your expense."
                                "\n'Thank you Ser knight, and please do enjoy your prize.'")
                            print("\nYou blink, and she vanishes."
                                  "\nPeering ahead into the room she was guarding, you can't help but feel as though you have lost something...")
                            Backpack.remove(Amulet)
                            flags.remove(8)
                            flags.add(6)  # Fairy Queen dealt with
                            userInput = ""
                            while userInput not in directions:
                                print("\nOptions: north/south/east/west")
                                userInput = input()
                                if userInput in answer_n:
                                    gotoroom10()
                                elif userInput in answer_e:
                                    gotoroom6()
                                elif userInput in answer_s:
                                    gotoroom4()
                                elif userInput in answer_w:
                                    gotoroom8()
                                else:
                                    print("\nI can't do that")
                        elif userInput in answer_no:
                            print("\nShe shrugs."
                                  "\n'Then I cannot let you pass.'")
                            if "Rusty Sword" in player_belt:
                                print("\nFor a second, you see her eyes flicker to the sword on your belt.")
                                userInput = ""
                                while userInput not in decision:
                                    print("\nWill you draw your sword?"
                                          "\nOptions: Yes/No")
                                    userInput = input()
                                    if userInput in answer_y:
                                        print("\nYou pull out the Rusty Sword."
                                              "\nThe woman's eyes immediately flicker red, her beautiful face twisting into a monstrous visage."
                                              "\nHer entire body elongates with a cracking of bones, her fingertips now capped with gnarled claws."
                                              "\nShe lunges at you, her claws aimed straight at your eyes as you instinctively swing the dull blade."
                                              "\nIt passes through her body with shockingly little resistance."
                                              "\nHer form shudders like ripples on the surface of a disturbed pond before bursting into silvery mist, her final scream ringing in your ears."
                                              "\nYour hands shake as you tie the sword back onto to your belt."
                                              "\nYou are now free to explore the room beyond.")
                                        flags.add(6)  # Fairy Queen dealt with
                                        userInput = ""
                                        while userInput not in directions:
                                            print("\nOptions: north/south/east/west")
                                            userInput = input()
                                            if userInput in answer_n:
                                                gotoroom10()
                                            elif userInput in answer_e:
                                                gotoroom6()
                                            elif userInput in answer_s:
                                                gotoroom4()
                                            elif userInput in answer_w:
                                                gotoroom8()
                                            else:
                                                print("\nI can't do that")
                                    elif userInput in answer_no:
                                        print(
                                            "\nYou're not sure if violence is the answer, especially with such a poor weapon."
                                            "\nShe smiles at you once more."
                                            "\n'Come back if you change your mind.'")
                                        userInput = ""
                                        while userInput not in directions:
                                            print("\nOptions: north/south/east")
                                            userInput = input()
                                            if userInput in answer_n:
                                                gotoroom10()
                                            elif userInput in answer_e:
                                                gotoroom6()
                                            elif userInput in answer_s:
                                                gotoroom4()
                                            else:
                                                print("\nI can't do that.")
                                    else:
                                        print("\nI can't do that.")
                            else:
                                print("\nShe smiles at you once more."
                                      "\n'Come back if you change your mind.'")
                                userInput = ""
                                while userInput not in directions:
                                    print("\nOptions: north/south/east")
                                    userInput = input()
                                    if userInput in answer_n:
                                        gotoroom10()
                                    elif userInput in answer_e:
                                        gotoroom6()
                                    elif userInput in answer_s:
                                        gotoroom4()
                                    else:
                                        print("\nI can't do that.")
                        else:
                            print("\nI can't do that.")
                elif userInput in answer_no:
                    print("\nYou choose to stay away from her for now.")
                    userInput = ""
                    while userInput not in directions:
                        print("\nOptions: north/south/east")
                        userInput = input()
                        if userInput in answer_n:
                            gotoroom10()
                        elif userInput in answer_e:
                            gotoroom6()
                        elif userInput in answer_s:
                            gotoroom4()
                        else:
                            print("\nI can't do that.")
                else:
                    print("\nI can't do that.")
    else:
        userInput = ""
        while userInput not in directions:
            print("\nOptions: north/south/east/west")
            userInput = input()
            if userInput in answer_n:
                gotoroom10()
            elif userInput in answer_e:
                gotoroom6()
            elif userInput in answer_s:
                gotoroom4()
            elif userInput in answer_w:
                gotoroom8()
            else:
                print("\nI can't do that")


def gotoroom8():
    print("\nThis floor of this room is covered in large flowers; each with five silver petals shaped like raindrops.")
    print("\nThe air is filled with their sweet scent.")
    if "Fairy Tear" in Backpack:
        print("\nYou already have what you need.")
    else:
        print("\nYou've found the Fairy Tear!")
        print("\nYou pick one of the flowers and put it in your Backpack.")
        Backpack.append("Fairy Tear")
        flags.add(7)  # Needed to trigger endings A & B
    userInput = ""
    while userInput not in directions:
        print("\nOptions: east")
        userInput = input()
        if userInput in answer_e:
            gotoroom7()
        else:
            print("\nI can't do that.")


def gotoroom9():
    if "Rusty Sword" in player_belt:
        print("\nThere's nothing else here.")
    else:
        print("\nAn ancient sword, caked in rust has been stabbed into the floor at the centre of this room.")
        print("\nIt's no good for combat, but you have no other options...")
        print("\nYou put the Rusty Sword on your belt.")
        player_belt.append("Rusty Sword")  # Used for Fairy Queen encounter (optional)
    userInput = ""
    while userInput not in directions:
        print("\nOptions: north/south")
        userInput = input()
        if userInput in answer_n:
            gotoroom12()
        elif userInput in answer_s:
            gotoroom6()
        else:
            print("\nI can't do that.")


def gotoroom10():
    print("\nThere is a well sitting in the middle of this room.")  # Can be used to restore the amulet if name given to Fairy Queen
    print('\nA sign attached to the side reads "To reclaim what was lost, toss a coin and make a wish".')
    if Amulet in Backpack:
        print("\nNothing I need to do here.")
        userInput = ""
        while userInput not in directions:
            print("\nOptions: south/west")
            userInput = input()
            if userInput in answer_s:
                gotoroom7()
            elif userInput in answer_w:
                gotoroom11()
            else:
                print("\nI can't do that.")
    else:
        print("\nYour mind immediately goes to the fey woman, and the feeling of loss that followed.")
        if "Gold Coin" in Backpack:  # Gained from Sphinx puzzle
            print("\nWould you like to toss a coin in the well?")
            userInput = ""
            while userInput not in decision:
                print("\nOptions: Yes/No")
                userInput = input()
                if userInput in answer_y:
                    print("\nYou toss the coin in the well."
                          "\nYou feel a familiar weight settle in your Backpack."
                          "\nYou feel restored.")
                    Backpack.append(Amulet)
                    flags.add(8)
                    userInput = ""
                    while userInput not in directions:
                        print("\nOptions: south/west")
                        userInput = input()
                        if userInput in answer_s:
                            gotoroom7()
                        elif userInput in answer_w:
                            gotoroom11()
                        else:
                            print("\nI can't do that.")
                elif userInput in answer_no:
                    print("\nMore fey magic is probably not the answer."
                          "\nYou decide not to use the well.")
                    userInput = ""
                    while userInput not in directions:
                        print("\nOptions: south/west")
                        userInput = input()
                        if userInput in answer_s:
                            gotoroom7()
                        elif userInput in answer_w:
                            gotoroom11()
                        else:
                            print("\nI can't do that.")
                else:
                    print("\nI can't do that.")
        else:
            print("\nI don't have a coin to throw.")
            userInput = ""
            while userInput not in directions:
                print("\nOptions: south/west")
                userInput = input()
                if userInput in answer_s:
                    gotoroom7()
                elif userInput in answer_w:
                    gotoroom11()
                else:
                    print("I can't do that.")


def gotoroom11():
    print("\nA gate, shining silver with a lock in it's centre, covers the archway in the north of this room.")
    print("\nYou can see light coming from beyond the archway.")
    if 9 not in flags:
        if "Silver Key" in Backpack:
            print("\nYou unlock the gate with the silver key.")
            flags.add(9)
            userInput = ""
            while userInput not in directions:
                print("\nOptions: east/exit")
                userInput = input()
                if userInput in answer_e:
                    gotoroom10()
                elif userInput in win_game:
                    victory()
                else:
                    print("\nI can't do that")
        else:
            print("\nI need a key to open this.")
            userInput = ""
            while userInput not in directions:
                print("\nOptions: east")
                userInput = input()
                if userInput in answer_e:
                    gotoroom10()
                else:
                    print("\nI can't do that")
    else:
        print("\nThe gate is open."
              "\nI can leave now.")
        userInput = ""
        while userInput not in directions:
            print("\nOptions: east/exit")
            userInput = input()
            if userInput in answer_e:
                gotoroom10()
            elif userInput in win_game:
                victory()
            else:
                print("\nI can't do that")


def gotoroom12():
    print("\nThere is a large hook set into the east wall of this room.")
    if "Silver Key" in Backpack:
        print("\nThere's nothing else here.")
    else:
        print("\nThere is a key hanging on the hook.")
        print("\nYou take the key and put it in your Backpack.")
        Backpack.append("Silver Key")  # Needed to unlock Silver Gate
    userInput = ""
    while userInput not in directions:
        print("\nOptions: south/west")
        userInput = input()
        if userInput in answer_s:
            gotoroom9()
        elif userInput in answer_w:
            gotoroom13()
        else:
            print("I can't do that.")


def gotoroom13():
    print("\nA gate, glittering gold with a lock in it's centre, covers the archway in the west of this room.")
    print("\nYou can see light coming from beyond the archway.")
    if 10 not in flags:
        if "Gold Key" in Backpack:
            print("\nYou unlock the gate with the gold key.")
            flags.add(10)
            userInput = ""
            while userInput not in directions:
                print("\nOptions: east/exit")
                userInput = input()
                if userInput in answer_e:
                    gotoroom10()
                elif userInput in win_game:
                    victory()
                else:
                    print("\nI can't do that")
        else:
            print("\nI need a key to open this")
            userInput = ""
            while userInput not in directions:
                print("\nOptions: east")
                userInput = input()
                if userInput in answer_e:
                    gotoroom12()
                else:
                    print("\nI can't do that")
    else:
        print("\nThe gate is open."
              "\nI can leave now.")
        userInput = ""
        while userInput not in directions:
            print("\nOptions: east")
            userInput = input()
            if userInput in answer_e:
                gotoroom12()
            else:
                print("\nI can't do that")


def victory():
    print("\nYou stumble out of the passage, blinking in the sudden sunlight."
          "\nA low rumble comes from behind you, and you turn back you see the exit disappearing;"
          "\nThe hole is quickly covered by earth, then grass, now nothing more than an unassuming hillock.")
    if "Fairy Tear" in Backpack and Amulet in Backpack:
        print("\nYou swiftly pull your backpack open, letting out a sigh of relief as you see the silver petals peeking out."
              "\nWith the Fairy Tear in hand, you quickly set off back towards the castle and the ailing queen."
              "\nAt last, your quest for a cure is over.")
        print("\nYou got Ending A: The Triumphant Hero.")  # Best ending
    elif "Fairy Tear" in Backpack and Amulet not in Backpack:
        print("\nYou swiftly pull your backpack open, letting out a sigh of relief as you see the silver petals peeking out."
              "\nYou then freeze: what did you need this for again? Where are you? WHO are you?"
              "\nLooking around, you spot the spires of a castle off in the distance, the sight evoking a faint sense of familiarity in the back of your mind."
              "\nYou feel as if there is a connection between this castle and the flower you are carrying."
              "\nWith no other options, you set off towards the spires, not knowing your quest was a success... but at what cost?")
        print("\nYou got Ending B: The Devil's Bargain.")  # Neutral ending
    elif "Fairy Tear" not in Backpack and Amulet in Backpack:
        print("\nYour stomach sinks, somehow knowing that you will not find your way back into the Great Labyrinth."
              "\nSlowly, you turn and start trudging back towards the castle, heart as heavy as your footsteps."
              "\nBut wait; just because you have failed, that doesn't mean all hope is lost!"
              "\nPerhaps another knight, armed with the knowledge you carry could enter instead, with a better chance of success!"
              "\nDetermined, you set off towards the castle with haste, knowing that time is of the essence.")
        print("\nYou got Ending C: Keep Hope Alive.")  # Neutral ending
    elif "Fairy Tear" not in Backpack and Amulet not in Backpack:
        print("\nGlancing around in confusion, you suddenly realise, you have no idea where you are, or how you got here."
              "\nWait, who are you? Why can't you remember?"
              "\n'Excuse me', a gentle voice calls out to you."
              "\nYou turn to see an oddly familiar woman standing before you, a kind smile on her beautiful face."
              "\n'We meet again, Ser knight. You seem lost. Perhaps I can help?'"
              "\nYou nod mutely, seeing your hand reach out to grab hers, as if watching yourself from far away."
              "\n'Worry not, good Ser'; her words tinkle like wind chimes in your head."
              "\n'We will take very good care of you.'"
              "\nShe gently tugs at your hand, leading you deep, deep, deeper into the forest, never to be seen again.")
        print("\nYou got Ending D: The Lost Knight.")  # Bad ending


def introScene():
    print(
        "\nAs you step into the maze from the forest that surrounds it, the entrance snaps shut behind you"
        "\nIt looks like you'll need to find another exit.")
    print(
        "\nYou are in a dark room, with only the light of your torch to guide you. There are three hallways leading in different directions. "
        "\nWhere would you like to go?")
    start()


print("Welcome to the Great Labyrinth!")
print("\nYou, the greatest knight of the kingdom, have come seeking a cure for the ailing queen: \nThe mysterious FAIRY TEAR.")
print("\nYour goal is to obtain it, and then find your way out"
      "\nBut beware: unseen dangers lurk in the labyrinth, and it's up to you and your wits to overcome them.")
print("\nLet's start with your name: ")
player_name = input()
Amulet = ("A pendant with" + player_name + "written on it")
Backpack.append(Amulet)
print('\nGood luck, Ser ' + player_name + ".")
introScene()
