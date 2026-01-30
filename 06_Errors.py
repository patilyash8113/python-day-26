#try and except statement are used to handle Errors..
# while True:
#     try:
#         a=int(input("Enter the first number:"))
#         b=int(input("Enter the second number:"))
#         print(f"the sum of the number is {a+b}")
#     except Exception as e:
#         print("Some error occured!",e)
while True:
    try:  
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))

        print(f"The sum of a and b is {a+b}")
    except Exception as e:
        print("Lavdya chukich lihilay! parat lihi")