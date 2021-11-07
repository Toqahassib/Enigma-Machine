# importing the rotors, reflectors and plugboard file
from rotor import *
from plugboard import *


class Enigma:
    def __init__(self, rotors=[], msg="", cipher=""):
        self.rotors = rotors
        self.reflector = reflectorB
        self.msg = msg
        self.cipher = cipher

    def set_rotors(self, rotors):
        self.rotors = rotors

    def set_reflector(self):
        self.reflector = reflectorB

    def set_msg(self, msg):
        self.msg = msg

    def get_rotors(self):
        return self.rotors

    def get_reflector(self):
        return self.reflector

    def get_msg(self):
        return self.msg

    def get_cipher(self):
        return self.cipher

    def encode(self):
        # set rotor rotations to 0
        self.rotor1_rotation = 0
        self.rotor2_rotation = 0
        self.rotor3_rotation = 0
        self.cipher = ""

        # take input from user
        for i in range(len(self.msg)):
            # return any character that is not an alphabetic nor a num as is
            if not self.msg[i].isalnum():
                self.cipher += self.msg[i]

            else:
                # rotate the rotors after every letter
                self.rotation()

                # take the index of the first letter of the msg in the alphabet list
                index = alphabet.index(self.msg[i])
                # correspond it to the letter in the first rotor
                encrypted = self.rotors[0][index]

                # change the index to the coresponding letter in the alphabet list
                index = alphabet.index(encrypted)
                # correspond it to the letter in the second rotor
                encrypted = self.rotors[1][index]

                index = alphabet.index(encrypted)
                # correspond it to the letter in the third rotor
                encrypted = self.rotors[2][index]

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
                index = self.rotors[2].index(encrypted)
                # correspond it to the letter in the second rotor
                encrypted = self.rotors[2][index]
                # correspond it to the letter in the alphabet list
                encrypted = alphabet[index]

                index = self.rotors[1].index(encrypted)
                encrypted = self.rotors[1][index]
                encrypted = alphabet[index]

                index = self.rotors[0].index(encrypted)
                encrypted = self.rotors[0][index]
                encrypted = alphabet[index]
                # adds letter by letter to the encoded msg
                self.cipher += encrypted

    def rotation(self):
        # rotation of rotor1
        Rotors.rotate(self, 0)

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


class Plugboard:
    # pass through plug board
    def __init__(self, plugboard_chosen=[], new_msg=""):
        self.plugboard_chosen = plugboard_chosen
        self.new_msg = new_msg

    def set_new_msg(self, new_msg):
        self.new_msg = new_msg

    def get_plugboard_chosen(self):
        return self.plugboard_chosen

    def get_new_msg(self):
        return self.new_msg

    # user chooses from 3 plugboards
    def plugboard_choice(self):
        plugboard = INTvalidation("choose your plugboard (29, 30, 31): ")
        while plugboard not in range(29, 32):
            print("\nYou can enter from 29 to 31 ONLY.")
            plugboard = INTvalidation("choose your plugboard (29, 30, 31): ")
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

        count = INTvalidation("How many pairings will you configure? ")

        for i in range(count):
            x = input("Enter first pair: ")  # '(a,b),(b,c),(c,d),(d,e)'

            for tup in x.split("),("):
                # tup looks like `(a,a` or `b,b`
                tup = tup.replace(")", "").replace("(", "")
                # tup looks like `a,a` or `b,b`
                user_plugboard.append(tuple(tup.split(",")))

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


