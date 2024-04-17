#Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
#Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all 
#hours worked above 40 hours. Put the logic to do the computation of pay in a function called computepay() 
#and use the function to do the computation. The function should return a value. Use 45 hours and a rate of 
#10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and 
#float() to convert the string to a number. Do not worry about error checking the user input unless you want 
#to - you can assume the user types numbers properly. Do not name your variable sum or use the sum() function.

def computepay(h, r):
    if(h > 40):
        overhrs = h - 40
        return (h - overhrs) * r + (overhrs * 1.5 * r)
    else:
        return h * r

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)

p = computepay(h, r)
print("Pay", p)

#5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
# Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything 
# other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
# Enter 7, 2, bob, 10, and 4 and match the output below.

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break

    try:
        num = int(num)
    except:
        print("Invalid input")
        continue

    if largest is None or num > largest:
        largest = num

    if smallest is None or num < smallest:
        smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)