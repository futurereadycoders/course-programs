old = 0
current = 1
new = 0

terms = int(input("How many terms? "))
for i in range(terms):
    print(old)
    new = old + current
    old = current
    current = new



