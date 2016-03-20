class Solution():
	def imgPathSum(self, inputStr):
		paths = []
		stack = []
		entries = inputStr.split("\n")
		
		for i in range(len(entries)):
			path = ""
			if len(stack) == 0:
				path = self.handleEntry(entries[i], stack)
			else:
				curSpcNum = entries[i].count(" ")
				parentSpcNum = stack[-1].count(" ")

				if curSpcNum - parentSpcNum == 1:
					path = self.handleEntry(entries[i], stack)

				if curSpcNum == parentSpcNum:
					stack.pop()
					path = self.handleEntry(entries[i], stack)

				if curSpcNum < parentSpcNum:
					for j in range(parentSpcNum - curSpcNum + 1):
						stack.pop()
					path = self.handleEntry(entries[i], stack)
			if path and path not in paths:
				paths.append(path)

		if len(paths) == 0:
			return 0
		else:
			return sum([len(path) for path in paths])

	def handleEntry(self, entry, parentList):
		path = ""
		if self.isFile(entry):
			if self.isImg(entry):
				path = self.getImgPath(parentList)
		else:
			parentList.append(entry)
		
		return path

	def getImgPath(self, parentList):
		if len(parentList) == 0:
			path = "/"
		else:
			path = ""
			for each in parentList:
				path = path+"/"+each.strip()
		return path

	def isFile(self, inputStr):
		return "." in inputStr

	def isImg(self, inputStr):
		return ".jpeg" in inputStr or ".png" in inputStr or ".gif" in inputStr

if __name__ == '__main__':
	a = Solution()
	pathSum = a.imgPathSum("img.gif\ndir1\n dir11\n dir12\n  picture.jpeg\n  dir121\n  filel.txt\ndir2\n file2.gif\n123.gif")
	print pathSum

#input format: "dir1\n dir11\n dir12\n  picture.jpeg\n  dir121\n  filel.txt\ndir2\n file2.gif";