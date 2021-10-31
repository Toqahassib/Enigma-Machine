
#  https://en.wikipedia.org/wiki/Enigma_rotor_details#Rotor_wiring_tables

# https://www.cryptomuseum.com/crypto/enigma/wiring.htm

from collections import deque
from typing import Counter


alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

rotorI = ['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A', 'I', 'B', 'R', 'C', 'J',
          'h', '0', '9', '4', 'i', 'p', 'd', '7', 'j', 'x', 'u', 'a', 'o', '3', 'k', 'b', 'q', 'w', '2', 'f',
          'r',
          'e',
          '8',
          'g',
          'l',
          '6',
          't',
          'v',
          '5',
          'c',
          'm',
          '1',
          'n',
          's',
          'y',
          'z']

rotorII = ['A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H',
           'W', 'T', 'M', 'C', 'Q', 'G', 'Z', 'N', 'P', 'Y', 'F', 'V', 'O', 'E', 'i',
           'a',
           'h',
           'e',
           'y',
           '1',
           'g',
           '6',
           '2',
           'w',
           'o',
           'l',
           'd',
           'm',
           'k',
           'n',
           'q',
           'c',
           '0',
           's',
           'f',
           'p',
           '5',
           't',
           '3',
           '9',
           '7',
           '4',
           'v',
           'j',
           'x',
           'r',
           '8',
           'z',
           'u',
           'b']

rotorIII = ['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V',
            'Z', 'N', 'Y', 'E', 'I', 'W', 'G', 'A', 'K', 'M', 'U', 'S', 'Q', 'O', 's',
            'x',
            '1',
            'w',
            'v',
            'z',
            'p',
            '8',
            '2',
            'k',
            '3',
            'm',
            'c',
            '6',
            '0',
            'f',
            'j',
            'y',
            'd',
            '4',
            'g',
            'i',
            'a',
            'e',
            'l',
            '5',
            'n',
            'q',
            'o',
            'u',
            '9',
            'h',
            '7',
            'b',
            't',
            'r', ]

rotorIV = ['E', 'S', 'O', 'V', 'P', 'Z', 'J', 'A', 'Y', 'Q', 'U', 'I',
           'R', 'H', 'X', 'L', 'N', 'F', 'T', 'G', 'K', 'D', 'C', 'M', 'W', 'B', 'x',
           'b',
           'c',
           'v',
           'n',
           'q',
           '1',
           '8',
           '0',
           'd',
           'i',
           'o',
           '7',
           'f',
           '2',
           's',
           't',
           '5',
           'k',
           '4',
           'e',
           'j',
           'p',
           'w',
           'g',
           'z',
           'u',
           'l',
           'h',
           'y',
           'm',
           'a',
           'r',
           '9',
           '6',
           '3']

reflectorA = ['E', 'J', 'M', 'Z', 'A', 'L', 'Y', 'X', 'V', 'B', 'W', 'F',
              'C', 'R', 'Q', 'U', 'O', 'N', 'T', 'S', 'P', 'I', 'K', 'H', 'G', 'D']

reflectorB = ['Y', 'R', 'U', 'H', 'Q', 'S', 'L', 'D', 'P', 'X', 'N', 'G',
              'O', 'K', 'M', 'I', 'E', 'B', 'F', 'Z', 'C', 'W', 'V', 'J', 'A', 'T',
              'h',
              '3',
              'b',
              '4',
              'x',
              'w',
              't',
              'r',
              'q',
              'n',
              'y',
              '2',
              'l',
              '7',
              'c',
              'j',
              'e',
              'o',
              '0',
              '1',
              '6',
              'u',
              'g',
              'i',
              'f',
              'a',
              'd',
              '8',
              '5',
              'k',
              'z',
              '9',
              'm',
              's',
              'v',
              'p']

reflectorC = ['F', 'V', 'P', 'J', 'I', 'A', 'O', 'Y', 'E', 'D', 'R', 'Z',
              'X', 'W', 'G', 'C', 'T', 'K', 'U', 'Q', 'S', 'B', 'N', 'M', 'H', 'L']

reflectorB_map = [('A', 'Y'), ('B', 'R'), ('C', 'U'), ('D', 'H'), ('E', 'Q'), ('F', 'S'),
                  ('G', 'L'), ('I', 'P'), ('J', 'X'), ('K',
                                                       'N'), ('M', 'O'), ('T', 'Z'), ('V', 'W'),
                  ('h', 'a'), ('b', 'c'), ('x', 'd'), ('w', 'e'), ('t',
                                                                   'f'), ('r', 'g'), ('q', 'i'), ('n', 'j'),
                  ('y', 'k'), ('l', 'm'), ('o', 'p'), ('u', 's'), ('z', 'v'), ('3', '0'), ('4', '1'), ('2', '5'), ('7', '6'), ('8', '9')]


# def INTvalidation(msg):
#     while True:
#         try:
#             Input_int = int(input(msg))

#         except ValueError:
#             print("Invalid, answer should be in numbers.")
#             continue
#         else:
#             return Input_int
