da = "yes"

print("Hello, let's convert some miles into kilometres!")

miles = float(raw_input("Please enter the value for miles: "))
kilometres = miles * 1.61
print("%s miles is %s kilometres.") % (miles, kilometres)

while raw_input("Do you want another conversion? (yes/no) ").lower() == da:
    float(raw_input("Please enter the value for miles: "))
    print("%s miles is %s kilometres.") % (miles, kilometres)
else:
    print("Thank you for your query, have a nice day.")
