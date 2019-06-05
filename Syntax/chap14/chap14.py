class Bank:
    def __init__(self,username,number,amount):
        self.username = username
        self.number = number
        self.amount = amount


myBank = Bank("Sun Beichen", "12345678", "1265.90")
print("There is ",myBank.amount," in my bank.")
print("The password is ",myBank.number)
print("My username is ",myBank.username)