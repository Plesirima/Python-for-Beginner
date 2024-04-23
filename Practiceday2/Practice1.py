#Flowchart & if-else
#แบบฝึกหัด 3-1 ข้อที่ 1
a = int(input())
b = int(input())
if a < b:
  min = a
  max = b
else:
  min = b
  max = a
print(min, max)


#แบบฝึกหัด 3-1 ข้อที่ 2

a = int(input())
b = int(input())

if abs(a-b) > 2:
    a,b = b,a
else:
    a = b**2 + a
print(a,b)

