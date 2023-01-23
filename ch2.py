math = open('mat_dv.txt','r')
max = 0
winner = ""
for i in math:
     if max < int(i.split()[4]) + int(i.split()[3]):
        winner = " ".join(i.split()[0:3])
        max = int(i.split()[4]) + int(i.split()[3])
print(winner,max)
math.close()
math = open('mat_dv.txt','r')
max_al = 0
max_ge = 0
winners = {'albebra':[0,''],'geometria':[0,'']}
for i in math:

    if int(i.split()[-2]) > winners['albebra'][0]:
        winners['albebra'][0] = int(i.split()[-2])
        winners["albebra"][1]=(" ".join(i.split()[0:3]))
    if int(i.split()[-1]) > winners['geometria'][0]:
        winners['geometria'][0] = int(i.split()[-1])
        winners["geometria"][1] = (" ".join(i.split()[0:3]))
print(winners["albebra"][0],winners["albebra"][1])
print(winners["geometria"][0],winners["geometria"][1])
math.close()


