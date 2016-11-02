"""
	Author: Xavid Ramirez
	Date: November 2, 2016
	Desc: Hamming word encoding and decoding program. The python program
		  Will take either a set of bits to encode or decode. Encode will
		  encode the bits into Hamming Encoding. Decoding will check the 
		  given bits, check the parities, fix parities if needed, return
		  the correct word, and return the unencoded bit word. 
	
	Dependencies: Python 3

"""

class Hamming:

	def __init__(self):
		self.query()

	def query(self):
		""" Prompt user if they would like to encode or decode, then begin process for that subclass """
		command = input("Would you like to Encode or Decode? ")

		if "encode" in command.lower():
			bits = input("Please enter the bit word to be encoded in hamming code: ")
			data = Encode(bits)
			data.start()
		elif "decode" in command.lower():
			bits = input("\nPlease enter the bit word to be decoded in hamming code: ")
			print("\n")
			data = Decode(bits)
			data.analyze()
		else:
			#If user enters invalid command, run to here and close program.
			print("You entered an invalid command!")

class Encode:

	def __init__(self,bits=None):
		self.bits = list(bits) if bits != None else bits
		self.blank = True if bits == None else False
		self.MaxParity = self.encode_FindLargestParity()
		self.ErrorLog = []

	def encode(self,P):
		""" Function to encode the given Parity for given bits """
		pData = []
		if P == 1:
			#If parity bit is 1, then use slicing on the list to get the parity bits (every other bit, remove first bit)
			pData.extend(self.bits[::P+1])
			pData.pop(0)
			self.encode_setParityBit(pData,P)
		elif P in [2,4,8,16,32,64,128,256]:
			#For given Parity bit in range, and for range in j to p, pull out the bits for that parity
			# EX: Parity 2 => take two, ignore two, take two, ignore 2 etc...
			# EX: Parity 4 => take four, ignore four, take four, ignore 4 etc..
			for i in range( (P-1), len(self.bits), (P*2) ):
				for j in range(0,P):
					try:
						pData.append(self.bits[i+j])
					except IndexError:
						#Exception for index out of range to ErrorLog list of errors, just for logging purposes
						#List is known to hit out of range for large parity bits
						self.ErrorLog.append("During parity bit" + str(P) +" check. Index out of range at " + str(i+j))
			#Pop the first bit, as it is the parity, we need to find this parity, not encode it and it is set to NONE here
			pData.pop(0)
			#Run the encoding function for given Parity bit P
			self.encode_setParityBit(pData,P)

	def start(self):
		""" Prepair the list for encoding """
		"""
			1. For every location for a possible Parity,
			insert None into that specific location, shifting
			the next bit to the following location
			2. Now for every parity up to the Maximum Parity for
			the given bits, encode the Parity bit (find the parity for sequence)
			3. Print out the encoded output
		"""
		prepped = []
		prepped.extend(self.bits)
		for i in [1,2,4,8,16,32,64,128,256]:
			if i < self.MaxParity:
				prepped.insert(i-1,None)
			elif i == self.MaxParity:
				prepped.insert(i-1,None)
				break
		self.bits = prepped
		for i in [1,2,4,8,16,32,64,128,256]:
			if i == self.MaxParity:
				self.encode(i)
				break
			elif i == 1:
				self.encode(1)
			else:
				self.encode(i)
		print("Encoding Complete...\n")
		output = ''.join(self.bits)
		print("Output => " + output)

	def encode_setParityBit(self,pData,P):
		""" Encode the parity bit """

		#If number of 1's in parity bit sequence are even seto P to 0
		#otherwise set P to 1
		if pData.count('1') % 2 == 0:
			self.bits[P-1] = '0'
		elif pData.count('1') % 2 != 0:
			self.bits[P-1] = '1'

	def encode_FindLargestParity(self):
		"""For given range of bits, find the largest Possible Parity for given
		   number of bits """
		for i in [256,128,64,32,16,8,4,2,1]:
			if i <= len(self.bits):
				return i

