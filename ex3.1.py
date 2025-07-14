#Overtime Pay Calculator
hrs = input("Enter Hours:")
rate = input("Enter Rate:")
fh = float (hrs)
fr = float (rate)
if fh > 40 :
    so0 = fr * fh
    so = (fh - 40.0) * (fr * 0.5) 
    xp = so0 + so
else:
    xp = fh * fr     
print (xp) 
