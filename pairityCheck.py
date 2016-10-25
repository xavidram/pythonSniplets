"""
Author: Xavid Ramirez
Desc: This 7-bit even parity checker will ask the
      user to enter a 7 bit parity and will check to see if
      it is correct. It will run through a series of check for
      each parity bit, noting which one is wrong and correct the
      parity with an issue, returning the correct parity output.

Purpose: We covered parity in my Networks class so to better understand it
        I wrote this small python program to better understand parities and
        how the error detection and correction works.
"""

"""
	7-bit hamming code used commonly
		-Data bits - 4 bits
		-parity bits - 3 bits

	Knowns:
		2^n {where n = 0,1....n}  = parity bits
		2^0  = 1 , 2^1 = 1 , 2^2 = 4  => parity bits

		=>  D7 | D6 | D5 | P4 | D3 | P2 | P1

		P1 => {D3, D5, D7}
		P2 => {D3, D6, D7}
		P4 => {D5, D6, D7}

														   _______________________________
	EX:		Data = 1011  => to 7bit =>  1 0 1 _ 1 _ _  => | 1 | 0 | 1 | P4 | 1 | P2 | P1 |

		P1 = {D3, D5, D7} => {1,1,1} so for Even Parity P1 = 1
		P2 = {D3, D6, D7} => {1,0,1} so for Even Parity P2 = 0 
		P4 = {D5, D6, D7} => {1,0,1} so for Even Parity P4 = 0
									____________________________
		So Data 1011 => to 7Bit => | 1 | 0 | 1 | 0 | 1 | 0 | 1 |

"""


class hammingCode:

    def __init__(self, data):
        # Bits should be 7 bits long as this will fix the errors
        self.bits = data
        self.errorP1 = False
        self.errorBit = None

    def check(self):

        allBits = list(self.bits)
        errorBit = 0
        # check the parities

        # for P1 check D3, D5, and D7
        P1_ones = allBits[0] + allBits[2] + allBits[4]
        print(
            "Data for Parity bit 1 = { " + allBits[0] + "," + allBits[2] + "," + allBits[4] + " }")
        print("Parity Bit 1 == " + allBits[6])

        if P1_ones.count('1') % 2 == 0 and allBits[6] == '0':
            print("Parity Bit 1 is Correct.")
        elif P1_ones.count('1') % 2 != 0 and allBits[6] == '1':
        	print("Parity Bit 1 is Correct.")
        else:
            print("Parity Bit 1 is Incorrect!")
            errorBit += (int(allBits[6]) * 1)
            self.error = True

        # for P2 check D3, D6, and D7
        P2_ones = allBits[0] + allBits[1] + allBits[4]
        print(
            "Data for Parity bit 2 = { " + allBits[0] + "," + allBits[1] + "," + allBits[4] + " }")
        print("Parity Bit 2 == " + allBits[5])
        if (P2_ones.count('1') % 2 == 0) and allBits[5] == '0':
            print("Parity Bit 2 is Correct.")
        elif P2_ones.count('1') % 2 != 0 and allBits[6] == '1':
        	print("Parity Bit 2 is Correct.")
        else:
            print("Parity Bit 2 is Incorrect!")
            errorBit += (int(allBits[5]) * 2)
            self.error = True

        # for P4 check D5, D6, and D7
        P4_ones = allBits[0] + allBits[1] + allBits[2]
        print(
            "Data for Parity bit 4 = { " + allBits[0] + "," + allBits[1] + "," + allBits[2] + " }")
        print("Parity Bit 4 == " + allBits[3])
        if (P1_ones.count('1') % 2 == 0) and allBits[3] == '0':
            print("Parity Bit 4 is Correct.")
        elif P4_ones.count('1') % 2 != 0 and allBits[6] == '1':
        	print("Parity Bit 4 is Correct.")
        else:
            print("Parity Bit 4 is Incorrect!")
            self.error = True
            errorBit += (int(allBits[3]) * 4)



        #check error
        if self.error == True:
            print("\n Analyzing Error in parity.....")
            print(
                "Error located in bit " + str(errorBit) + "... Fixing error...")
            print("Error Fixed... Running check again....")
            self.error = False
            self.fixError(errorBit)

            self.check()
        else:
            print("Test successful... Hamming Code output = " + self.bits)

    def fixError(self, errorBit):

        allBits = list(self.bits)
        if allBits[7 - errorBit] == '1':
            allBits[7 -errorBit] = '0'
        else:
            allBits[7 - errorBit] = '1'

        self.bits = ''.join(allBits)
        print(self.bits)


def main():

    data = input("Please enter a 7 bit hamming code:")
    entry = hammingCode(data)
    entry.check()


if __name__ == '__main__':
    main()
