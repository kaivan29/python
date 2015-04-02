
fi = open("range.txt",'r')
fo = open("text.txt",'w')

for line in fi:
    print line
    s = sum([x for x in (range(int(line))) if x%3==0 or x%5==0])
    print s
fo.close()

