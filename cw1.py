# importing the rotors, reflectors and plugboard file
from rotor import *
from plugboard import *


class Enigma:

    def __init__(self, rotors, reflector, msg):
        self.rotors = rotors
        self.reflector = reflector
        self.encoded_msg = msg.new_msg
        self.cipher = str()
        # self.plugboard = plugboarD

    # Encodes a Message
    def encode(self, msg):
        # define variables
        # self.encoded_msg = ""

        self.rotor1_rotation = 0
        self.rotor2_rotation = 0

        # take input from user
        for i in range(len(self.encoded_msg)):
            # return the space as is
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

    def plugboard_choice(self, plugboard_chosen):
        plugboard = int(input('choose your plugboard (29, 30, 31): '))
        if plugboard == 29:
            self.plugboard_chosen = plugboard29
        elif plugboard == 30:
            self.plugboard_chosen = plugboard30
        elif plugboard == 31:
            self.plugboard_chosen = plugboard31
        else:
            print("invalid choice")

    def plugboard_configure(self):
        user_plugboard = []

        count = int(input(
            "How many pairings will you configure (limit: 10 pairs)? "))

        for i in range(count):
            x = input('Enter first pair: ')  # '(a,a),(b,b),(c,c),(d,d)'

            for tup in x.split('),('):
                # tup looks like `(a,a` or `b,b`
                tup = tup.replace(')', '').replace('(', '')
                # tup looks like `a,a` or `b,b`
                user_plugboard.append(tuple(tup.split(',')))

        self.plugboard_chosen = user_plugboard

    def plugboard_default(self, msg):
        self.new_msg = msg

    def plugboard_settings(self, msg):
        list_msg = list(msg)
        for i in range(len(msg)):
            for x in self.plugboard_chosen:
                if list_msg[i] == x[0]:
                    list_msg[i] = x[1]
                elif list_msg[i] == x[1]:
                    list_msg[i] = x[0]
            self.new_msg = "".join(list_msg)

    def get_new_msg(self):
        return self.new_msg


class Rotors:

    def __init__(self, rotors):
        self.first_rotor = ""
        self.mid_rotor = ""
        self.last_rotor = ""
        self.rotors = rotors

    def rotor_order(self, rotors):

        # take user input to choose the first rotor
        first_rotor = input('choose 1st rotor (ex: I): ')
        if first_rotor == 'I':
            rotors.append(rotorI)
        elif first_rotor == 'II':
            rotors.append(rotorII)
        elif first_rotor == 'III':
            rotors.append(rotorIII)
        elif first_rotor == 'IV':
            rotors.append(rotorIV)
        else:
            print("choice is invalid")

        # take user input to choose the second rotor
        second_rotor = input('choose 2nd rotor (ex: I): ')
        if second_rotor == 'I':
            rotors.append(rotorI)
        elif second_rotor == 'II':
            rotors.append(rotorII)
        elif second_rotor == 'III':
            rotors.append(rotorIII)
        elif second_rotor == 'IV':
            rotors.append(rotorIV)
        else:
            print("choice is invalid")

        # take user input to choose the third rotor
        third_rotor = input('choose 3rd rotor (ex: I): ')
        if third_rotor == 'I':
            rotors.append(rotorI)
        elif third_rotor == 'II':
            rotors.append(rotorII)
        elif third_rotor == 'III':
            rotors.append(rotorIII)
        elif third_rotor == 'IV':
            rotors.append(rotorIV)
        else:
            print("choice is invalid")

    def starting_point(self, rotors, first_rotor, second_rotor, last_rotor):

        # take user input for the starting letter in the first rotor
        r1 = input(
            'Enter the first letter for the starting point: ')
        # change the letter to its index
        starting_letter = rotors[0].index(r1)

        # rotate the first rotor to the starting point
        for i in range(starting_letter):
            rotors[0].append(rotors[0].pop(0))

        r2 = input(
            'Enter the second letter for the starting point: ')

        starting_letter = rotors[1].index(r2)

        # rotate the second rotor to the starting point
        for i in range(starting_letter):
            rotors[1].append(rotors[1].pop(0))

        r3 = input(
            'Enter the third letter for the starting point: ')
        starting_letter = rotors[2].index(r3)

        for i in range(starting_letter):
            # rotate the third rotor to the starting point
            rotors[2].append(rotors[2].pop(0))

    def rotate(index):
        # rotation of rotors function
        rotors[index].append(rotors[index].pop(0))

    def reset(self):
        # reset function

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


rotors = list()
plugboard_chosen = int()
new_msg = str()

Rotor_class = Rotors(rotors)
Plugboard_class = Plugboard(plugboard_chosen, new_msg)


print("This is an enigma machine, please select what you need to do by inserting the corresponding number")

selection = 0
while(selection != 4):
    print("\n1: Encode a Message ")
    print("2: Decode a Message ")
    print("3: Exit the program \n")

    selection = int(input("Enter your selection: "))

    if selection == 1 or 2:

        Rotor_class.reset()

        Rotor_class.rotor_order(rotors)
        Rotor_class.starting_point(rotors, rotors[0], rotors[1], rotors[2])

        x = input("Do you want to use a plugboard? ")
        if x == "Y":
            print("\n1: Choose a preset plugboard ")
            print("2: Configure a plugboard\n")

            ans = int(input("Choose one from the above: "))
            if ans == 1:
                Plugboard_class.plugboard_choice(plugboard_chosen)
                msg = input("Enter your Message: ")

                Plugboard_class.plugboard_settings(msg)
                Enigma_mahcine = Enigma(rotors, reflectorB, Plugboard_class)

                Enigma_mahcine.encode(msg)
                cipher = Enigma_mahcine.get_ciphered_msg()
                Plugboard_class.plugboard_settings(cipher)

                print(Plugboard_class.get_new_msg())

            elif ans == 2:
                Plugboard_class.plugboard_configure()
                msg = input("Enter your Message: ")

                Plugboard_class.plugboard_settings(msg)
                Enigma_mahcine = Enigma(rotors, reflectorB, Plugboard_class)

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

            print(rotors[0], "\n")
            print(rotors[1], "\n")
            print(rotors[2], "\n")
