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


# 6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end 
# of the line below. Convert the extracted value to a floating point number and print it out.
text = "X-DSPAM-Confidence:    0.8475"
pos = text.find('.')

stringNum = text[pos-1:pos+5]
print(float(stringNum))


# Write a program that prompts for a file name, then opens that file and reads through the file, 
# and print the contents of the file in upper case. Use the file words.txt to produce the output below.
# You can download the sample data at http://www.py4e.com/code3/words.txt
try:
    fname = input("Enter file name: ")
    fh = open(fname)
except:
    quit()
    
for line in fh:
    str = line.rstrip()
    print(str.upper())
    

# Write a program that prompts for a file name, then opens that file and reads through 
# the file, looking for lines of the form: X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and 
# compute the average of those values and produce an output as shown below. Do not use the 
# sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are 
# testing below enter mbox-short.txt as the file name.

fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    pos = line.find(":") + 1
    substr = line[pos:]
    num = float(substr)
    total = total + num
print("Average spam confidence: " + str(total/count))


