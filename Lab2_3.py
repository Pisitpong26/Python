class TorKham:

	def __init__(self):
		self.words = []

	def restart(self):
		self.words = []
		return "game restarted"

	def play(self, word):
		word = word[2:]
		if len(self.words) == 0:
			self.words.append(word)
			return "'{}'".format(word) + " -> " + str(self.words)
		else:
			x = word
			y = self.words
			for i in range(len(self.words)):
				if word != self.words[i]:
					if x[0].upper() == y[i][len(y[i])-2].upper():
						if x[1].upper() == y[i][len(y[i])-1].upper():
							self.words.append(word)
							return "'{}'".format(word) + " -> " + str(self.words)
						else:
							return "'{}'".format(word) + " -> " + "game over"
					else:
						return "'{}'".format(word) + " -> " + "game over"
				else:
					return "'{}'".format(word) + " -> " + "game over"


torkham = TorKham()

print("*** TorKham HanSaa ***")


S = input("Enter Input : ").split(',')

for i in range(len(S)):
	if S[i] == 'R':
		torkham.restart()
		print(torkham.restart())
	elif S[i] == 'X':
		break
	elif S[i][0] == 'P':
		print(torkham.play(S[i]))
	else:
		print("'{}'".format(S[i])+" is Invalid Input !!!")
		break
