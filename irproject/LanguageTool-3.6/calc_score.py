import os
inp=raw_input("Enter input Folder name to calculate score:\n")

for root, dirs, files in os.walk(inp, topdown=False):
	for file_i in files:
		os.system(str("java -jar languagetool-commandline.jar -l en-GB "+root+"/"+file_i+" > output.txt"))
		start="Message: "
		spelling="spelling mistake" #0.2
		numspell=0.0
		typo="typo" #0.1
		numtypo=0.0
		#grammar1="instead of" 
		#numgrammar1=0.0
		#grammar2="Did you mean" #0.5
		numgrammar=0.0
		uppercase="uppercase letter"
		quote="quote here" 
		score=0.0
		with open("output.txt") as fp:
			for line in fp:
				k=line.find(start)
				if (k < 0):
					continue;
				else:
					print line
					t=line.find(spelling)
					if(t>=0):
						numspell+=1
						continue
					t=line.find(typo)
					if(t>=0):
						numtypo+=1
						continue
					t=line.find(quote)
					if(t>=0):
						continue
					t=line.find(uppercase)
					if(t>=0):
						continue
					numgrammar+=1

		total=(numspell+numtypo+numgrammar)
		if (total>0):
			score=(numspell*0.2 + numtypo*0.1 + numgrammar*0.5)/total
	#	print((numspell)
	#	print(numtypo)
		#print(numgrammar1)
	#	print(numgrammar)
		print("the input file has following score: ")
		print(score)
		print("**********************************************************")
