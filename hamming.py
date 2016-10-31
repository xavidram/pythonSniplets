class Hamming:

	def __init__(self):
		self.query()

	def query(self):
		command = input("Would you like to Encode or Decode? ")

		if "encode" in command.lower():
			bits = input("Please enter the bit word to be encoded in hamming code: ")
			data = Encode(bits)
			data.start()
		elif "decode" in command.lower():
			bits = input("Please enter the bit word to be decoded in hamming code: ")
			data = Decode(bits)
			data.analyze()
		else:
			print("You entered an invalid command!")

class Encode:

	def __init__(self,bits=None):
		self.bits = list(bits) if bits != None else bits
		self.blank = True if bits == None else False
		self.MaxParity = self.encode_FindLargestParity()
		self.ErrorLog = []

	def encode(self,P):
		pData = []
		if P == 1:
			pData.extend(self.bits[::P+1])
			pData.pop(0)
			self.encode_setParityBit(pData,P)
		elif P in [2,4,8,16,32,64,128,256]:
			for i in range( (P-1), len(self.bits), (P*2) ):
				for j in range(0,P):
					try:
						pData.append(self.bits[i+j])
					except IndexError:
						#print("Index out of range at " + str(i+j))
						self.ErrorLog.append("During parity bit" + str(P) +" check. Index out of range at " + str(i+j))
			pData.pop(0)
			self.encode_setParityBit(pData,P)

	def start(self):
		prepped = []
		prepped.extend(self.bits)
		print(self.MaxParity)
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

	def encode_setParityBit(self,pData,P):
		if pData.count('1') % 2 == 0:
			self.bits[P-1] = '0'
		elif pData.count('1') % 2 != 0:
			self.bits[P-1] = '1'

	def encode_FindLargestParity(self):
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
		for i in [1,2,4,8,16,32,64,128,256]:
			if len(self.bits) - i >= 0:
				self.MaxParity = i

	def analyze(self):
		for i in [1,2,4,8,16,32,64,128,256]:
			if i == self.MaxParity:
				self.decode(i)
				break
			else:
				self.decode(i)

		if self.error == True:
			self.error = False
			print("\nError found in bit " + str(self.errorBit) + "... Fixing Error...\n")
			self.FixError()
			print("Rerunning parity analysis....")
			self.analyze()
		else:
			print("Test Complete!")
			print("Output => " + ''.join(self.bits))

	def decode(self,P):
		pData = []
		pVal = 0
		if P == 1:
			pData.extend(self.bits[::P+1])
			pVal = pData[0]
			pData.pop(0)
			self.parityAnalysis(pData,P,pVal)
		elif P in [2,4,8,16,32,64,128,256]:
			for i in range( (P-1), len(self.bits), (P*2) ):
				for j in range(0, P):
					try:
						pData.append(self.bits[i+j])
					except IndexError:
						self.ErrorLog.append("During parity bit" + str(P) +" check. Index out of range at " + str(i+j))
			pVal = pData[0]
			pData.pop(0)
			self.parityAnalysis(pData,P,pVal)

	def parityAnalysis(self, pData, P, pVal):
		print("Data for PArity Bit " + str(P) + " = { " + str(pData) + " }")
		print("P" + str(P) + " currently = " + str(pVal))

		if pData.count('1') % 2 == 0 and pVal == '0':
			print("Parity Bit " + P + " is Correct...")
		elif pData.count('0') % 2 != 0 and pVal == '1':
			print("Parity Bit " + P + " is Correct...")
		else:
			print("Parity Bit " + P + " is Incorrect!")
			self.errorBit += (int(pVal) * int(p))
			self.error = True

	def FixError(self):
		if self.bits[self.errorBit] == '1':
			self.bits[self.errorBit] = '0'
		else:
			self.bits[self.errorBit] = '1'

def main():
	hamming = Hamming()

if __name__ == '__main__':
	main()
