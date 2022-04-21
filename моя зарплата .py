payrate = int(input('Привет, сколько ты получаешь в час?:  '))
hrswoked = int(input('А сколько часов ты отработал?:  '))
def salary(payrate, hrsworked):
        salary=payrate*hrsworked
        return salary
    
print(salary(payrate, hrswoked))