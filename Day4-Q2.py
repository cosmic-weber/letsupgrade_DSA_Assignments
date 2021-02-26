class Sum:

    def addition(self, a, b):
        q = a + b
        return q


a = int(input("enter first number: "))
b = int(input("enter second number: "))

Add = Sum()
t = Add.addition(a, b)

print("Sum is = ", t)
