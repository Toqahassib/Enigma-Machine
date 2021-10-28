from _typeshed import Self
from rotor import *


class Enigma:

    def __init__(self, rotors):
        pass
        # self.plugboard = plugboard

    # Encodes a Message
    def encode(self, msg):

        # msg will be the message input
        new_msg = ""
        for i in range(len(msg)):
            rotorI.append(rotorI.pop(0))

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

            new_msg += encrypted

        print(new_msg)

    # # reset machine settings
    # def reset(self, rotors):
    #     for rotor in rotors:
    #         rotor.reset()


class Plugboard:

    # pass through plug board
    def __init__(self):
        pass


class Rotors:

    def __init__(self, first_rotor, mid_rotor, last_rotor, reflector, rotors):
        self.first_rotor = first_rotor
        self.mid_rotor = mid_rotor
        self.last_rotor = last_rotor
        self.reflector = reflector
        self.rotors = rotors

    # starting point
    def starting_point(self):
        starting_r1 = int(input(
            'Choose 3 letters for the starting point (eg. 13): '))

        for i in range(starting_r1):
            self.rotors[0].append(self.rotors[0].pop(0))

        starting_r2 = int(input(
            'Choose 3 letters for the starting point (eg. 1): '))

        for i in range(starting_r2):
            self.rotors[1].append(self.rotors[1].pop(0))

        starting_r3 = int(input(
            'Choose 3 letters for the starting point (eg. 20): '))

        for i in range(starting_r3):
            self.rotors[2].append(self.rotors[2].pop(0))


class Reflector:

    def __init__(self, reflector):
        Self.reflector = reflector
        pass

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

        x = Rotors(first_rotor, second_rotor, third_rotor, reflector, rotors)
        # r = Reflector(reflector)

        x.starting_point()
        # r.reflector()

        msg = input("Enter your Message: ")

        y = Enigma(rotors)

        y.encode(msg.upper())
