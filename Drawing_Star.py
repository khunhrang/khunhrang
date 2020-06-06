import math
import turtle
import time

__Pen = turtle.Pen()


def drawStar(arms,walk):
    #ชุดคำสั่งวาดรูปดาว
    for __count in range(math.floor(arms)):
        #ลากเส้นตามทิศหัวลูกศร 100 pxs
        __Pen.forward(200)
        #หมุนหัวลูกศร
        __Pen.right(((360 / arms) * walk))

def checkStar(arms,walk):
    for i in range(2,(walk + 1)):
        if (arms % i == 0 and walk % i == 0):
            return 0
    return 1

#Get Start with Python
#วนซ้ำเพื่อรับค่า
while True:
    #กำหนดค่า จำนวนแฉก และ จำนวน walking step จากผู้ใช้
    arms = turtle.numinput('Arms','How many arms?',5,5)
    walk = turtle.numinput('Walk','How many step?',1,1,arms / 2)
    #ตรวจสอบความเป็นไปได้ของการวาดรูปดาว
    if checkStar(math.floor(arms), math.floor(walk)) :
        drawStar(arms, walk)
    else :
        #แสดงข้อความแจ้ง ว่าไม่สามารถวาดรูปดาวได้
        __Pen.write('Cannot draw')
    time.sleep(3)
    __Pen.clear()
