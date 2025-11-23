print("-------------------------------------------")
print("        STUDENT REPORT CARD SYSTEM"         )
print("-------------------------------------------")

name=str(input("ENTER STUDENT NAME:"))
print("Enter Marks Out of 100")
php=int(input("php :"))
java=int(input("java :"))
dbms=int(input("dbms :"))
maths=int(input("maths :"))
network=int(input("networking :"))

print("Calculating Result...")

print("-------------------------------------------")
print("               REPORT CARD                 ")
print("-------------------------------------------")

print("Student Name :",name)


print("php         :",php)
print("java        :",java)
print("dbms        :",dbms)
print("maths       :",maths)
print("networking  :",network)

print("-------------------------------------------")

total=php+java+dbms+maths+network
print("Total Marks :",total, "/ 500")
per=total/5
print("Percentage  :",per,"%")
if per>= 40:
    status="Pass"
else :
    status="Failed"

if per >= 90 and per <= 100:
    grade = "A+"
elif per >= 80 and per < 90:
    grade = "A"
elif per >= 70 and per < 80:
    grade = "B+"
elif per >= 60 and per < 70:
    grade = "B"
elif per >= 50 and per < 60:
    grade = "C"
elif per >= 40 and per < 50:
    grade = "D"
else:
    grade = "-"

print("grade     :",grade)
print("status    :",status)

print("-------------------------------------------")
print("                 THANK YOU                 ")
print("-------------------------------------------")
