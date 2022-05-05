#2 Create a function that checks if the string length is
#even; if it is, print the string, the length and an
#appropriate message in one sentence. Do the same
#but with a different message if it's odd.
def string_len_evenodd( the_str = None, str_len=None):
    #if passed param are bogus, just return
    if the_str == None or str_len == None:
        return None

    #if string length is even, set an "even" message else set an "odd" one
    if str_len % 2 == 0:
        evenodd = "even"
    else:
        evenodd = "odd"
    
    #print the complete message as specified
    print(f"String:'{the_str}' is length:{str_len} which is an {evenodd} length")


#1a Create a variable that holds the text "Welcome to Code Nation"
welcome = "Welcome to Code Nation"

#1b Find the length of welcome
welcome_len = len(welcome)

#3 Change the string length so you can test all
#possible outcomes

print("calling function without all parameters should return None")
print("string_len_evenodd() returned: ", string_len_evenodd())

print("\n\ncalling function with parameters should return nothing\nand will print out the result of the check:")
string_len_evenodd( welcome, welcome_len)

#reduce string length by one character making it odd
welcome = welcome[:-1]
#get the new length which will have switched from even to odd or odd to even
welcome_len = len(welcome)
print("\n\ncalling function with string shortened by 1 character")
string_len_evenodd( welcome, welcome_len)
