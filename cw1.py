
# importing my rotors and reflectors file
from rotor import *


class Enigma:

    def __init__(self, rotors, reflector):
        self.encoded_msg = ""
        # self.plugboard = plugboard

    # Encodes a Message
    def encode(self, msg):

        # take input from user
        self.encoded_msg = ""
        for i in range(len(msg)):
            # rotation of rotor after each letter
            rotorI.append(rotorI.pop(0))

            # take the index of the first letter of the msg in the alphabet list & corespond it to the first rotor chosen
            index = alphabet.index(msg[i])
            encrypted = rotors[0][index]

            index = alphabet.index(encrypted)
            encrypted = rotors[1][index]

            index = alphabet.index(encrypted)
            encrypted = rotors[2][index]

            index = alphabet.index(encrypted)
            encrypted = rotors[3][index]

            index = alphabet.index(encrypted)
            encrypted = rotors[2][index]

            index = alphabet.index(encrypted)
            encrypted = rotors[1][index]

            index = alphabet.index(encrypted)
            encrypted = rotors[0][index]

            # adds letter by letter to the encoded msg
            self.encoded_msg += encrypted

    # returns encoded msg
    def get_encoded_msg(self):
        return self.encoded_msg

    # # reset machine settings
    # def reset(self, rotors):
    #     for rotor in rotors:
    #         rotor.reset()


class Plugboard:

    # pass through plug board
    def __init__(self):
        pass


class Rotors:

    def __init__(self, first_rotor, mid_rotor, last_rotor, rotors):
        self.first_rotor = first_rotor
        self.mid_rotor = mid_rotor
        self.last_rotor = last_rotor
        # self.reflector = reflector
        self.rotors = rotors

    # starting point
    def ring_setting(self):
        # take user input for the starting letter in the first rotor
        r1 = int(input(
            'Choose first letters for the starting point (eg. 13): '))

        # rotate the first rotor to the starting point
        self.rotors[0].append(self.rotors[0].pop(r1 + 1))

        r2 = int(input(
            'Choose 3 letters for the starting point (eg. 1): '))

        # rotate the second rotor to the starting point
        self.rotors[1].append(self.rotors[1].pop(r2 + 1))

        r3 = int(input(
            'Choose 3 letters for the starting point (eg. 20): '))

        # rotate the third rotor to the starting point
        self.rotors[2].append(self.rotors[2].pop(r3 + 1))


class Reflector:

    def __init__(self, reflector):
        self.reflector = reflector

        # forward

    def forward(self):
        pass


print("This is an enigma machine, please select what you need to do by inserting the corresponding number")

selection = 0
while(selection != 5):
    print("\n1: Encode a Message ")
    print("2: Plugboard settings ")
    print("5: Exit the program \n")

    selection = int(input("Enter your selection: "))
    rotors = []

    if selection == 1:

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

        reflector = input('choose a reflector (ex: A): ')
        if reflector == 'A':
            rotors.append(reflectorA)
        elif reflector == 'B':
            rotors.append(reflectorB)
        elif reflector == 'C':
            rotors.append(reflectorC)
        else:
            print("choice is invalid")

        x = Rotors(first_rotor, second_rotor, third_rotor, rotors)
        r = Reflector(reflector)

        x.ring_setting()

        msg = input("Enter your Message: ")

        enigma_mahcine = Enigma(rotors, reflector)

        enigma_mahcine.encode(msg.upper())
        print(enigma_mahcine.get_encoded_msg())
