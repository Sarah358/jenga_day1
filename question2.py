# search in python
# main function
def main():
    fileName = 'names.txt'
    # creating options  
    print("\nMAIN MENU")  
    print("1. Show file contents")  
    print("2. Search with name")  
    print("3. Search with age")  
    print("4. Exit")  
    choice1 = int(input("Enter the Choice:"))  

    # choice 1
    if choice1 == 1:
        searchallnames(fileName)
    elif choice1 == 2:
        searchuserName(fileName)
    elif choice1 == 3:
        searchAge(fileName)
    elif choice1 == 4:
        exit
    else:
        print('Incorrect choice.')
        
            
# print all names
def searchallnames(fn):
    infile = open(fn,'r')
    for s in infile:
        print(s,end='')
    return

# search name starting with A
def searchName(fn):
    infile = open(fn,'r')
    for s in infile:
        if s.startswith('A'):
            print(s)    
    return

# search name from users input
def searchuserName(fn):
    infile = open(fn,'r')
    text = input('Enter string to search :')
    # convert to upper case
    text = text.upper()
    for s in infile:
        if s.startswith(text):
            print(s)
        
    # res = [idx for idx in infile if idx.lower().startswith(text.lower())]
    # print(res)           
    return

# search names with age 5
def searchoneAge(fn):
    infile = open(fn,'r')
    age = '5'
    age = age.strip()
    for line in infile:
        # convert each line into a list of words
        list = line.split()
        for word in list:
            if word == age:
                print(line)
    return




# search names with age  
def searchAge(fn):
    infile = open(fn,'r')
    age = input('Enter age to search: ')
    age = age.strip()
    for line in infile:
        # convert each line into a list of words
        list = line.split()
        for word in list:
            if word == age:
                print(line)
                
    return










   
    
   
       


    








	

	

	

	






if __name__ == "__main__":
    main()

