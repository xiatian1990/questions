class MaxIntWithoutADigit():
	def solution(self, intNum):
		if intNum < 11 or intNum > 1000000000:
			return ValueError
		numToString = str(intNum)
		i = 0
		maxRes = 0
		while i < len(numToString):
			j = 1
			while i+j < len(numToString) and numToString[i] == numToString[i+j]:
				j += 1
			if j > 1:
				temp = int(numToString[:i+j-1] + numToString[i+j:])
				maxRes = max(maxRes, temp)

			i = i + j
		return maxRes

if __name__ == "__main__":
	a = MaxIntWithoutADigit()
	print a.solution(223336226)
	print a.solution(1100)