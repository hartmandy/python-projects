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


# 8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a 
# list of words using the split() method. The program should build a list of words. 
# For each word on each line check to see if the word is already in the list and if not append it to the list. 
#When the program completes, sort and print the resulting words in python sort() order as shown in the 
# desired output. You can download the sample data at http://www.py4e.com/code3/romeo.txt

fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    fline = line.rstrip()
    words = fline.split()
    for word in words: 
        if word in lst: continue
        
        lst.append(word)
    
lst.sort()
print(lst)


# 8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' 
# like the following line: From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line (i.e. the entire 
# address of the person who sent the message). Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample 
# output to see how to print the count. You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh: 
  if not line.startswith('From '): continue
  words = line.split()
  print(words[1])
  count = count + 1


print("There were", count, "lines in the file with From as the first word")



# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number 
# of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the 
# person who sent the mail. The program creates a Python dictionary that maps the sender's mail address 
# to a count of the number of times they appear in the file. After the dictionary is produced, the program 
# reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
count = dict()

for lines in handle:
    lines = lines.rstrip()
    if lines.startswith("From "):
        words = lines.split()
        word = words[1]
        count[word] = count.get(word, 0) + 1

bigcount = None
bigword = None

for word, count in count.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)


# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour 
# of the day for each of the messages. You can pull the hour out from the 'From ' line by finding 
# the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
count = dict()

for line in handle:
    if not line.startswith("From "):
        continue
    words = line.split()
    time = words[5]
    hour = time.split(":")[0]
    count[hour] = count.get(hour, 0) + 1

for k, v in sorted(count.items()):
    print(k, v)

    