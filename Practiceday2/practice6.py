#if-elif-elif-else
#แบบฝึกหัด 3-6 ข้อที่ 1
#มีตัวแปร bmi เก็บจำนวนจริง จงเขียนคำสั่งให้แสดงข้อความตามค่าของ bmi
#กำหนด bmi ดังนี้
#bmi = 0 - 15 แสดง Very severely underweight
#bmi = 15 - 16 แสดง Severely underweight
#bmi = 16 - 18.5 แสดง Underweight
#bmi = 18.5 - 25 แสดง Normal
#bmi = 25 - 30 แสดง Overweight
#bmi = >30 แสดง Obese
bmi = float(input())
if bmi <= 15:
    msg = "Very severely underweight"
elif bmi <= 16:
    msg = "Severely underweight"
elif bmi <= 18.5:
    msg = "Underweight"
elif bmi <= 25:
    msg = "Normal"
elif bmi <= 30:
    msg = "Overweight"
else:
    msg = "Obese"
print(msg)