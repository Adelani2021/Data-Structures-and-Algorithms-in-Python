Question 4 (Interleave Two Strings)
String_1 = input("Enter the first string: ")
String_2 = input("Enter the second string: ")
New_string = "".join([String_1[i] + String_2[i] for i in range(len(String_1))])
print (New_string)


  
