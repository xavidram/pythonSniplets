class parityCheck:

	def __init__(self, bits="0000000"):
		self.bits = list(bits)
		self.error = False
		self.errorBit = 0

	def analyze(self):
		self.parityBitAnalysis(1)
		self.parityBitAnalysis(2)
		self.parityBitAnalysis(4)

		if self.error == True:
			self.error = False
			print("\nError found in bit " + str(self.errorBit) + "... Fixing Error...\n")
			self.fixError()
			print("Rerunning parity analysis....")
			self.analyze()
		else:
			print("Test Complete!")
			print("Output => " + ''.join(self.bits))

	def parityBitAnalysis(self, P):
		try:
			if P == 1:
				"""
				Parity bit 1 analysis
				P1 = {D3,D5,D7}
				"""
				p1Data = self.bits[0]+ self.bits[2]+ self.bits[4]
				self.parityAnalysis(p1Data, "1" , self.bits[6])
			elif P == 2:
				"""
				Parity bit 2 analysis
				P2 = {D3,D6,D7}
				"""
				p2Data = self.bits[0]+ self.bits[1]+ self.bits[4]
				self.parityAnalysis(p2Data, "2", self.bits[5])
			elif P == 4:
				"""
				Parity bit 4 analysis
				P4 = {D5,D6,D7}
				"""
				p4Data = self.bits[0]+ self.bits[1]+ self.bits[2]
				self.parityAnalysis(p4Data, "4", self.bits[3])
			else:
				#Error, no other parity bits available besides 1,2 and 4
				print("Error: Parity Bit not valid!")
		except Exception as e:
			print(str(e))

	def parityAnalysis(self, pdata, p, pval):
		print("Data for Parity Bit " + p + " = { " + pdata + " }")
		print("P1 currently = " + pval)

		if pdata.count('1') % 2 == 0 and pval == '0':
			print("Parity Bit " + p + " is Correct...")
		elif pdata.count('1') % 2 != 0 and pval == '1':
			print("Parity Bit " + p + " is Correct...")
		else:
			print("Parity Bit " + p + " is Incorrect!")
			self.errorBit += (int(pval) * int(p))
			self.error = True

	def fixError(self):
		if self.bits[7 - self.errorBit] == '1':
			self.bits[7 - self.errorBit] = '0'
		else:
			self.bits[7 - self.errorBit] = '1'

#Main Function
def main():
	bits = input("Please enter a 7-bit hamming code:  ")
	data = parityCheck(bits)
	data.analyze()

if __name__ == '__main__':
	main()