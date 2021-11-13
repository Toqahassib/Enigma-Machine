# importing the rotors, reflectors and plugboard file
from rotor import *
from plugboard import *


class Enigma:
    def __init__(self, rotors=[], reflector=[], reflector_map=[], msg="", cipher=""):
        self.rotors = rotors
        self.reflector = reflector
        self.reflector_map = reflector_map
        self.msg = msg
        self.cipher = cipher

    # sets the 3 rotors in a list
    def set_rotors(self, rotors):
        self.rotors = rotors

    # sets the reflector
    def set_reflector(self, reflector):
        self.reflector = reflector

    # sets the reflector_map
    def set_reflector_map(self, reflector_map):
        self.reflector_map = reflector_map

    # sets the message that will get encrypted/decrypted
    def set_msg(self, msg):
        self.msg = msg

    # returns the list of rotors
    def get_rotors(self):
        return self.rotors

    # returns the reflector
    def get_reflector(self):
        return self.reflector

    # returns the reflector_map
    def get_reflector_map(self):
        return self.reflector_map

    # returns ciphered message
    def get_cipher(self):
        return self.cipher

    # function to cipher/decipher the message
    def encode(self):
        # set rotor rotations to 0 and empty the cipher text
        self.rotor1_rotation = 0
        self.rotor2_rotation = 0
        self.cipher = ""

        # for loop to cipher/decipher the message letter by letter
        for i in range(len(self.msg)):
            # return any character that is not an alphabetic nor a num as is
            if not self.msg[i].isalnum():
                self.cipher += self.msg[i]

            else:
                # rotate the rotors after every letter
                self.rotation()

                # set the index as the letter's index in the alphabet list
                index = alphabet.index(self.msg[i])
                # set the encrypted letter as the index's letter in the 1st rotor
                encrypted = self.rotors[0][index]

                # change the index to the encrypted letter's index in the alphabet list
                index = alphabet.index(encrypted)
                # change the encrypted letter as the index's letter in the 2nd rotor
                encrypted = self.rotors[1][index]

                index = alphabet.index(encrypted)
                # change the encrypted letter as the index's letter in the 3rd rotor
                encrypted = self.rotors[2][index]

                index = alphabet.index(encrypted)
                # change the encrypted letter as the index's letter in the reflector
                encrypted = reflectorB[index]

                # for loop to check the mapping of the letter in the reflector
                for x in self.reflector_map:
                    if x[0] == encrypted:
                        encrypted = x[1]

                    elif x[1] == encrypted:
                        encrypted = x[0]

                # change the index to the encrypted letter's index in the reflector
                index = reflectorB.index(encrypted)
                # change the encrypted letter as the index's letter in the alphabet list
                encrypted = alphabet[index]

                # change the index to the encrypted letter's index in the 3rd rotor
                index = self.rotors[2].index(encrypted)
                # change the encrypted letter as the index's letter in the 3rd rotor
                encrypted = self.rotors[2][index]
                # change the encrypted letter as the index's letter in the alphabet list
                encrypted = alphabet[index]

                index = self.rotors[1].index(encrypted)
                encrypted = self.rotors[1][index]
                encrypted = alphabet[index]

                index = self.rotors[0].index(encrypted)
                encrypted = self.rotors[0][index]
                encrypted = alphabet[index]
                # add letter by letter to the ciphered msg
                self.cipher += encrypted

    # function to ratate the rotors
    def rotation(self):
        # rotation of rotor1
        Rotors.rotate(self, 0)

        # incriminate after each letter in rotor1
        self.rotor1_rotation += 1

        # rotate rotor2 after full rotation of rotor1
        if self.rotor1_rotation == 60:
            Rotors.rotate(1)
            # reset the incrimination
            self.rotor1_rotation = 0
            # incriminate after each letter in rotor2
            self.rotor2_rotation += 1

        # rotate rotor3 after full rotation of rotor2
        if self.rotor2_rotation == 60:
            self.rotor2_rotation = 0
            Rotors.rotate(2)


