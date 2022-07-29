#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#letters
final_list = []
for i in range(nr_letters):
  i = random.randint(0,len(letters)-1)
  actual_letter = letters[i]
  list_of_letters = [actual_letter]
  final_list = list_of_letters + final_list

string_letters = ""
for x in range(nr_letters):
  string_letters = final_list[x] + string_letters
#print(string_letters)

#numbers 
final_list_numbers = []

for y in range(nr_numbers):
  y = random.randint(0,len(numbers)-1)
  actual_number = numbers[y]
  list_of_numbers = [actual_number]
  final_list_numbers = list_of_numbers + final_list_numbers

string_numbers = ""
for z in range(nr_numbers):
  string_numbers = final_list_numbers[z] + string_numbers
#print(string_numbers)


#symbols
final_list_symbols = []

for y in range(nr_symbols):
  y = random.randint(0,len(symbols)-1)
  actual_symbol = symbols[y]
  list_of_symbols = [actual_symbol]
  final_list_symbols = list_of_symbols + final_list_symbols

string_symbols = ""
for z in range(nr_symbols):
  string_symbols = final_list_symbols[z] + string_symbols
#print(string_symbols)


print(string_letters+string_symbols+string_numbers)










  
  


  
  
  

  



  

  
  
  
  
  
  



  
  
  
  
  
  
  
  

  
  
