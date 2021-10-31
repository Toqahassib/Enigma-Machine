
# importing the rotors and reflectors file
from rotortest import *


class Enigma:

    def __init__(self, rotors, reflector):
        self.encoded_msg = ""
        # self.plugboard = plugboarD

    # Encodes a Message
    def encode(self, msg):
        # define variables
        self.encoded_msg = ""
        self.rotor1_rotation = 0
        self.rotor2_rotation = 0

        # take input from user
        for i in range(len(msg)):
            # return the space as is
            if msg[i] == ' ':
                self.encoded_msg += ' '

            else:
                # rotate the rotors after every letter
                self.rotation()

                # take the index of the first letter of the msg in the alphabet list
                index = alphabet.index(msg[i])
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
                self.encoded_msg += encrypted

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
    def get_encoded_msg(self):
        return self.encoded_msg

    # returns dencoded msg
    def get_decoded_msg(self):
        return self.encoded_msg


class Plugboard:

    # pass through plug board
    def __init__(self):
        pass


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

    def starting_point(self, rotors, first_rotor, second_rotor, third_rotor):

        # take user input for the starting letter in the first rotor
        r1 = int(input(
            'Choose first letters for the starting point (eg. 13): '))

        # rotate the first rotor to the starting point
        for i in range(r1 - 1):
            rotors[0].append(rotors[0].pop(0))

        r2 = int(input(
            'Choose 3 letters for the starting point (eg. 1): '))

        # rotate the second rotor to the starting point
        for i in range(r2 - 1):
            rotors[1].append(rotors[1].pop(0))

        r3 = int(input(
            'Choose 3 letters for the starting point (eg. 20): '))

        for i in range(r3 - 1):
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


rotors = []
Enigma_mahcine = Enigma(rotors, reflectorB)
Rotor_class = Rotors(rotors)

print("This is an enigma machine, please select what you need to do by inserting the corresponding number")

selection = 0
while(selection != 4):
    print("\n1: Encode a Message ")
    print("2: Decode a Message ")
    print("3: Plugboard settings ")
    print("4: Exit the program \n")

    selection = int(input("Enter your selection: "))

    if selection == 1:

        Rotor_class.reset()
        Rotor_class.rotor_order(rotors)
        Rotor_class.starting_point(rotors, rotors[0], rotors[1], rotors[2])

        msg = input("Enter your Message: ")

        Enigma_mahcine.encode(msg)
        print(Enigma_mahcine.get_encoded_msg())

        print(rotors[0], "\n")
        print(rotors[1], "\n")
        print(rotors[2], "\n")

    elif selection == 2:

        Rotor_class.reset()
        Rotor_class.rotor_order(rotors)
        Rotor_class.starting_point(rotors, rotors[0], rotors[1], rotors[2])

        msg = input("Enter your Message: ")

        Enigma_mahcine.decode()
        print(Enigma_mahcine.get_decoded_msg())

        print(rotors[0], "\n")
        print(rotors[1], "\n")
        print(rotors[2], "\n")
