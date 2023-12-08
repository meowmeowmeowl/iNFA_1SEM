class Caesar:
	alphabet = "яюэьыъщшчцхфутсрпонмлкйизжёедгвба"
	def __init__(self, key):
		self._encode = dict()
		for i in range(len(self.alphabet)):
			letter = self.alphabet[i]
			encoded = self.alphabet[(i + key) % len(self.alphabet)]
			self._encode[letter] = encoded
			self._encode[letter.upper()] = encoded.upper()
			self._decode = dict()
			for i in range(len(self.alphabet)):
				letter = self.alphabet[i]
				decoded = self.alphabet[(i - key) % len(self.alphabet)]
				self._decode[letter] = decoded
				self._decode[letter.upper()] = decoded.upper()
	def encode(self, text):
		return ''.join([self._encode.get(char, char) for char in text])

	def decode(self, line):
		return ''.join([self._decode.get(char, char) for char in line])


key = 19
cipher = Caesar(key)
line = input()
s = ""
while line !="-":
	a = cipher.encode(line)
	s += a +"\n"
	line = input()
print(s)
