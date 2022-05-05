#1 create a list that represents the alphabet:
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
            "n","o","p","q","r","s","t","u","v","w","x","y","z"]

#2 create a for loop to iterate through this and print each letter in order
#produce a header (key) string. Not in the spec, but makes the program more flexible
headstr = ""
for x in range(1,27) :
    headstr += "{:>3}".format(x)

print(f"Header:{headstr}\nTarget:")

for c in alphabet :
    print("{:>3}".format(c),end="")
print("\n")

#3 Now using input, allow the user to type a number
#and print the letter it represents in the alphabet
user_val = input("Specify a header value to get the corresponding target letter:")

#4 Remember how index works - and think about how to structure your code
if user_val in range(1,27):
    print("correct")
else:
    print("not correct") 
user_val -= 1
print(f"Your entered: {user_val} ")