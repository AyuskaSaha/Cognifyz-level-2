def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def main():
    try:
        num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))
        if num_terms <= 0:
            print("Please enter a positive integer.")
        else:
            sequence = fibonacci_sequence(num_terms)
            print(f"Fibonacci sequence up to {num_terms} terms: {sequence}")
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
