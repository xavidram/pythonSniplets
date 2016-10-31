class HammingCode:

	def __init__(self, bits=None):
		self.bits = list(bits) if bits != None else bits
		self.blank = True if bits == None else False
		self.error = False
		self.errorBit = 0
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

	def prepEncode(self):
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

	def decode_findLargestParity(self):
		MaxParity = 0
		for i in [1,2,4,8,16,32,64,128,256]:
			if len(self.bits) - i >= 0:
				MaxParity = i

	


def main():
	bits = input("Please enter a 16 bit word: ")
	data = HammingCode(bits)
	#data.prepEncode()
	#print(data.bits)

if __name__ == '__main__':
	main()

