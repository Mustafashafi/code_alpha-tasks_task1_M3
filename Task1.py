# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def fibonacci_generator(n):
    fib_sequence = [0, 1]

    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence[:n]

# Example usage:
n_terms = int(input("Enter the number of Fibonacci terms to generate: "))
result = fibonacci_generator(n_terms)
print(f"The first {n_terms} Fibonacci numbers are: {result}")
