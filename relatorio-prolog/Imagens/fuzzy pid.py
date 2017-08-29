import matplotlib.pyplot as plt
from pyswip import Prolog
import random
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
erro = 0.0
erroacumulado = 0.0
setpoint = 0.0
sg = [0.0]
k=0

prolog.assertz("tanque(E,Kp,Ki):- E>(-30), E<0, Kp is 0.9, Ki is 0.01")
prolog.assertz("tanque(E,Kp,Ki):- E=<(-30), Kp is 0.01, Ki is 0.001")
prolog.assertz("tanque(E,Kp,Ki):- E>=0, E<30, Kp is 0.9, Ki is 0.01")
prolog.assertz("tanque(E,Kp,Ki):- E>=30, Kp is 0.1, Ki is 0.001")

setpoint = float(input("Qual o nivel desejado?\n"))


for i in range(0,50000):
    sg.append(setpoint)
    erro = setpoint - L2[0]
    erroacumulado = erroacumulado + erro

    for solution in prolog.query("tanque("  + str(erro) + ", X, Y)"):
        Kp = solution["X"]
        Ki = solution["Y"]
    
    u = Kp*erro + Ki*erroacumulado
    ug.append(u)
    
    L1[1] = L1[0]
    L2[1] = L2[0]
    
    L1[0] = 0.99346032*L1[1] + 0.01477313*(ug[-1]+ug[-2])
    L2[0] = 0.99346032*L2[1] + 0.00326984*(L1[0]+L1[1])

    yg.append(L2[0])

    if (erro < 0.000001):
        if (erro > 0):
            setpoint = random.randint(5,23)
            k = k+1
            if (k>=5):
                break

t = [t for t in range(len(yg))]

print 'erro = ' + str(erro)
print 'erro acumulado = ' + str(erroacumulado)
plt.plot(t,yg,label='nivel',color='r')
plt.plot(t,ug,label='sinal de controle',color='blue')
plt.plot(t,sg,label='setpoint',color='k')
plt.legend()
plt.show()
