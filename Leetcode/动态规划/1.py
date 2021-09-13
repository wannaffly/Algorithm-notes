while 1:
    a=[]  
    s = input()

    if s != "":
        for x in s.split():  
            a.append(int(x))  

        print(sum(a))
    else:
        break


while 1:
	N,M = map(int,input().split())
	res = []
	for i in range(M):
		a,b,c = map(int,input().split())
		if c == 1:
			r = [a,b] if a<b else [b,a]
			res.append(r)
	s = set()
	s.add(1)
	res.sort()
	for i in res:
		if i[0] in s:
			s.add(i[1])
	print(len(s)-1)

while 1:
    a=[]  
    s = input()

    if s != "":
        for x in s.split():  
            a.append(int(x))  

        print(sum(a))
    else:
        break

a = 1
N,M = map(int,input().split())