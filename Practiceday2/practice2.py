#Relational Operator
#แบบฝึกหัด 3-2 ข้อที่ 1
# แสดงผลของการเปรียบเทียบว่า a เป็นจำนวนลบหรือไม่
a = int(input())
print(a < 0)

# แสดงผลของการเปรียบเทียบว่า h
# เป็นเลขชั่วโมงบนหน้าปัดนาฬิกาหรือไม่
h = int(input())
print(1<=h<=12)

# แสดงผลของการเปรียบเทียบว่า m เป็น
#  จำนวนเต็มบวกคี่ที่หารด้วย 3 ลงตัวหรือไม่
m = int(input())
print(m>0 and m%2 == 1 and m%3 == 0)

# แสดงผลของการเปรียบเทียบว่า url เก็บ
#  ชื่อเว็บไซต์ที่ลงท้ายด้วย .com หรือ .th หรือไม่
url = str(input())
print(url[-4:] == '.com' or url[-3:] == '.th')

#แบบฝึกหัด 3-2 ข้อที่ 2
weight = float(input())
height = float(input())
if weight <= 0 or height <= 0:
    print("Error")
else:
    hm = height/100
    bmi = weight/hm**2
    if bmi <= 18.5:
        print("Underweight")
    else:
        if bmi < 25:
         print("Normal")
        else:
           print("Overweight")
print("OK")
    
