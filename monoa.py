import random
#это из Штирлица
class Monoalphabet:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"  # FIXME

    def __init__(self, keytable):
        lowercase_code = {self.alphabet[i]:keytable[i] for i in range(len(self.alphabet))}
        uppercase_code = {self.alphabet[i].upper():keytable[i].upper() for i in range(len(self.alphabet))}
        self._encode = dict(lowercase_code)
        self._encode.update(uppercase_code)
        lower_decode = {keytable[i]:self.alphabet[i] for i in range(len(self.alphabet))}
        uppercase_decode = {keytable[i].upper():self.alphabet[i].upper() for i in range(len(self.alphabet))}
        self._decode = dict(lower_decode)
        self._decode.update(uppercase_decode)
    def encode(self, line):
        if len(line) == 1:
            return self._encode[line] if line in self._encode else line
        else:
            return ''.join([self.encode(char) for char in line])

    def decode(self, line):
        if len(line) == 1:
            return self._decode[line] if line in self._decode else line
        else:
            return ''.join([self.decode(char) for char in line])



key = "птхиёшцрыязэчджвфгмущюьоксеaйбанл"
cipher = Monoalphabet(key)
line = input()
s = ""
s2 = ""
while line !="-":
	a = cipher.encode(line)
	b = cipher.decode(a)
	s += a +"\n"
	s2 += b + "\n"
	line = input()
print(s)
