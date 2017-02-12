i = 1

q = int(raw_input("Select a number between 1 and 100: "))

while i <= q:
    if i % 5 == 0 and i % 3 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print i

    i = i + 1