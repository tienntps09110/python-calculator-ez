import os

class Mess:
    # Print choose the function
    def program():
        print ("---CHƯƠNG TRÌNH MÁY TÍNH---")
        print ('|   1.Tính cộng            |')
        print ('|   2.Tính trừ             |')
        print ('|   3.Tính nhân            |')
        print ('|   4.Tính chia            |')
        print ('----------------------------')
    
    # Print value
    def result(text):
        print (f'Kết quả: {text}')

    # Print style ---
    def style():
        print ('----------------------------\n')
    
    # Print notice of end
    def thanks():
        print ('Chương trình kết thúc, xin cảm ơn !')

class Math:  
    # Get number1 and number2
    def __init__(self, numbers):
      self.a = numbers[0]
      self.b = numbers[1]

    # Summation
    def sum(self):
        return self.a + self.b
    
    # Subtraction
    def sub(self):
        return self.a - self.b

    # Multiplication
    def mul(self):
        return self.a * self.b

    # Division
    def div(self):
        return self.a / self.b

def clearConsole():
    # Clear console
    os.system('cls' if os.name=='nt' else 'clear')
       
def main():
    # Clear console if running again
    clearConsole()
    
    again_math = 'yes'

    while again_math == 'yes':
        again_math = 'no' 
        again_fun_program = 'yes'
        
        number1 = input('Nhập số thứ nhất: ')
        number2 = input('Nhập số thứ hai: ')

        Mess.program()
        numbers = [int(number1), int(number2)]
        math = Math(numbers)
        
        # Choose the function
        switcher = {
                1 : math.sum(),
                2 : math.sub(),
                3 : math.mul(),
                4 : math.div()
            }

        program_number = 0
        
        # If it is wrong, then choose again
        while again_fun_program == 'yes':            
            program_number = input('Chọn chức năng: ')
            program_number = int(program_number)
            if program_number == 1 or program_number == 2 or program_number == 3 or program_number == 4:
                break

        # Get the value of the choose function
        result = switcher.get(program_number, "Chưa chọn chức năng")

        # Print value
        Mess.result(result)

        Mess.style()

        # Continue
        again_math = input('Tính tiếp (yes): ')

        # If again_math to 'yes', it will run again while other characters will exit
        if(again_math == 'yes'):
            clearConsole()
        pass

    # Print notice of end
    Mess.style()
    Mess.thanks()
main()