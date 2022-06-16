introstring=input("Enter your Introduction")
print(introstring)
charactercount=0
wordcount=1
for i in introstring:
    charactercount=charactercount+1
    print(charactercount)
    if (i==' '):
        wordcount=wordcount+1

print("number of words in a string",wordcount)
print("number of character count",charactercount)
    