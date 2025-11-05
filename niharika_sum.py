# niharika_sum.py
# Simple program to compute sum of two numbers

def main():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Sum =", a + b)
    except Exception as e:
        print("Please enter valid integers.")

if __name__ == "__main__":
    main()
