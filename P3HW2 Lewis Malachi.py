#CTI-110
#P3HW2- Salary
#Malachi Lewis
#10/26/2023
#Design structres

Name= input("Name of  Employee: ")
hours = float(input("Hours worked: "))
pay_rate= float(input("Pay rate: "))
pay=hours * pay_rate
overtime= 0
overpay= 0

if hours >= 40:
    overtime = hours - 40
    overpay = overtime * (pay_rate* 1.5)
    regpay= hours * pay_rate
    pay = (hours - overtime) * pay_rate
Grosspay = overpay + pay
print("Employee Name:", Name)
print("Hours worked:", hours)
print("Pay Rate:", pay_rate)
print("OverTime:", overtime)
print("OverTime Pay:", overpay)
print("RegHour Pay:", pay)
print("Gross Pay:", Grosspay)
