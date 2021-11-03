# importing the rotors, reflectors and plugboard file
from rotor import *
from plugboard import *


class Enigma:

    def __init__(self, rotors, reflector, msg):
        self.rotors = rotors
        self.reflector = reflector
        # constructer to take the msg from the plugboard class
        self.encoded_msg = msg.new_msg
        self.cipher = str()

    # Encodes a Message

    def encode(self, msg):
        # set rotor rotations to 0
        self.rotor1_rotation = 0
        self.rotor2_rotation = 0
        self.rotor3_rotation = 0

        # take input from user
        for i in range(len(self.encoded_msg)):
            # return any character that is not an alphabetic nor a num as is
            if not self.encoded_msg[i].isalnum():
                self.cipher += self.encoded_msg[i]

            else:
                # rotate the rotors after every letter
                self.rotation()

                # take the index of the first letter of the msg in the alphabet list
                index = alphabet.index(self.encoded_msg[i])
                # correspond it to the letter in the first rotor
                encrypted = rotors[0][index]

                # change the index to the coresponding letter in the alphabet list
                index = alphabet.index(encrypted)
                # correspond it to the letter in the second rotor
                encrypted = rotors[1][index]

                index = alphabet.index(encrypted)
                # correspond it to the letter in the third rotor
                encrypted = rotors[2][index]

                index = alphabet.index(encrypted)
                # correspond it to the letter in the reflector
                encrypted = reflectorB[index]

                # check the mapping of the letter in the reflection
                for x in reflectorB_map:
                    if x[0] == encrypted:
                        encrypted = x[1]

                    elif x[1] == encrypted:
                        encrypted = x[0]

                # change the index to the coresponding letter in the refelector list
                index = reflectorB.index(encrypted)
                # correspond it to the letter in the alphabet
                encrypted = alphabet[index]

                # change the index to the coresponding letter in the third rotor
                index = rotors[2].index(encrypted)
                # correspond it to the letter in the second rotor
                encrypted = rotors[2][index]
                # correspond it to the letter in the alphabet list
                encrypted = alphabet[index]

                index = rotors[1].index(encrypted)
                encrypted = rotors[1][index]
                encrypted = alphabet[index]

                index = rotors[0].index(encrypted)
                encrypted = rotors[0][index]
                encrypted = alphabet[index]

                # adds letter by letter to the encoded msg
                self.cipher += encrypted

    def rotation(self):
        # rotation of rotor1
        Rotors.rotate(0)

        # incriminate after each letter in rotor1
        self.rotor1_rotation += 1

        # rotate rotor2 after full rotation of rotor1
        if self.rotor1_rotation == 60:
            Rotors.rotate(1)
            # reset the inrimintation
            self.rotor1_rotation = 0
            # incriminate after each letter in rotor2
            self.rotor2_rotation += 1

        # rotate rotor3 after full rotation of rotor2
        if self.rotor2_rotation == 60:
            self.rotor2_rotation = 0
            Rotors.rotate(2)

    def decode(self):
        self.encode(msg)

    # returns encoded msg
    def get_ciphered_msg(self):
        return self.cipher

    # returns dencoded msg
    def get_deciphered_msg(self):
        return self.cipher


class Plugboard:
    # pass through plug board
    def __init__(self, plugboard_chosen, new_msg):
        self.plugboard_chosen = plugboard_chosen
        self.new_msg = new_msg

    # if the user does not want to use a plugboard
    def plugboard_default(self, msg):
        # pass the msg with no changes
        self.new_msg = msg

    # user chooses from 3 plugboards
    def plugboard_choice(self, plugboard_chosen):
        plugboard = INTvalidation(
            'choose your plugboard (29, 30, 31): ')
        while plugboard not in range(29, 32):
            print("\nYou can enter from 29 to 31 ONLY.")
            plugboard = INTvalidation(
                'choose your plugboard (29, 30, 31): ')
            if plugboard == 29:
                self.plugboard_chosen = plugboard29
            elif plugboard == 30:
                self.plugboard_chosen = plugboard30
            elif plugboard == 31:
                self.plugboard_chosen = plugboard31
            else:
                print("invalid choice")

    # user configures their own plugboard
    def plugboard_configure(self):
        user_plugboard = []

        count = INTvalidation(
            "How many pairings will you configure? ")

        for i in range(count):
            x = input('Enter first pair: ')  # '(a,b),(b,c),(c,d),(d,e)'

            for tup in x.split('),('):
                # tup looks like `(a,a` or `b,b`
                tup = tup.replace(')', '').replace('(', '')
                # tup looks like `a,a` or `b,b`
                user_plugboard.append(tuple(tup.split(',')))

        self.plugboard_chosen = user_plugboard

    # pairing function
    def plugboard_settings(self, msg):
        # convert the msg characters to a list
        list_msg = list(msg)

        for i in range(len(msg)):
            for x in self.plugboard_chosen:
                # swap the character with it's pairing
                if list_msg[i] == x[0]:
                    list_msg[i] = x[1]
                elif list_msg[i] == x[1]:
                    list_msg[i] = x[0]
            self.new_msg = "".join(list_msg)

    def get_new_msg(self):
        return self.new_msg


