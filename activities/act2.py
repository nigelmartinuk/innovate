#1 create a list that represents the alphabet:
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
            "n","o","p","q","r","s","t","u","v","w","x","y","z"]



#2 create a for loop to iterate through this and print each letter in order
for x in range(26) :
    print("{:>3}".format(x),end="")
print(" ")
for x in alphabet :
    print("{:>3}".format(x),end="")

#3 Now using input, allow the user to type a number
#and print the letter it represents in the alphabet

#4 Remember how index works - and think about how to structure your code