import math
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
class Window(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        self.width = 400
        self.height = 400
        self.resize(self.width,self.height)
        self.move(250,250)
        self.img = QImage(self.width,self.height,QImage.Format_ARGB32)

        self.pixelsInCircle = 0
        self.circleCenter = 200
        self.circleRadius = 200

        self.label = QLabel()
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

        self.setUpdatesEnabled(True)
        self.label.setUpdatesEnabled(True)
        self.drawCircle()
        self.show()
    def setPoint(self,x,y):
        dX = self.circleCenter - x;
        dY = self.circleCenter - y;
        distance = math.sqrt(dX*dX+dY*dY);
        if(distance <= self.circleRadius):
            color = Qt.red
            self.pixelsInCircle += 1
        else:
            color = Qt.blue
        painter = QPainter(self.img)
        painter.setBrush(QBrush(color))
        painter.drawEllipse(QPointF(x,y),2,2)
        painter.end()
    def drawCircle(self):
        painter = QPainter(self.img)
        painter.setPen(QPen(Qt.black))
        painter.drawEllipse(QPointF(self.circleCenter,self.circleCenter),self.circleRadius,self.circleRadius)
        painter.end()
    def getAmountOfPointsInCircle(self):
        return self.pixelsInCircle
    def updateScreen(self,pi):
        for x in range(44):
            for y in range(22):
                self.img.setPixel(x, y, QColor(255, 255, 255, 1).rgb())
        painter = QPainter(self.img)
        painter.setFont(QFont('Decorative',14))
        painter.setPen(QPen(Qt.green))
        painter.drawText(1,14,"{:2.2f}".format(pi))
        self.label.setPixmap(QPixmap.fromImage(self.img))
        self.label.update()
        self.update()
        if(math.fabs(pi - 3.14159) <= 10e-4):
            return True
        return False
    def clear(self):
        self.img = QImage(self.width,self.height,QImage.Format_ARGB32)
        self.pixelsInCircle = 0