class Rotors:

    def __init__(self, rotors, first_rotor, mid_rotor, last_rotor):
        self.first_rotor = first_rotor
        self.mid_rotor = mid_rotor
        self.last_rotor = last_rotor
        self.rotors = rotors

    # orders the rotors based on user input
    def rotor_order(self, rotors, rotor):
        if rotor == 1:
            rotors.append(rotorI)
        elif rotor == 2:
            rotors.append(rotorII)
        elif rotor == 3:
            rotors.append(rotorIII)
        elif rotor == 4:
            rotors.append(rotorIV)
        else:
            print("choice is invalid")

    def starting_point(self, rotors, r1, r2, r3):

        # take user input for the starting letter in the first rotor
        r1 = input(
            'Enter the first letter for the starting point: ')

        # validation if char not in list
        while r1 not in rotors[0]:
            print("Enter any alphabet characet or a number form 0-9 ONLY.")
            r1 = input(
                'Enter the first letter for the starting point: ')
        # change the letter to its index
        starting_letter = rotors[0].index(r1)

        # rotate the first rotor to the starting point
        for i in range(starting_letter):
            rotors[0].append(rotors[0].pop(0))

        r2 = input(
            'Enter the second letter for the starting point: ')

        while r2 not in rotors[1]:
            print("Enter any alphabet characet or a number form 0-9 ONLY.")
            r2 = input(
                'Enter the first letter for the starting point: ')

        starting_letter = rotors[1].index(r2)

        # rotate the second rotor to the starting point
        for i in range(starting_letter):
            rotors[1].append(rotors[1].pop(0))

        r3 = input(
            'Enter the third letter for the starting point: ')
        starting_letter = rotors[2].index(r3)

        while r3 not in rotors[2]:
            print("Enter any alphabet characet or a number form 0-9 ONLY.")
            r3 = input(
                'Enter the first letter for the starting point: ')

        for i in range(starting_letter):
            # rotate the third rotor to the starting point
            rotors[2].append(rotors[2].pop(0))

    def rotate(index):
        # rotation of rotors function
        rotors[index].append(rotors[index].pop(0))

    #  function to reset rotors to their original state

    def reset(self):

        # rotate first rotor till the first index is E
        while rotorI[0] != 'E':
            rotorI.append(rotorI.pop(0))

        # rotate second rotor till the first index is A
        while rotorII[0] != 'A':
            rotorII.append(rotorII.pop(0))

        # rotate third rotor till the first index is B
        while rotorIII[0] != 'B':
            rotorIII.append(rotorIII.pop(0))

        # rotate fourth rotor till the first index is E
        while rotorIV[0] != 'E':
            rotorIV.append(rotorIV.pop(0))


class Reflector:

    def __init__(self, reflector):
        self.reflector = reflector

# validation for integer inputs


def INTvalidation(msg):
    while True:
        try:
            Input_int = int(input(msg))

        except ValueError:
            print("\nInvalid, answer should be in numbers.")
            continue
        else:
            return Input_int


rotors = list()
plugboard_chosen = int()
new_msg = str()
first_rotor = ""
mid_rotor = ""
last_rotor = ""

Rotor_class = Rotors(rotors, first_rotor, mid_rotor, last_rotor)
Plugboard_class = Plugboard(plugboard_chosen, new_msg)


print("This is an enigma machine, please select what you need to do by inserting the corresponding number")

selection = 0
while(selection != 3):
    print("\n1: Encode a Message ")
    print("2: Decode a Message ")
    print("3: Exit the program \n")

    selection = INTvalidation("\nEnter your selection: ")
    if selection == 1 or 2:

        Rotor_class.reset()
        while rotors == []:
            # take user input to choose the first rotor
            first_rotor = INTvalidation('choose 1st rotor (ex: I): ')
            Rotor_class.rotor_order(rotors, first_rotor)

            # take user input to choose the second rotor
            mid_rotor = INTvalidation('choose 2nd rotor (ex: I): ')
            Rotor_class.rotor_order(rotors, mid_rotor)

            # take user input to choose the third rotor
            last_rotor = INTvalidation('choose 3rd rotor (ex: I): ')
            Rotor_class.rotor_order(rotors, last_rotor)

            for elem in rotors:
                if rotors.count(elem) > 1:
                    rotors = []
                    print("\nRotors can't be chosen twice. Please try again.")
                    break

        Rotor_class.starting_point(rotors, rotors[0], rotors[1], rotors[2])

        x = input("Do you want to use a plugboard? ")
        if x == "Y":
            print("\n1: Choose a preset plugboard ")
            print("2: Configure a plugboard\n")

            ans = INTvalidation("Choose one from the above: ")
            while ans not in range(1, 3):
                print("\nYou can enter from 3 to 6 modules ONLY.")
                ans = INTvalidation("Choose one from the above: ")

            if ans == 1:
                Plugboard_class.plugboard_choice(plugboard_chosen)
                msg = input("Enter your Message: ")

                Plugboard_class.plugboard_settings(msg)
                Enigma_mahcine = Enigma(
                    rotors, reflectorB, Plugboard_class)

                Enigma_mahcine.encode(msg)
                cipher = Enigma_mahcine.get_ciphered_msg()
                Plugboard_class.plugboard_settings(cipher)

                print(Plugboard_class.get_new_msg())

            elif ans == 2:
                Plugboard_class.plugboard_configure()
                msg = input("Enter your Message: ")

                Plugboard_class.plugboard_settings(msg)
                Enigma_mahcine = Enigma(
                    rotors, reflectorB, Plugboard_class)

                Enigma_mahcine.encode(msg)

                cipher = Enigma_mahcine.get_ciphered_msg()
                Plugboard_class.plugboard_settings(cipher)

                print(Plugboard_class.get_new_msg())

        else:

            msg = input("Enter your Message: ")

            Plugboard_class.plugboard_default(msg)
            Enigma_mahcine = Enigma(rotors, reflectorB, Plugboard_class)

            Enigma_mahcine.encode(msg)
            print(Enigma_mahcine.get_ciphered_msg())

            # print(rotors[0], "\n")
            # print(rotors[1], "\n")
            # print(rotors[2], "\n")
    elif selection == 3:
        quit()
