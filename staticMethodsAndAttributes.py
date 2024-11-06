class Calculator:
    count = 0

    @staticmethod
    def add(a, b):
        Calculator.count += 1
        return a + b

# I used the add static method and update the count
result1 = Calculator.add(5, 3)
print(f"addition results: {result1}")
print(f"Add method called: {Calculator.count} times")

result2 = Calculator.add(10, 7)
print(f"addition results: {result2}")
print(f"Add method called: {Calculator.count} times")
