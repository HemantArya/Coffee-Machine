class CoffeeMachine:

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee = 120
        self.money = 550
        self.cups = 9

    def buy(self):
        print("")
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        b = input("> ")
        if b == '1':
            if (self.water < 250):
                print("Sorry, not enough water!")
                return
            if (self.coffee < 16):
                print("Sorry, not enough coffee beans!")
                return
            if (self.cups < 1):
                print("Sorry, not enough disposable cups!")
                return
            print("I have enough resources, making you a coffee!")
            self.water -= 250
            self.coffee -= 16
            self.cups -= 1
            self.money += 4
        elif b == '2':
            if (self.water < 350):
                print("Sorry, not enough water!")
                return
            if (self.milk < 75):
                print("Sorry, not enough milk!")
                return
            if (self.coffee < 20):
                print("Sorry, not enough coffee beans!")
                return
            if (self.cups < 1):
                print("Sorry, not enough disposable cups!")
                return
            print("I have enough resources, making you a coffee!")
            self.water -= 350
            self.milk -= 75
            self.coffee -= 20
            self.money += 7
            self.cups -= 1
        elif b == '3':
            if (self.water < 200):
                print("Sorry, not enough water!")
                return
            if (self.milk < 100):
                print("Sorry, not enough milk!")
                return
            if (self.coffee < 12):
                print("Sorry, not enough coffee beans!")
                return
            if (self.cups < 1):
                print("Sorry, not enough disposable cups!")
                return
            print("I have enough resources, making you a coffee!")
            self.water -= 200
            self.milk -= 100
            self.coffee -= 12
            self.money += 6
            self.cups -= 1
        else:
            return

    def remaining(self):
        print("")
        print("The Coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.coffee, "of coffee beans")
        print(self.cups, "of disposable cups")
        print(self.money, "of money")

    def fill(self):
        print("")
        print("Write how many ml of water do you want to add:")
        self.water += int(input("> "))
        print("Write how many ml of milk do you want to add:")
        self.milk += int(input("> "))
        print("Write how many grams of coffee beans do you want to add:")
        self.coffee += int(input("> "))
        print("Write how many disposable cups of coffee do you want to add:")
        self.cups += int(input("> "))

    def take(self):
        print("")
        print("I gave you $" + str(self.money))
        self.money = 0


coffeeMachine = CoffeeMachine()
while True:
    print("Write action (buy, fill, take, remaining, exit):")
    option = input("> ")
    if option == 'buy':
        coffeeMachine.buy()
    elif option == 'fill':
        coffeeMachine.fill()
    elif option == 'take':
        coffeeMachine.take()
    elif option == 'remaining':
        coffeeMachine.remaining()
    else:
        break
    print("")
