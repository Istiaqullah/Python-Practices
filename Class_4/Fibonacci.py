def is_fibonacci(n, a=0, b=1):
    # Base cases
    if a == n:
        return True
    if a > n:
        return False

    # Tail-recursive call
    return is_fibonacci(n, b, a + b)


# Example
num = int(input("Enter a number: "))
print("Fibonacci" if is_fibonacci(num) else "Not Fibonacci")
