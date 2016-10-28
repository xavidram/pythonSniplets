class HammingCode:

	def __init__(self, bits=None):
		self.bits = list(bits) if bits != None else bits
		self.blank = True if bits == None else False
		self.error = False
		self.errorBit = 0
		self.largestBit = 0

	def prepEncode(self):
		prepped = []
		prepped.extend(self.bits)
		for i in [0,1,3,7,15]:
			prepped.insert(i,None)
		#print(prepped)
		self.bits = prepped
		#for i in [1,2,4,8,16]:
		#	self.encode(i)
		self.selfEncode(1)

	def selfEncode(self,P):
		pData = []
		if P == 1:
			pData.extend(self.bits[::P+1])
			pData.pop(0)
			#self.set_parityBit(pData,P)
			print(self.bits)
			print(pData)
		elif P in [2,4,8,16,32,64,128,256]:
			for i in range( (P-1), len(self.bits), (P*2) ):
				for j in range(0,P):
					try:
						pData.append(self.bits[i+j])
					except IndexError:
						print("Index out of range at " + (i+j))

			print(self.bits)
			print(pData)

	def set_parityBit(self,pData,P):
		if pData.count('1') % 2 == 0:
			self.bits[P-1] = '0'
		elif pData.count('1') % 2 != 0:
			self.bits[P-1] = '1'

	def encode(self,P):
		if self.bits != None:
			try:
				if P == 1:
					"""
					Parity bit 1 analysis
					P1 = (3,5,7,9,11,13,15,17,19,21)
					- Check one skip one check one , etc..
					"""
					pData = []
					pData.extend(self.bits[::P+1])
					pData.pop(0)

				elif P == 2:
					"""
					P2 = {3,6,7,10,11,14,15,18,19}
					- check 2, skip 2, check 2 , etc...
					"""
					pData = []
					[ pData.extend([self.bits[i], self.bits[i+1] ]) for i in range(P-1,len(self.bits),4) ]
					pData.pop(0)
					print(self.bits)
					print(pData)
				elif P == 4:
					"""
					P4 = {4,5,6,7,12,13,14,15,20,21}
					- check 4, skip 4, check 4, etc...
					"""
					pData = []

				elif P == 8:
					"""
					P8 = {8,9,10,11,12,13,14,15}
					- check 8, skip 8, skip 8, etc...
					"""

				elif P == 16:
					"""
					P16 = {16,17,18,19,20,21}
					- check 16, skip 16, check 16, etc...
					"""

				else:
					#Should not get here...
					print("Error: Parity bit not valid!")

			except Exception as e:
				print(str(e))

		else:
			print("Canot encode => Invalid data:")

def main():
	bits = input("Please enter a 16 bit word: ")
	data = HammingCode(bits)
	data.prepEncode()

if __name__ == '__main__':
	main()

