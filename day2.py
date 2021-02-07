try:
   n =float(input("Enter ur height in feet:"))
   if n >= 6.5:
       print("allowed")
   else:
       print("not allowed")
except ValueError:
   print("its a string")
