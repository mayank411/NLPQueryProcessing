import sys

print str(sys.argv)
word_list = sys.argv[1:]
print ' '.join(word for word in word_list)

