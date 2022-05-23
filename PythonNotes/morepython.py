
# # casting types
# print( int(round(5.3)))
# print( int("54"))

# print( float(54))

# print( type(str(54)))
# print( type(str(5.4)))

# # Falsy and truthy
# name = input("Whats your name:")
# if name:
#     print(f"Hello {name}, have a nice day")
# else:
#     print("you didn't enter anything")

# # not
# print(not True)
# print(not False)

# bool = False
# if bool != True:
#     print(False)
# else:
#     print(True)

# # try/except
# def add_up():
#     num1 = input("give number1:")
#     num2 = input("give number2:")
#     # first version produces string concatenation, no math
#     print( num1 + num2)
#     # second version will add values, but still falls with text
#     print( int(num1) + int(num2))
#     # third version will try to work, but catch any error
#     try:
#         print(f"Adding {num1} + {num2} = {int(num1)+int(num2)}")
#     except:
#         print("A nice error handler")

# # add_up()

# print(int("0xdeadbeef", 0))

# print(int("10", 0))

# # class definition
# class light:
#     def light_switch(light):
#         #global light
#         if light:
#             print("Whoa! It's bright in here")
#             light = False
#         else:
#             print("Who turned out the lights?")
#             light = True

#         return light


# # light switch
# lighting = light
# alight = False

# alight = lighting.light_switch(alight)
# alight = lighting.light_switch(alight)

even_nums = [2,4,6,8,10]
odd_nums = (1,3,5,7,9)

even_nums.insert(10,0); print(even_nums)
even_nums.remove(6); print(f"remove(6) {even_nums}")
even_nums.pop(2); print(f"pop(2) {even_nums}")

