print("\n" * 100)
print("\nWelcome to the Interrogator Game\n")
print("You are an investigator in charge of finding out who committed a murder. ")
print("Your notepad contains the case file, list of suspects, and any notes you would like to take.")
print("Press 'N' to bring up your notepad.")
input1 = input('')

while(input1!='Q'):
    while(input1=='N'):
        print("************************************************************************")
        print("* Date/Time:                                                           *")
        print("* Saturday January 13, 2018 at approximately 2:14 am                   *")
        print("*                                                                      *")
        print("* Location:                                                            *")
        print("* 341 E 15th Avenue                                                    *")
        print("* Columbus, OH 43201                                                   *")
        print("*                                                                      *")
        print("* Description:                                                         *")
        print("* Brutus Buckeye, a 23-year-old male, was found outside his apartment  *")
        print("* with a gunshot wound to the head on Saturday night. A bystander      *")
        print("* called in to the police station to report hearing gunshots and seeing*")
        print("* someone in a blue and maize sweatshirt run from the area. Police were*")
        print("* able to identify this person ad bring him in for questioning.        *")
        print("* Brutus's roommate was also brought in for questioning                *")
        print("*                                                                      *")
        print("* Evidence:                                                            *")
        print("*    -Two sets of footprints in the snow around the body               *")
        print("*    -Disturbed snow makes it appear there was a fight                 *")
        print("*                                                                      *")
        print("* You currently have 2 suspects for this case:                         *")
        print("*     -Brad (Suspect who was fleeing from the scene)                   *")
        print("*     -Todd (Brutus's roommate)                                        *")
        print("*                                                                      *")
        print("* Your Notes:                                                          *")
        print("*     -                                                                *")
        print("*                                                                      *")
        #print("* Press 'E' to edit your notes                                         *")
        #Edit does not work right now
        print("* Press 'C' to close your notepad                                      *")
        input1 = input('')

    while((input1=='C') or (input1=='S') or (input1=='D')):
        print("\n" * 100)
        print("Press 'N' to bring up your notepad.")
        print("Press 'I' to interrogate a suspect.")
        print("Press 'E' to end interrogation.")
        input1 = input('')

    while(input1=='I'):
        print("Who would you like to interrogate?")
        print("   -Brad")
        print("   -Todd")
        inputName = input('')
        while(inputName=="Brad"):
            print("\n" * 100)
            print("You are now talking to Brad.")
            print("Press 'S' to stop talking to Brad")
            print("Press 'W' to talk to Watson\n")

            print("You see a disheveled, young man in a grey hoodie and sweatpants. As you walk in, he looks up nervously. Ask questions to figure out who murdered Brutus!\n")
            inputQuestion = input('')
            print("\nBrad: I-I was o-out… hanging out with friends. We went to watch S-star Wars at Gateway.\n")
            inputQuestion = input('')
            print("\nBrad: Maybe from 8-11:30? We all w-went home afterwards.\n")
            inputQuestion = input('')
            print("\nBrad: Y-yes! It was terrifying! I saw two people on the street f-fighting and yelling and all of a sudden, one of them pulls out a gun and shoots the other g-guy in the head!\n")
            inputQuestion = input('')
            print("\nBrad: Well, after that, I-I walked up to the guy to see if he was okay, but then p-police sirens came. I was so s-scared, I ran! But I swear, I didn’t do it!\n")
            inputQuestion = input('')
            print("\nBrad: I c-couldn’t see too well, but he looked kind of preppy?\n")
            inputQuestion = input('')
            print("\nBrad: W-well… no. No one walked home with me.\n")
            input1 = input('')
            if (input1=='S'):
                inputName="Stop"


        while(inputName=="Todd"):
            print("\n" * 100)
            print("You are now talking to Todd")
            print("Press 'S' to stop talking to Todd")
            print("Press 'W' to talk to Watson\n")


            print("In the other interrogation room, you see a young man with gelled up hair, wearing a sweater vest, khaki pants and a pair of Vans. Ask questions to figure out who murdered Brutus!\n")
            inputQuestion = input('')
            print("\nTodd: Saturday? I was at home catching up on the latest Game of Thrones season. I stayed home all night.\n")
            inputQuestion = input('')
            print("\nTodd: No. Brutus left the house earlier.\n")
            inputQuestion = input('')
            print("\nTodd: Definitely not. Can I go now?\n")
            inputQuestion = input('')
            print("\nWatson: One set of sneakers, men’s size 11 and a set of Vans, men’s size 4.\n")
            inputQuestion = input('')
            print("\nTodd: Yeah, it’s a genetic thing. Probably like a 4 or a 4.5? Why?\n")
            inputQuestion = input('')
            print("\nTodd: O-oh! I forgot. I did go outside to uh… give Brutus his keys.\n")
            inputQuestion = input('')
            print("\nWatson: No keys were found on the body.\n")
            inputQuestion = input('')
            print("\nTodd: Look, alright. Stop asking me questions! Obviously that other person did it. You’re wasting time here!\n")
            input1 = input('')
            if (input1=='S'):
                inputName="Stop"

    while(input1=='E'):
        print("\n" * 100)
        print("The interrogation is over.")
        print("Who do you think committed the murder?")
        print("   -Brad")
        print("   -Todd\n")
        inputGuess = input('')
        if(inputGuess=="Todd"):
            print("You are correct! Good job!\n")
        if(inputGuess=="Brad"):
            print("You got it wrong. You are a failure.\n")
        print("As it turns out, Brutus made too much fun of Todd’s small shoe size and one day, Todd couldn’t take it anymore. How ironic that Todd’s shoe size ended up being his downfall.")
        input1='Q'