print(".....CLI based simple calculator.....")

num1=float(input("Enter 1st number: "))
num2=float(input("Enter 2nd number: "))

opr=input("Enter arithmatic operation (+, - , x , /): ")

def format_result(result):
    return int(result) if result.is_integer() else result

def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

def div(num1,num2):
    return num1 / num2

def mult(num1,num2):
    return num1 * num2

if opr=="+":
    result=add(num1,num2)
    print(f"{format_result(num1)} + {format_result(num2)} = {format_result(result)}")

elif opr=="-":
    result=sub(num1,num2)
    print(f"{format_result(num1)} - {format_result(num2)} = {format_result(result)}")  
      
elif opr=="*":
    result=mult(num1,num2)
    print(f"{format_result(num1)} * {format_result(num2)} = {format_result(result)}")
    
elif opr=="/": 
    if num2!=0:
        result=div(num1,num2)
        print(f"{format_result(num1)} / {format_result(num2)} = {format_result(result)}")
        
    else:
        print("Error: Division 0 in not allowed")
else:
    print("invalid operation")


     
    