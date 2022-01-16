# numbers divisible by 3 and 7 between 1 and 100
# empty list
print()
n1=[]
# for loop
for x in range(1, 100):
    if (x%7==0) and (x%3==0):
        n1.append(str(x))
        # print output
print('Numbers divisible by 7 and 3 : '+','.join(n1))

# break
print()

# numbers divisible by 7 not 3
n2=[]
# for loop
for x in range(1, 100):
    if (x%7==0) and (x%3!=0):
        n2.append(str(x))
        # print output
print('Numbers divisible by 7 not 3 : '+','.join(n2))
# break
print()


# ODD numbers divisible by 7 but not 3
n3=[]
# for loop
for x in range(1, 100):
    if (x%2!=0) and (x%7==0) and (x%3==0):
        n3.append(str(x))
        # print output
print('Odd Numbers divisible by 7 and 3 : '+','.join(n3))
# break
print()

# numbers that are divisible by the sum of its digits (e.g. 36: 3+9=9 39/9 = 4)  harshad numbers
def check_harshad(number):
  remainder = 0
  digit_sum = 0
  check = False
  n = number
  while(n > 0):
    remainder = n % 10
    digit_sum = digit_sum + remainder
    n = n//10
  if number % digit_sum == 0:
    check = True
  return check

print("HARSHAD NUMBERS :" )
for i in range(1,100):
  if check_harshad(i):
    print(i,end = "  ")
    # break
print('')
print('')


# Print the numbers that are equal to the square of the sum of its digits(happy numbers)

#isHappyNumber() will determine whether a number is happy or not  
def isHappyNumber(num):  
    rem = sum = 0;  
      
    #Calculates the sum of squares of digits  
    while(num > 0):  
        rem = num%10;  
        sum = sum + (rem*rem);  
        num = num//10;  
    return sum;  

          
#Displays all happy numbers between 1 and 100  
print("List of happy numbers between 1 and 100: ");  
for i in range(1, 101):  
    result = i;  
      
    #Happy number always ends with 1 and   
    #unhappy number ends in a cycle of repeating numbers which contains 4  
    while(result != 1 and result != 4):  
        result = isHappyNumber(result);  
      
    if(result == 1):  
        print(i,end="  ") 
print('')
print('')
          