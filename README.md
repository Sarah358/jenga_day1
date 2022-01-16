# jenga_day1
assignment 1 at jenga school
# QUESTION 0NE 
## Use a loop from 1 to 100 and print the numbers that satisfy the following conditions.

● Print the numbers that are divisible by 7 and 3

● Print the numbers that are divisible by 7 but not 3

● Print the ODD numbers divisible by 7 but not 3

● Print the numbers that are divisible by the sum of its digits (e.g. 36: 3+9=9
  39/9 = 4)   harshad numbers

● Print the numbers that are equal to the square of the sum of its digits (happy numbers )


# QUESTION TWO

## In this part, we are going to write a program that does a search in a file that contains names and ages. Copy the following lines and paste them in Notepad. Save the file in the folder that you will save your python program with the name “names.txt”. Make sure Each name and age is in its own line (e.g “Albert 5” is one line ) . Remove the commas when pasting.
    Alfred 5, Abdul 5, Eliza 11, Harun 8, Rama 9, Fatma 11, Martin 12, Nuray
    7, Mustafa 7, Nazan 7, Yasin 13, Susan 8, Tabitha 12, Omar 5, Unat 11, Veli 10, Zehra 11, Jale 8, Lale 9, Kerim 13, Pelin 7, Cecil 6, Berna 5, Deniz 12, Godwin 10, Melih 6, Maryam 10, Emre 6, Berta 5, Ceren 5, Derya 9


● Open a new Python program file. Define a function named searchname(). In this function, open the file “names.txt” and print its contents using a loop.

● Modify your program so that it prints only the lines where the name starts with the letter “A”

● Modify your program so that it first reads a letter from the user, and then prints only the lines where the name starts with that letter. Handle the lower/upper case issue. EXTRA: Let the user search with a longer string. E.g. Search with Ah instead of A.

● Define a new function named searchage(). Again, copy the code that opens and
prints the file. This time, modify the code such that it prints only the lines where the age is equal to 5.

● Modify searchage() such that it gets the search age from the user.

● Add the main() function to your program. Your program should start from here. In this function, print the choices 1-search with name and 2-search with age as a menu and ask the user to choose one. Call the function searchname() or searchage() based on the number the user enters. If the user enters a number other than 1 or 2, print a warning message and end the program
