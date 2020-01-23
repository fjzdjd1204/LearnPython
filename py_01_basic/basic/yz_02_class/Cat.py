class Cat:
  def eat(self):
    print("cat like to eat fish")

  def drink(self):
    print("the cat want to drink milk")


# Create class object
tom = Cat()

tom.eat()
tom.drink()

print(tom)

addr = id(tom)

print("%x" % addr)
