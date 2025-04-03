def div(num1, num2):
    return num2 / num1

def main():
    print('This program will do some calculation on two user-entered numbers!')
    
    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))
    
    print(f"Divide = {div(num1, num2)}")

if __name__ == "__main__":
    main()
