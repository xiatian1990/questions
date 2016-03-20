class Solution():
	def imgPathSum(self, inputStr):
		res = 0
		paths = []
		stack = []
		entries = inputStr.split("\n")
		for i in range(len(entries)):
			if self.isFile(entries[i]):
				if self.isImg(entries[i]):
					if len(stack) == 0:
						path = "/"
					else:
						path = ""
						for each in stack:
							path = path+"/"+each.strip()
					if path not in paths:
						paths.append(path)
			else:
				if len(stack) == 0:
					stack.append(entries[i]) 
				else:
					curSpcNum = entries[i].count(" ")
					parentSpcNum = stack[-1].count(" ")

					if curSpcNum - parentSpcNum == 1:
						stack.append(entries[i])

					if curSpcNum < parentSpcNum:
						for j in range(parentSpcNum - curSpcNum):
							stack.pop()

		print paths
		if len(paths) == 0:
			return 0
		else:
			return sum([len(path) for path in paths]) 

	def isFile(self, inputStr):
		return "." in inputStr

	def isImg(self, inputStr):
		return ".jpeg" in inputStr or ".png" in inputStr or ".gif" in inputStr

if __name__ == '__main__':
	a = Solution()
	pathSum = a.imgPathSum("img.png\ndir1\n dir11\n dir12\n  picture.jpeg\n  dir121\n  filel.txt\ndir2\n file2.gif\n123.gif")
	print pathSum

#input format: "dir1\n dir11\n dir12\n  picture.jpeg\n  dir121\n  filel.txt\ndir2\n file2.gif";