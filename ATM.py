class atm:
    def __init__(self,cardNum, pinNum):
        self.cardNumber=cardNum
        self.pinNumber=pinNum

    def showcardNum(self):
        print("The Card Number is: " , self.cardNumber)
    
    def showpinNum(self):
        print("The Pin Number is: " , self.pinNumber)
    

def main():
    cardNumber = input("Enter Card Number: ")
    pinNumber = input("Enter Pin Number: ")

    CashWithdrawal = atm(cardNumber, pinNumber)   
   
    CashWithdrawal.showcardNum()
    CashWithdrawal.showpinNum()


main()