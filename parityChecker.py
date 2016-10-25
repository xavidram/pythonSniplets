class data:

	def _init__(self, bits="0000000"):
		self.bits = list(bits)

	def analyze(self):

	def parityBitAnalysis(self, P):

		if P == 1:
			"""
			Parity bit 1 analysis
			P1 = {D3,D5,D7}
			"""
			p1Data = []
			p1Data.extend(self.bits[0] ,self.bits[2] , self.bits[4])

			self.analysDesc(p1Data, "1" , self.bits[6])


		elif P == 2:
			"""
			Parity bit 2 analysis
			P2 = {D3,D6,D7}
			"""

		elif P == 4:
			"""
			Parity bit 4 analysis
			P4 = {D5,D6,D7}
			"""

		else:
			#Error, no other parity bits available besides 1,2 and 4
			print("Error: Parity Bit not valid!")

	def analysDesc(self, pdata, p, pval):
		print("Data for Parity Bit " + p + " = { " + pdata + " }")
		print("P1 currently = " + pval)

	def parityAnalysis(self, pdata, p, pval):
		if pdata.count('1') % 2 == 0 and pval == '0':
			print("Parity Bit " + p + " is Correct...")
		elif pdata.count('1') % 2 != 0 and pval == '1':
			print("Parity Bit " + p + " is Correct...")
		else:
			print("Parity Bit " + p + " is Incorrect!")
			self.errorBit += (int(pval) * )