import matplotlib.pyplot as plt
from pyswip import Prolog
prolog = Prolog()

L1 = [0.0]
L2 = [0.0]
yg = []
ug = []
L1.append(0.0)
L2.append(0.0)
yg.append(0)
ug.append(0)
u = []
u.append(0.0)


#prolog.assertz("tanque(N,E):- N>=17, E is -8")
#prolog.assertz("tanque(N,E):- N>=12, N<17, E is 0")
#prolog.assertz("tanque(N,E):- N>=8, N<12, E is 2")
#prolog.assertz("tanque(N,E):- N>=2, N<8, E is 8")
#prolog.assertz("tanque(N,E):- N>=0, N<2, E is 15")

prolog.assertz("tanque(N,E):- N>=10, N=<20, E is 2")
prolog.assertz("tanque(N,E):- N<10, E is 4")
prolog.assertz("tanque(N,E):- N>20, E is 0")



for i in range(0,2000):
    #i = i + 1
    for solution in prolog.query("tanque("  + str(L2[0]) + ", X)"):
        u = solution["X"] #u eh inteiro
    ug.append(u)
    
    L1[1] = L1[0]
    L2[1] = L2[0]
    
    L1[0] = 0.99346032*L1[1] + 0.01477313*(ug[-1]+ug[-2])
    L2[0] = 0.99346032*L2[1] + 0.00326984*(L1[0]+L1[1])

    yg.append(L2[0])

print 'nivel = ' + str(yg)
print 'sinal de controle = ' + str(ug)

t = [t for t in range(len(yg))]

#print len(yg)
#print len(t)
#print len(ug)
plt.plot(t,yg,label='nivel',color='r')
plt.plot(t,ug,label='sinal de controle',color='blue')
plt.legend()
plt.show()
