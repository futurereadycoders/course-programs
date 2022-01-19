old = 0
current = 1
new = 0

total = ""

terms = int(input("How many terms? "))
for i in range(terms):
    if i == terms - 1:
        total = total + str(old)
    else:
        total = total + str(old) + ", "
    new = old + current
    old = current
    current = new

print(total)
