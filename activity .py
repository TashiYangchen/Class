name = input("Enter your name:")
print("Select operations.:")
print("1. addition (a)")
print("2. subtraction (s)")
print("3. multiplication (m)")
print("4. division (d)")
choice = input( "Enter the option number for the arithmetic operatiion: ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if choice == "1":
     a = num1 + num2
     print(f"addition (a) = {a}")
elif choice == "2":
     s = num1 - num2  
     print(f"subtraction (s) = {s}")
elif choice == "3":
     m = num1 * num2
     print(f"mulitplication (m) = {m}")
elif choice == "4":
     d = num1 / num2
     print(f"d")
else:
    print( "Invalid option selected for the arthmetic operatios choice")