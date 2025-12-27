# making simple calculator 
print("---------------WLECOME TO THE CALCULATOR-------------")

opr_list = ['+','-','*','/','**','%']
history= []

def show_history ():
    if not history:
        print('No history📂')
    else:
        for i,result in enumerate(history, 1):
            print(f'{i}. {result}')

def calculator(num1 ,num2, opr ):
    
    try:
        
        if opr == '+':
            return num1+num2

        elif opr == '-':
            return num1 - num2

        elif opr == '*':
            return num1 * num2

        elif opr == '/':
            if num2 == 0 :
                raise ValueError('ERROR : "not divisible by 0"')
            else:
                return num1 / num2

        elif opr =='**':
            return num1 ** num2
        
        elif opr == '%':
            return num1 % num2
        
        else:
            return
    
    except ValueError as e:
        return e 

while True:
    
    while True:
        
        try:
            num1 = float(input('ENTER 1st number : '))
            num2 = float(input('ENTER 2nd number : '))
            break
        
        except ValueError:
            print("ERROR : PLEASE INPUT CORRECT NUMBER")
            continue
    
    while True:    
        
        print("operarots", opr_list)
        print("q for Quit | h for History")
        opr = input("ENTER : ")
        
        if opr.lower() == 'q':
            print('\ncalculaator closed')
            print('\ncalculator histroy ')
            show_history()
            break
        
        elif opr.lower() == 'h':
            show_history()
            
        elif opr in opr_list:
            break
        
        else :
            print('❌--ERROR--❌, TRY AGAIN , ENTER VALID OPERATOR')
    
    result = calculator(num1,num2,opr )
    if int(result) == result:
        result = int(result)
    print('RESULT : ', result)
    
    # history saved
    history.append(f"{num1} {opr} {num2} = {result}")