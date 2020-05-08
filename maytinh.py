import os

class Mess:
    def program():
        print ("---CHƯƠNG TRÌNH MÁY TÍNH---")
        print ('|   1.Tính cộng            |')
        print ('|   2.Tính trừ             |')
        print ('|   3.Tính nhân            |')
        print ('|   4.Tính chia            |')
        print ('----------------------------')
    
    def result(text):
        print (f'Kết quả: {text}')

    def style():
        print ('----------------------------\n')
    
    def thanks():
        print ('Chương trình kết thúc, xin cảm ơn !')

class Math:
    def __init__(self, numbers):
      self.a = numbers[0]
      self.b = numbers[1]

    def sum(self):
        return self.a + self.b
        
    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

def clearConsole():
    os.system('cls' if os.name=='nt' else 'clear')
       
def main():
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

        switcher = {
                1 : math.sum(),
                2 : math.sub(),
                3 : math.mul(),
                4 : math.div()
            }

        program_number = 0
        
        while again_fun_program == 'yes':            
            program_number = input('Chọn chức năng: ')
            program_number = int(program_number)
            if program_number == 1 or program_number == 2 or program_number == 3 or program_number == 4:
                break

        result = switcher.get(program_number, "Chưa chọn chức năng")
        Mess.result(result)
        Mess.style()

        again_math = input('Tính tiếp (yes): ')

        if(again_math == 'yes'):
            clearConsole()
        pass

    Mess.style()
    Mess.thanks()
main()