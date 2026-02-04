#To access characters from the end of a string using a negative index.

#create variable to store input string
string_var = input("Enter a string: ")

#access the last and 4th character of the string

#to get 1st char - index (-1)
charlast = string_var[-1]

#to get 4th char  - index (-4)
char4 = string_var[-4]

#print result
print ("last character of entered string is: ",  charlast)
print ("4th character of entered string is: ", char4)