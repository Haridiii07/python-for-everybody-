#Safe Overtime Pay Calculator
hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try :
     fh = float (hrs)
     fr = float (rate)
except :
    print ("Error, please enter numeric input")
    quit ()     
if fh > 40 :
    so0 = fh * fr
    so = (fh - 40.0) * (fr * 0.5) 
    xp = so0 + so
else:
    xp = fh * fr     
print (xp) 
