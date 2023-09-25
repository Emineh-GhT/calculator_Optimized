from functools import partial # yek parametr be tavabe bedim

from PySide6.QtCore import * 
from PySide6.QtWidgets import * 
from PySide6.QtGui import * 
from PySide6.QtUiTools import QUiLoader

from math import *



class Calculator(QMainWindow):

    def __init__(self):
        super().__init__()
        self.loader = QUiLoader()
        self.ui = self.loader.load('design.ui' , None)
        self.ui.show()
        self.result = 0
        self.operation = ''

        self.screen = [ [self.ui.b_ac , self.ui.b_pm , self.ui.b_p , self.ui.b_d , self.ui.b_sin] ,
                        [self.ui.b7 , self.ui.b8 , self.ui.b9 , self.ui.b_m , self.ui.b_cos ] ,
                        [self.ui.b4 , self.ui.b5 , self.ui.b6 , self.ui.b_sub , self.ui.b_tan ] ,
                        [self.ui.b1 , self.ui.b2 , self.ui.b3 , self.ui.b_sum , self.ui.b_cot ] ,
                        [self.ui.b0 , self.ui.b00 , self.ui.b_dot , self.ui.b_sqrt , self.ui.b_log] ] # yek araye 5*5
        
        for i in range(5):
            for j in range(5):
                self.screen[i][j].clicked.connect(partial(self.click , i , j))

        self.ui.b_equal.clicked.connect(self.equal)

    
    def click(self , i , j ):
         
        if self.screen[i][j] == self.ui.b_ac :
            self.ui.text_box.setText("")
            self.result=0
            self.opration=""

        if self.screen[i][j] == self.ui.b_pm :
            try:
                self.num2=float(self.ui.text_box.text())
                self.num2 *=-1
                self.ui.text_box.setText(str(self.num2))
            except:
                self.ui.text_box.setText("Enter a number")
                self.result = 0

        if self.screen[i][j] == self.ui.b_p:
            try:
                self.ui.text_box.setText(str(float(self.ui.text_box.text())/100))
            except:
                self.ui.text_box.setText("Enter a number")
                self.result = 0

        if self.screen[i][j] == self.ui.b_d :
            try:
                self.result=float(self.ui.text_box.text())
                self.ui.text_box.setText("")
                self.opration="/"
            except:
                self.ui.text_box.setText("Enter a number")
                self.result = 0

        if self.screen[i][j] == self.ui.b_sin :
            try:
                self.result = float(self.ui.text_box.text())
                self.result = self.result/360 *2 * pi
                self.result = round(sin(self.result),5)
                self.ui.text_box.setText(str(self.result))
                self.oparation = 'sin'
            except:
                self.ui.text_box.setText("Enter an angle")
                self.result = 0
            
        if self.screen[i][j] == self.ui.b7 :
            self.ui.text_box.setText(self.ui.text_box.text() + "7")
            
        if self.screen[i][j] == self.ui.b8 :
            self.ui.text_box.setText(self.ui.text_box.text() + "8")
            
        if self.screen[i][j] == self.ui.b9 :
            self.ui.text_box.setText(self.ui.text_box.text() + "9")
            
        if self.screen[i][j] == self.ui.b_m :
            try:
                self.result=float(self.ui.text_box.text())
                self.ui.text_box.setText("")
                self.opration="*"
            except:
                self.ui.text_box.setText("Enter a number")
                self.result = 0
            
        if self.screen[i][j] == self.ui.b_cos : 
            try:
                self.result = float(self.ui.text_box.text())
                self.result = self.result/360 *2 * pi
                self.result = round(cos(self.result),5)
                self.ui.text_box.setText(str(self.result))
                self.oparation = 'cos'
            except:
                self.ui.text_box.setText("Enter an angle")
                self.result = 0
        
        if self.screen[i][j] == self.ui.b4 :
            self.ui.text_box.setText(self.ui.text_box.text() + "4")
        
        if self.screen[i][j] == self.ui.b5 :
            self.ui.text_box.setText(self.ui.text_box.text() + "5")
        
        if self.screen[i][j] == self.ui.b6 :
            self.ui.text_box.setText(self.ui.text_box.text() + "6")
        
        if self.screen[i][j] == self.ui.b_sub :
            try:
                self.result=float(self.ui.text_box.text())
                self.ui.text_box.setText("")
                self.opration="-"
            except:
                self.ui.text_box.setText("Enter a number")
                self.result = 0
        
        if self.screen[i][j] == self.ui.b_tan :
            try:
                self.result = float(self.ui.text_box.text())
                self.result = self.result/360 *2 * pi
                self.result = round(tan(self.result),5)
                self.ui.text_box.setText(str(self.result))
                self.oparation = 'tan'
            except:
                self.ui.text_box.setText("Enter an angle")
                self.result = 0
        
        if self.screen[i][j] == self.ui.b1 :
            self.ui.text_box.setText(self.ui.text_box.text() + "1")

        if self.screen[i][j] == self.ui.b2 :
            self.ui.text_box.setText(self.ui.text_box.text() + "2")

        if self.screen[i][j] == self.ui.b3 :
            self.ui.text_box.setText(self.ui.text_box.text() + "3")

        if self.screen[i][j] == self.ui.b_sum :
            try:
                self.result=float(self.ui.text_box.text())
                self.ui.text_box.setText("")
                self.opration="+"
            except:
                self.ui.text_box.setText("Enter a number")
                self.result = 0
        
        if self.screen[i][j] == self.ui.b_cot :
            try:
                self.result=float(self.ui.text_box.text())
                self.result=self.result/360 *2 * pi
                self.result=round(atan(self.result),5)
                self.ui.text_box.setText(str(self.result))
                self.oparation = 'cot'
            except:
                self.ui.text_box.setText("Enter an angle")
                self.result = 0
        
        if self.screen[i][j] == self.ui.b0 : 
            self.ui.text_box.setText(self.ui.text_box.text() + "0")

        if self.screen[i][j] == self.ui.b00 :
            self.ui.text_box.setText(self.ui.text_box.text() + "00")

        if self.screen[i][j] == self.ui.b_dot :
            if '.' not in self.ui.text_box.text():
                self.ui.text_box.setText(self.ui.text_box.text() + '.')

        if self.screen[i][j] == self.ui.b_sqrt :
            try:
                self.ui.text_box.setText(str(sqrt(float(self.ui.text_box.text()))))
            except:
                self.ui.text_box.setText("Enter a number")
                self.result = 0

        if self.screen[i][j] == self.ui.b_log :
            try:
                self.ui.text_box.setText(str(log10(float(self.ui.text_box.text()))))
            except:
                self.ui.text_box.setText("Enter a number")
                self.result = 0
                 

    def equal(self):
        self.num2 = float(self.ui.text_box.text())
        if self.opration == "+":
            self.result +=self.num2
            self.ui.text_box.setText(str(self.result))
            self.opration= ""
            self.result=0
        elif self.opration == "-":
            self.result -=self.num2
            self.ui.text_box.setText(str(self.result))
            self.opration= ""
            self.result=0
        elif self.opration == "*":
            self.result *= self.num2
            self.ui.text_box.setText(str(self.result))
            self.opration= ""
            self.result=0
        elif self.opration == "/":
            try:
                self.result /= self.num2
                self.ui.text_box.setText(str(self.result))
                self.opration= ""
                self.result=0
            except:
                self.ui.text_box.setText("")
                self.opration= ""
                self.result=0
        else:
            self.result = self.num2




app = QApplication([]) #yek aplication mitone chand window dashte bashe
window = Calculator()
app.exec() #baz baqi mondan