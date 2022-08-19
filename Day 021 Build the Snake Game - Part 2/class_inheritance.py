class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("I'm breathing")


class Fish(Animal):
    def __init__(self):
        super().__init__()  # Calling the parent class constructor

    def breathe(self):  # Overriding the parent class method
        super().breathe()  # Calling the parent class method
        print(" and doing this underwater")  # Inheritance is a way to reuse code.

    def swim(self):  # Additional method for Fish class
        print("I'm swimming")


print("\033[2J\033[1;1H")  # clear screen
nemo = Fish()
nemo.swim()
nemo.breathe()
print(f"I have {nemo.num_eyes} eyes")
