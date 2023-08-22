def sum(num1, num2):
    sum = int(num1) + int(num2)
    print(sum)   

def sub(num1, num2):
    sub = int(num1) - int(num2)
    print(sub) 

def cores():
    pass

def main():
    num1 = input("digite um numero\n")
    num2 = input("digite outro numero\n")
    sum(num1, num2)
    sub(num1, num2)

if __name__ == "__main__":
    main()