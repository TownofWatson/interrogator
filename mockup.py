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
        print("* able to identify this person as Brad Vanderbilt and he was brought in*")
        print("* for questioning. Brutus's roommate, Todd Washington, was also brought*")
        print("* in for questioning.                                                  *")
        print("*                                                                      *")
        print("* Evidence:                                                            *")
        print("*    -Two sets of footprints in the snow around the body               *")
        print("*    -Disturbed snow makes it appear there was a fight                 *")
        print("*                                                                      *")
        print("* You currently have 2 suspects for this case:                         *")
        print("*     -Brad Vanderbilt (Suspect who was fleeing from the scene)        *")
        print("*     -Todd Washington  (Brutus's roommate)                            *")
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
        print("   -Brad Vanderbilt")
        print("   -Todd Washington")
        inputName = input('')
        while(inputName=="Brad Vanderbilt"):
            print("\n" * 100)
            print("You are now talking to Brad Vanderbilt.")
            #This is where the talking goes on
            print("Press 'S' to stop talking to Brad Vanderbilt")
            input1 = input('')
            if (input1=='S'):
                inputName="Stop"
        while(inputName=="Todd Washington"):
            print("\n" * 100)
            print("You are now talking to Todd Washington")
            #This is where the talking goes on
            print("Press 'S' to stop talking to Todd Washington")
            input1 = input('')
            if (input1=='S'):
                inputName="Stop"

    while(input1=='E'):
        print("\n" * 100)
        print("The interrogation is over.")
        print("Who do you think committed the murder?")
        inputGuess = input('')
        if(inputGuess=="Todd Washington"):
            print("You are correct! Good job!")
            input1='Q'
        if(inputGuess=="Brad Vanderbilt"):
            print("You got it wrong. You are a failure.")
            input1='Q'