class Decode:

	def __init__(self, bits=None):
		self.bits = list(bits) if bits != None else bits
		self.blank = True if bits == None else False
		self.error = False
		self.errorBit = 0
		self.MaxParity = self.decode_FindLargestParity()
		self.ErrorLog = []
		self.parityBits = []

	def decode_FindLargestParity(self):
		""" Find the largest possible parity for given bits """
		maxP = 0
		for i in [1,2,4,8,16,32,64,128,256]:
			if len(self.bits) - i >= 0:
				maxP = i
		return maxP

	def analyze(self):
		""" Decode the list for each parity up to the max parity possible for given bit sequence """
		for i in [1,2,4,8,16,32,64,128,256]:
			if i == self.MaxParity:
				self.decode(i)
				break
			else:
				self.decode(i)

		"""If there is an error, self.erroBit should contain the error bit, go and fix it, then re-analyze
			Other wise, the test is complete, go give out the decoded bits
		"""
		if self.error == True:
			self.error = False
			print("\nError found in bit " + str(self.errorBit) + "... Fixing Error...\n")
			self.FixError()
			print("Rerunning parity analysis....")
			self.analyze()
		else:
			print("\nTest Complete!")
			print("\nCorrected encoded bits => " + ''.join(self.bits))

			#Go print out decoded word
			self.outputDecodedWord()

	def outputDecodedWord(self):
		""" Print out decoded bit sequence """
		output = self.bits
		for i in [256,128,64,32,16,8,4,2,1]:
			if i <= self.MaxParity:
				output.pop(i-1)
		output = ''.join(output)
		print("Decoded bits => " + output)

	def decode(self,P):
		"""Decode"""
		pData = []
		pVal = 0
		if P == 1:
			#If parity bit is 1, then use slicing on the list to get the parity bits (every other bit, remove first bit)
			pData.extend(self.bits[::P+1])
			pVal = pData[0]
			pData.pop(0)
			self.parityAnalysis(pData,P,pVal)
		elif P in [2,4,8,16,32,64,128,256]:
			#For given Parity bit in range, and for range in j to p, pull out the bits for that parity
			# EX: Parity 2 => take two, ignore two, take two, ignore 2 etc...
			# EX: Parity 4 => take four, ignore four, take four, ignore 4 etc..
			for i in range( (P-1), len(self.bits), (P*2) ):
				for j in range(0, P):
					try:
						pData.append(self.bits[i+j])
					except IndexError:
						self.ErrorLog.append("During parity bit" + str(P) +" check. Index out of range at " + str(i+j))
			pVal = pData[0]
			#Pop the first bit, this is the bit that will be analyzed and corected if needed.
			pData.pop(0)
			self.parityAnalysis(pData,P,pVal)

	def parityAnalysis(self, pData, P, pVal):
		""" This function alayzes the sequence for a Given parity, the value of the parity and marks erro if Parity is incorrect """
		print("Data for Parity Bit " + str(P) + " = { " + str(pData) + " }")
		print("P" + str(P) + " currently = " + str(pVal))

		"""
			If number of 1's are odd and Parity is 1 then there is no error
			If number of 1's are even and Parity is 0 then there is no error
			Otherwise it is Incorrect, mark error flag
			Calculate the errorBit
		"""
		if pData.count('1') % 2 == 0 and pVal == '0':
			print("Parity Bit " + str(P) + " is Correct...\n")
		elif pData.count('1') % 2 != 0 and pVal == '1':
			print("Parity Bit " + str(P) + " is Correct...\n")
		else:
			print("Parity Bit " + str(P) + " is Incorrect!\n")
			self.errorBit += (int(pVal) * int(P))
			self.error = True

	def FixError(self):
		""" Flip the value of the Error bit """
		if self.bits[self.errorBit] == '1':
			self.bits[self.errorBit] = '0'
		else:
			self.bits[self.errorBit] = '1'

def main():
	hamming = Hamming()

if __name__ == '__main__':
	main()
