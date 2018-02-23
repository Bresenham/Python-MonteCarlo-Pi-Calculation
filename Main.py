import sys, time, random
from PyQt5.QtWidgets import *
from Window import Window
from Halton import Halton
from Sobol import *

if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    window = Window()
    amount = 5
    vNums = 0
    n = 0
    times = []
    while(n < 1):
        start = time.time()
        for i in range(0,amount):
            #rndX = random.random()
            #rndY = random.random()
            #rndX = i4_sobol(2,i)[0][0]
            #rndY = i4_sobol(2,i)[0][1]
            rndX = Halton(2,i)
            rndY = Halton(3,i)
            if(rndX <= 1 and rndY <= 1 and rndX >= 0 and rndY >= 0):
                print(str(rndX) + ":" + str(rndY))
                rndX *= window.width
                rndY *= window.height
                window.setPoint(rndX,rndY)
                if(vNums > 0):
                    val = window.updateScreen(float((float(window.getAmountOfPointsInCircle() / float(vNums)))) * 4.0)
                    if(val):
                        break
                qApp.processEvents()
                vNums += 1
            else:
                print("i")
        end = time.time()
        times.append(end - start)
        n += 1
        vNums = 0
        window.clear()
    print(times)
    sys.exit(qApp.exec_())