class Rotors:
    def __init__(self, first_rotor=[], mid_rotor=[], last_rotor=[]):
        self.first_rotor = first_rotor
        self.mid_rotor = mid_rotor
        self.last_rotor = last_rotor
        self.rotors = []

    def set_first_rotor(self):
        self.first_rotor = self.rotors[0]

    def set_mid_rotor(self):
        self.mid_rotor = self.rotors[1]

    def set_last_rotor(self):
        self.last_rotor = self.rotors[2]

    def get_first_rotor(self):
        return self.first_rotor

    def get_mid_rotor(self):
        return self.mid_rotor

    def get_last_rotor(self):
        return self.last_rotor

    def get_rotors(self):
        return self.rotors

    # orders the rotors based on user input
    def rotor_order(self):

        while self.rotors == []:
            for i in range(3):
                rotor = INTvalidation("choose rotor {}: ".format(i + 1))
                if rotor == 1:
                    self.rotors.append(rotorI)
                elif rotor == 2:
                    self.rotors.append(rotorII)
                elif rotor == 3:
                    self.rotors.append(rotorIII)
                elif rotor == 4:
                    self.rotors.append(rotorIV)
                else:
                    print("choice is invalid")

            for elem in self.rotors:
                if self.rotors.count(elem) > 1:
                    self.rotors = []
                    print("\nRotors can't be chosen twice. Please try again.")
                    break

    def starting_point(self):

        for i in range(3):
            start = input("Enter the starting point of rotor {}: ".format(i + 1))

            while start not in self.rotors[i]:
                print("Enter any alphabet characet or a number form 0-9 ONLY.")
                start = input(
                    "Enter the staring starting point of rotor {}: ".format(i + 1)
                )

            # change the letter to its index
            starting_letter = self.rotors[i].index(start)

            # rotate the first rotor to the starting point
            for x in range(starting_letter):
                self.rotate(i)

    def rotate(self, index):
        # rotation of rotors function
        self.rotors[index].append(self.rotors[index].pop(0))

    #  function to reset rotors to their original state

    def reset(self):
        self.rotors = []
        # rotate first rotor till the first index is E
        while rotorI[0] != "E":
            rotorI.append(rotorI.pop(0))

        # rotate second rotor till the first index is A
        while rotorII[0] != "A":
            rotorII.append(rotorII.pop(0))

        # rotate third rotor till the first index is B
        while rotorIII[0] != "B":
            rotorIII.append(rotorIII.pop(0))

        # rotate fourth rotor till the first index is E
        while rotorIV[0] != "E":
            rotorIV.append(rotorIV.pop(0))


# saves the output in a txt file
def save_output():
    save_output = input("do you want to save the output in a text file? ")
    if save_output == "y":
        file_name = input("enter name: ")
        file = open(file_name, "w")

        file.write(Enigma_class.get_cipher())
        file.close()


# validation for integer inputs
def INTvalidation(text):
    while True:
        try:
            Input_int = int(input(text))

        except ValueError:
            print("\nInvalid, answer should be in numbers.")
            continue
        else:
            return Input_int


Enigma_class = Enigma()
Rotor_class = Rotors(first_rotor=[], mid_rotor=[], last_rotor=[])
Plugboard_class = Plugboard()


def __main__():
    print(
        "This is an enigma machine, please select what you need to do by inserting the corresponding number"
    )

    selection = 0
    while selection != 3:
        print("\n1: Encode a Message ")
        print("2: Decode a Message ")
        print("3: Exit the program \n")

        selection = INTvalidation("\nEnter your selection: ")
        if selection in range(1, 3):
            # reset rotors with every input
            Rotor_class.reset()
            Plugboard_class.set_new_msg("")
            print(Plugboard_class.get_new_msg())

            Rotor_class.rotor_order()
            Rotor_class.starting_point()

            Rotor_class.set_first_rotor()
            Rotor_class.set_mid_rotor()
            Rotor_class.set_last_rotor()

            x = Rotor_class.get_rotors()
            Enigma_class.set_rotors(x)

            # plugboard usage
            x = input("Do you want to use a plugboard (yes or no)? ")
            if x.lower() == "yes":
                print("\n1: Choose a preset plugboard ")
                print("2: Configure a plugboard\n")

                ans = INTvalidation("Choose one from the above: ")
                while ans not in range(1, 3):
                    print("\nInvalide. You can only choose either 1 or 2.")
                    ans = INTvalidation("Choose one from the above: ")

                if ans == 1:
                    Plugboard_class.plugboard_choice()
                    print(Plugboard_class.get_plugboard_chosen())

                elif ans == 2:
                    Plugboard_class.plugboard_configure()
                    print(Plugboard_class.get_plugboard_chosen())

            else:
                print(Plugboard_class.get_plugboard_chosen())

            print("1. Type a message")
            print("2. Import a file")

            msg_type = INTvalidation("Choose one from the above: ")
            while msg_type not in range(1, 3):
                print("\nInvalide. You can only choose either 1 or 2.")
                msg_type = INTvalidation("Choose one from the above: ")

            if msg_type == 1:
                msg = input("Enter your Message: ")
            elif msg_type == 2:
                file_name = input("Enter your file name: ")
                open(file_name, "r")

                with open(file_name) as f:
                    msg = f.read()
                    f.close()

            Plugboard_class.plugboard_settings(msg)

            new_msg = Plugboard_class.get_new_msg()
            Enigma_class.set_msg(new_msg)

            Enigma_class.encode()

            cipher = Enigma_class.get_cipher()

            Plugboard_class.plugboard_settings(cipher)

            print(Plugboard_class.get_new_msg())
            save_output()

        elif selection == 3:
            quit()
        else:
            print("Invalid. Please choose a number from 1 to 3.")


__main__()
