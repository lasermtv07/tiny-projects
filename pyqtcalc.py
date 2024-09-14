#!/usr/bin/python3

#pyqtcalc
#(c) lasermtv07,2024
#under WTFPL (essentially equivalent to public domain)
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
import math

def romanToInt(num):
    s=0
    values={"m":1000,"d":500,"c":100,"l":50,"x":10,"v":5,"i":1}
    for j in values.keys():
        v=values[j]
        for i in values.keys():
            if (i+j) in num and i!=j:
                s+=(v-values[i])*num.count((i+j))
                num=num.replace(i+j,"")
        if j in num:
            s+=v*num.count(j)
            num=num.replace(j,"")
    return s
def intToRoman(num):
    o=""
    for i in range(math.floor(num/1000)): o+="m"
    num-=1000*o.count("m")
    for i in range(math.floor(num/500)): o+="d"
    num-=500*o.count("d")
    for i in range(math.floor(num/100)): o+="c"
    num-=100*o.count("c")
    for i in range(math.floor(num/50)): o+="l"
    num-=50*o.count("l")
    for i in range(math.floor(num/10)): o+="x"
    num-=10*o.count("x")
    for i in range(math.floor(num/5)): o+="v"
    num-=5*o.count("v")
    for i in range(num): o+="i"
    return o

app=QApplication([])
window=QWidget()
window.setGeometry(100,100,500,200)
window.setWindowTitle("mathin time")
layout=QVBoxLayout()

label=QLabel(window)
label.setText("mathin time")
label.setFont(QFont("Arial",16))
layout.addWidget(label)

isArabic=True
radLayout=QHBoxLayout()
dl=QLabel(window)
dl.setText("Numerical Script: ")
radLayout.addWidget(dl)
ar=QRadioButton("Arabic")
ar.setChecked(True)
ar.script="Arabic"
def arabic():
    global isArabic
    isArabic=True

ar.toggled.connect(arabic)
radLayout.addWidget(ar)

ar=QRadioButton("Roman")
ar.script="Roman"
def roman():
    global isArabic
    isArabic=False
ar.toggled.connect(roman)
radLayout.addWidget(ar)
layout.addLayout(radLayout)

res=QLabel(window)
res.setText("0")
res.setFont(QFont("Arial",16))

proLayout=QHBoxLayout()
inpt1=QLineEdit("")
proLayout.addWidget(inpt1)
op=QComboBox()
op.addItems(['+','-','*','/'])
proLayout.addWidget(op)
inpt2=QLineEdit("")
proLayout.addWidget(inpt2)
def handleProblem():
    global isArabic
    global inpt1
    global op
    global inpt2
    global res
    i1=inpt1.text()
    o=op.currentText()
    i2=inpt2.text()
    if isArabic:
        try:
            i1=float(i1)
            i2=float(i2)
            if o=='+':
                res.setText(str(i1+i2))
            elif o=='-':
                res.setText(str(i1-i2))
            elif o=='*':
                res.setText(str(i1*i2))
            elif o=='/':
                res.setText(str(i1/i2))
        except:
            res.setText("Error!")
    else:
        i1=romanToInt(i1.lower())

        print(i1)
        i2=romanToInt(i2.lower())

        print(i2)
        if o=='+':
            res.setText(intToRoman(i1+i2))
        elif o=='-':
            res.setText(intToRoman(i1-i2))
        elif o=='*':
            res.setText(intToRoman(i1*i2))
        elif o=='/':
            if i2==0:
                res.setText("Error!")
            else:
                res.setText(intToRoman(i1/i2))

eq=QPushButton("=")
proLayout.addWidget(eq)
eq.clicked.connect(handleProblem)
layout.addLayout(proLayout)

layout.addWidget(res)
window.setLayout(layout)
window.show()
app.exec_()
