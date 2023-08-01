name = input('What is your name? ')
print('Welcome', name+'! You are about to begin an adventure.')

answer = input('You are on a dirt road. You come to a fork in the road, do you want to go left or right?(left/right) ').lower()

if answer == 'left':
    question2 = input('''You see a sign jutting from the ground. Upon inspection it asks you a simple question, "Have you seen the boy in the woods?(yes/no)" ''').lower()
    if question2 == 'no':
        print('''Well that was uneventful. A goblin walks over, clobbers you on the head and throws you over his shoulder. A wizened old man walks beside him and speaks sympathetically to the goblin, "Maybe the next one lad". They disappear into the distance. Goodbye traveler.''')
    elif question2 == 'yes':
        print('''
A small doll to your left pops to life. "You say you\'ve seen the boy?" The doll sqeaks "You know him well? Perfect! Come follow me!" Before you get a word in the doll grips your hand and pulls you along with her.''')
        question3 = input('You come to a hill in a forest. The doll asks you if you\'d dance with her. Do you dance?(yes/no): ').lower()
        if question3 == 'yes':
            question4 = input('As you dance you hear a rhythm build in your head. It moves your body, swaying you. Your feet begin to step in a pattern. Lights glow on the ground, first dimply, then bright, until you find yourself to be on a ship. The doll is no longer a doll but a tall, slender alien with long wiry limbs. "It\'s good to see you again dear, how long has it been? Anyways, now that you\'re back, shall we play a game?" The alien gestures to a board that looks to be a game you once learned. Memories resurface, this is your sister. You look back to the board. Do you play?(yes/no) ').lower()
            if question4 =='yes':
                question5 = input('As you sit to play you seem to remember that you aren\'t very good at this game. Your sister always seemed to get the better of you. In fact... you kind of dislike your sister. She\'s stuck up, pompous, and childish. Mom and Dad used to give her everything. Do you confront her about this?(yes/no) ').lower()
                if question5 == 'yes':
                    print('"So... Why is it you came all the way out here to meet me?" "Oh I just missed my sibling! Isn\'t that enough?" A menacing grin spreads on her face. You feel a tingling in your hand. "What have you done?!" Your body goes limp and your vision begins to dim. "Silly little', name, 'Mom and Dad will not be happy to see you again!" The last thing you see is her boot on the table resting just next to your face. Well that\'s it! Thanks for the adventure! Maybe choose a different path next time.')
                elif question5 == 'no':
                    question6 = input('Before speaking you sense something amiss. You think to yourself "Why would she come out here to see me? What is she playing at?" you notice a slight glimmer on the pieces of the game. "Poison?" You get up and say. "I\'m thirsty, anything to drink around here? You notice irritation run across her face, she quickly rearranges it with a smile. "Absolutley, down the hall and to the left. You\'ll find beverages in the closet". You make your way down the hall and out of sight. There is a closet on the left hand side and a door on the right. Do you go left or right?(left/right) ').lower()
                    if question6 == 'right':
                        print('You open the door and find a small closet, just big enonugh to fit into. You see a slight glimmer of light at the edge of the closet. You push the back wall. It swings open like a door. You see a stone floor before you. You step through. Above you is a shield embossed with 4 figures, a raven, snake, lion, and badger. You see to your left a crowd of people filing out of rooms, chatter fills the hall. Everyone\'s dressed in robes. You look down at yourself. You\'re dressed in robes! You pat yourself down and find a long stick in your pocket. The tip of it flickers with a dim light as you hold it. A bell rings. Better get to class bucko!        Congratulations! You have completed the adventure set before you. You are now a witch/wizard of Hogwarts castle. You get the honour of training under one of hogwarts greatest headmasters to ever live. Albus Dumbledore. Now hurry off, class has started.')
                    elif question6 == 'left':
                        print('You find a closet full of beverages. You choose one and walk back to the room. You decide it\'s crazy to consider your sister poisoning you. You begin playing the game. You feel faint, you go unconscious. Sorry adventurer! Your time is up. Thanks for playing!')
                    else:
                        print('Invalid response. Maybe next time you\'ll answer the question properly. Byebye!')
                else:
                    print('Wrong answer bucko! You lose!')
            elif question4 == 'no':
                print('"Oh you\'re  no fun at all!" Sister says. "Fine! Be that way! I don\'t wanna play either!" You feel a strong wind lift you from the ground and blow you out the window. You plummet to the earth. A small boy sees a figure falling through the sky. "Mom look! Someone just fell from a cloud!". "That\'s nice sweetie.". Seems that your adventure is up. Thanks for playing!')
            else:
                print('Invalid anwer. You are swept from the ship and given a reprimand by the Voice of God!')
        elif question3 == 'no':
            print('The doll begins to dance and as she does so her body begins to dim until she is nothing but air. As if she was never there. You hear a voice on the wind. "Maybe next time!". You are left alone in the woods. The adventure cut short. Thanks for playing!')
        else:
            print('Invalid answer. The doll doesn\'t appreciate what you\'ve said. She swiftly parts you from your head.')
    else:
        print('"Invalid response." Booms a voice above you. You see the clouds part, a hand the size of a mountain swoops down. Darkness engulfs you.')



elif answer == 'right':
    print('You walk a long winding path. It\'s quite beautiful out. You hear birds singing and feel a warm breeze on your face. All seems well and good except for that incessant gnawing you\'ve felt ever since turning right. Almost as if you had missed a great opportunity. Ah well, must\'ve been something you ate.')
    print('Well, unfortunately your adventure has been cut short. You chose, unbeknownst to you, the easy and comfortable path. While it does have it\'s upsides it is rarely fulfilling. But at least your safe right? Hmmmm maybe that\'s not quite worth it. Perhaps you should reincarnate and pick a different path. Just a thought.')
else:
    print('''
          Not a valid answer. You lose sucka! HaAHAHAHAahahahaHAHAHaHahahaHahahhahHAHAHAhaAHAA... A mist appears to your right. There shrouded in darkness is void, it pulls you in. A sharp sensation stings your spine. You merge with darkness. Goodbye traveler, should've chosen left or right.''')
