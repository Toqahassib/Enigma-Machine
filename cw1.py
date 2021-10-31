
# importing the rotors and reflectors file
from rotor import *


class Enigma:

    def __init__(self, rotors, reflector):
        self.encoded_msg = ""
        self.count = 0
        self.count2 = 0
        # self.plugboard = plugboarD

    # Encodes a Message
    def encode(self, msg):

        # take input from user
        self.encoded_msg = ""
        rotor1_rotation = 0
        rotor2_rotation = 0

        for i in range(len(msg)):
            if msg[i] == ' ':
                self.encoded_msg += ' '

            else:
                self.rotation(rotor1_rotation, rotor2_rotation)

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

                # check the mapping of the letter
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

    def rotation(self, rotor1_rotation, rotor2_rotation):
        # rotation of rotor after each letter
        Rotors.rotate(0)
        rotor1_rotation += 1
        print(rotor1_rotation)
        # rotate second rotor after full rotation of first rotor
        if rotor1_rotation == 25:
            Rotors.rotate(1)
            rotor1_rotation = 0
            rotor2_rotation += 1
        # rotate third rotor after full rotation of second rotor
        if rotor2_rotation == 25:
            rotor2_rotation = 0
            Rotors.rotate(2)

    def decode(self):
        # Enigma.reset(self)
        self.encode(msg)

    # returns encoded msg
    def get_encoded_msg(self):
        return self.encoded_msg

    # returns encoded msg
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
        rotors[index].append(rotors[index].pop(0))


class Reflector:

    def __init__(self, reflector):
        self.reflector = reflector


print("This is an enigma machine, please select what you need to do by inserting the corresponding number")

selection = 0
while(selection != 4):
    print("\n1: Encode a Message ")
    print("2: Decode a Message ")
    print("3: Plugboard settings ")
    print("4: Exit the program \n")

    selection = int(input("Enter your selection: "))
    rotors = []

    if selection == 1:

        enigma_mahcine = Enigma(rotors, reflectorB)

        x = Rotors(rotors)

        x.rotor_order(rotors)
        x.starting_point(rotors, rotors[0], rotors[1], rotors[2])

        print(rotors[0])
        print(rotors[1])
        print(rotors[2])

        msg = input("Enter your Message: ")

        enigma_mahcine.encode(msg.upper())
        print(enigma_mahcine.get_encoded_msg())
        print(rotors[0])
        print(rotors[1])
        print(rotors[2])

    elif selection == 2:
        decode = Enigma(rotors, reflectorB)
        x = Rotors(rotors)

        print(rotors)

        x.rotor_order(rotors)
        x.starting_point(rotors, rotors[0], rotors[1], rotors[2])

        print(rotors[0])
        print(rotors[1])
        print(rotors[2])

        msg = input("Enter your Message: ")
        decode.decode()
        print(decode.get_decoded_msg())
