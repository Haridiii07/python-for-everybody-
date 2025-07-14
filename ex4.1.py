hours = input("Enter your working hours: ")
rate = input("Enter your rate: ")

hrs = float(hours)
rt = float(rate)

def computepay(hours, rate): 
    if hours <= 40: 
        pay = hours * rate
    else: 
        regular_pay = 40 * rate
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * rate * 1.5
        pay = regular_pay + overtime_pay
    return pay 

gross_pay = computepay(hrs, rt)

print("Pay:", gross_pay)
