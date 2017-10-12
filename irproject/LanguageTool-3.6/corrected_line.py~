import os,sys
queryno=1
word_list = sys.argv[1:]
inp = ' '.join(word for word in word_list)
fp=open(".queries","w")
fp.write(inp)
fp.close();
os.system(str("cat .queries| java -jar languagetool-commandline.jar -l en-GB -a -  > output"+str(queryno)+".txt"))
question=(open("output"+str(queryno)+".txt")).readline()
msg= "Corrected question"
filename="output" + str(queryno) +".txt" 
print msg
print "="*len(msg)
print question
print "\n"
os.system(str("cat " +str(filename)+" | python ../dbpedia/main.py "+str(question)))
queryno+=1