class Plugboard:

    def __init__(self, plugboard_chosen=[], new_msg=""):
        self.plugboard_chosen = plugboard_chosen
        self.new_msg = new_msg

    # sets the new msg after it passed from the plugboard
    def set_new_msg(self, new_msg):
        self.new_msg = new_msg

    # sets the chosen plugboard
    def get_plugboard_chosen(self):
        return self.plugboard_chosen

    # returns the new msg
    def get_new_msg(self):
        return self.new_msg

    # function to know wether the user wants to use a plugboard or not
    def plugboard_usage(self):

        x = input("\nDo you want to use a plugboard (y/n)? ")
        while x.lower() not in ("yes", "y", "no", "n"):
            print("Invalid. You can only answer with yes, y, no, or n.")
            x = input("\nDo you want to use a plugboard (y/n)? ")

        if x.lower() in ("yes", "y"):
            print("\n1: Choose a preset plugboard ")
            print("2: Configure a plugboard")

            ans = INTvalidation("\nChoose one from the above: ")
            while ans not in range(1, 3):
                print("\nInvalide. You can only choose either 1 or 2.")
                ans = INTvalidation("Choose one from the above: ")

            if ans == 1:
                self.plugboard_choice()

            elif ans == 2:
                self.plugboard_configure()
        else:
            pass

    # function to let users choose 1 plugboard from 3
    def plugboard_choice(self):
        plugboard = INTvalidation("\nChoose your plugboard (29, 30, 31): ")
        while plugboard not in range(29, 32):
            print("\nYou can enter from 29 to 31 ONLY.")
            plugboard = INTvalidation("choose your plugboard (29, 30, 31): ")
        if plugboard == 29:
            self.plugboard_chosen = plugboard29
        elif plugboard == 30:
            self.plugboard_chosen = plugboard30
        elif plugboard == 31:
            self.plugboard_chosen = plugboard31

    # function to let users configure their own plugboard
    def plugboard_configure(self):
        user_plugboard = []

        count = INTvalidation(
            "\nHow many pairings will you configure (limit: 10)? ")
        while count > 10:
            print("Invalid, the limit of pairings is 10.")
            count = INTvalidation(
                "\nHow many pairings will you configure (limit: 10)? ")

        print("\nExample:\nEnter pair 1: a,e\n")

        # for loop to append the input as tuples in a list
        for i in range(count):
            x = input("Enter pair {}: ".format(i + 1))

            # while loop to ensure the input format is correct
            while True:
                if len(x) != 3:
                    print("Invalid input.")
                    print("\nExample:\nEnter pair 1: a,e\n")

                    x = input("Enter pair {}: ".format(i + 1))

                elif len(x) == 3:
                    if x[1] != ",":
                        print("Invalid input.")
                        print("\nExample:\nEnter pair 1: a,e\n")

                        x = input("Enter pair {}: ".format(i + 1))
                    else:
                        break

            user_plugboard.append(tuple(x.split(",")))

        print("You have succussfully configured the plugboard!")
        self.plugboard_chosen = user_plugboard

    # function to pair the letters
    def plugboard_settings(self, msg):
        # convert the msg characters to a list
        list_msg = list(msg)

        for i in range(len(msg)):
            for x in self.plugboard_chosen:
                # swap the character with it's pair
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

    # sets the 1st rotor
    def set_first_rotor(self):
        self.first_rotor = self.rotors[0]

    # sets the 2nd rotor
    def set_mid_rotor(self):
        self.mid_rotor = self.rotors[1]

    # sets the 3rd rotor
    def set_last_rotor(self):
        self.last_rotor = self.rotors[2]

        # sets the 1st rotor
    def get_first_rotor(self):
        return self.rotors[0]

    # sets the 2nd rotor
    def get_mid_rotor(self):
        return self.rotors[1]

    # sets the 3rd rotor
    def get_last_rotor(self):
        return self.rotors[2]

    # returns all 3 rotors in a list
    def get_rotors(self):
        return self.rotors

    # function to let users choose 3 rotors in order
    def rotor_order(self):

        while self.rotors == []:
            for i in range(3):
                rotor = INTvalidation("Choose rotor {}: ".format(i + 1))
                # while loop to make sure the user chooses a rotor from 1 to 5
                while rotor not in range(1, 6):
                    print("\nInvalid. You can only choose from 1 to 5 rotors.")
                    rotor = INTvalidation("choose rotor {}: ".format(i + 1))

                if rotor == 1:
                    self.rotors.append(rotorI)
                elif rotor == 2:
                    self.rotors.append(rotorII)
                elif rotor == 3:
                    self.rotors.append(rotorIII)
                elif rotor == 4:
                    self.rotors.append(rotorIV)
                elif rotor == 5:
                    self.rotors.append(rotorV)

            # for loop to check for duplicated rotors
            for elem in self.rotors:
                if self.rotors.count(elem) > 1:
                    self.rotors = []
                    print("\nRotors can't be chosen twice. Please try again.")
                    break

    # function to let users choose the starting point of the 3 rotors
    def starting_point(self):

        for i in range(3):
            start = input(
                "Enter the starting point of rotor {}: ".format(i + 1))

            # while loop to ensure the user choose a character that is found in the rotor
            while start not in self.rotors[i]:
                print("\nEnter one alphabet characet or a number form 0-9 ONLY.")
                start = input(
                    "Enter the starting point of rotor {}: ".format(i + 1))

            # change the letter to its index
            starting_letter = self.rotors[i].index(start)

            # rotate the rotor to the starting point
            for x in range(starting_letter):
                self.rotate(i)

    # function to ratate any list
    def rotate(self, index):

        self.rotors[index].append(self.rotors[index].pop(0))

    #  function to reset rotors to their original state
    def reset(self):
        self.rotors = []

        while rotorI[0] != "E":
            rotorI.append(rotorI.pop(0))

        while rotorII[0] != "A":
            rotorII.append(rotorII.pop(0))

        while rotorIII[0] != "B":
            rotorIII.append(rotorIII.pop(0))

        while rotorIV[0] != "E":
            rotorIV.append(rotorIV.pop(0))


class Reflector:
    def __init__(self, reflector=[], reflector_map=[]):
        self.reflector = reflector
        self.reflector_map = reflector_map

    # function to let users choose 1 reflector from 3
    def reflector_choice(self):
        reflector = input("Choose a reflector (A, B, or C): ")

        # while loop to ensure users only choose reflector A,b, or C
        while reflector.upper() not in ("A", "B", "C"):
            print("Invalid. You can only enter A, B, or C.")
            reflector = input("Choose a reflector (A, B, or C): ")

        if reflector.upper() == "A":
            self.reflector = reflectorA
            self.reflector_map = reflectorA_map
        elif reflector.upper() == "B":
            self.reflector = reflectorB
            self.reflector_map = reflectorB_map
        elif reflector.upper() == "C":
            self.reflector = reflectorC
            self.reflector_map = reflectorC_map

    # returns the reflector
    def get_reflector(self):
        return self.reflector

    # returns the reflector map
    def get_reflector_map(self):
        return self.reflector_map


# function to save the output in a txt file
def save_output():

    save_output = input(
        "\nDo you want to save the output in a text file (y/n)? ")

    while save_output.lower() not in ("yes", "y", "no", "n"):
        print("Invalid. You can only answer with yes, y, no, or n.")
        save_output = input(
            "\nDo you want to save the output in a text file (y/n)? ")

    if save_output.lower() in ("yes", "y"):
        file_name = input("Enter your file name: ")
        file = open(file_name, "w")

        file.write(Enigma_class.get_cipher())
        file.close()
        print("\nFile saved Successfully!")
    else:
        pass


# funcation to validate integer inputs
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
Reflector_class = Reflector()


if __name__ == "__main__":
    print(
        "\nThis is an enigma machine, please select what you need to do by inserting the corresponding number"
    )

    selection = 0
    while selection != 3:
        print("\n1: Encode a Message ")
        print("2: Decode a Message ")
        print("3: Exit the program \n")

        selection = INTvalidation("\nEnter your selection: ")
        print(" ")
        if selection in range(1, 3):
            # reset rotors, empty msg with every input
            Rotor_class.reset()
            Plugboard_class.set_new_msg("")

            Rotor_class.rotor_order()
            print(" ")

            Reflector_class.reflector_choice()
            print(" ")
            Rotor_class.starting_point()

            Rotor_class.set_first_rotor()
            Rotor_class.set_mid_rotor()
            Rotor_class.set_last_rotor()

            # pass the rotors chosen to the enigma class
            rot = Rotor_class.get_rotors()
            Enigma_class.set_rotors(rot)

            # pass the reflector chosen to the enigma class
            ref = Reflector_class.get_reflector()
            Enigma_class.set_reflector(ref)

            ref_map = Reflector_class.get_reflector_map()
            Enigma_class.set_reflector_map(ref_map)

            Plugboard_class.plugboard_usage()

            print("------------------------------------------------The Configured settings are------------------------------------------------")

            if Plugboard_class.get_plugboard_chosen() == []:
                print("\n-------------------------------------------------------Plugboard--------------------------------------------------------\n",
                      "No Plugboard used.")
            else:

                print("\n-------------------------------------------------------Plugboard--------------------------------------------------------\n",
                      Plugboard_class.get_plugboard_chosen())

            print("\n---------------------------------------------------------Rotor1---------------------------------------------------------\n",
                  Rotor_class.get_first_rotor())

            print("\n---------------------------------------------------------Rotor2--------------------------------------------------------\n",
                  Rotor_class.get_mid_rotor())

            print("\n---------------------------------------------------------Rotor3-------------------------------------------------------\n",
                  Rotor_class.get_last_rotor())

            print("\n--------------------------------------------------------Reflector-----------------------------------------------------\n",
                  Reflector_class.get_reflector())

            # msg type
            print("\n1. Type a message")
            print("2. Import a file")

            msg_type = INTvalidation("\nChoose one from the above: ")
            while msg_type not in range(1, 3):
                print("\nInvalide. You can only choose either 1 or 2.")
                msg_type = INTvalidation("Choose one from the above: ")

            if msg_type == 1:
                msg = input("\nEnter your Message: ")
            # import a file
            elif msg_type == 2:
                while True:
                    try:
                        file_name = input("\nEnter your file name: ")
                        open(file_name, "r")

                        with open(file_name) as f:
                            msg = f.read()
                            f.close()
                            print("File imported successfully!")
                    # error handling
                    except FileNotFoundError:
                        print("File not found. Please try another filename.")
                        continue
                    else:
                        break

            # send msg to plugboard, incase it was used
            Plugboard_class.plugboard_settings(msg)

            # pass msg from plugboard class to enigma class
            new_msg = Plugboard_class.get_new_msg()
            Enigma_class.set_msg(new_msg)

            Enigma_class.encode()

            # return msg to plugboard
            cipher = Enigma_class.get_cipher()
            Plugboard_class.plugboard_settings(cipher)

            print("\nResult:", Plugboard_class.get_new_msg())
            save_output()

        elif selection == 3:
            quit()
        else:
            print("\nInvalid. Please choose a number from 1 to 3.")
