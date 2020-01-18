class Cat:
  def eat(self):
    print("%s like to eat fish" % self.name)

  def drink(self):
    print("%s the cat want to drink milk" % self.name)


# Create class object
tom = Cat()
tom.name = "Tom"

tom.eat()
tom.drink()

print(tom)

# addr = id(tom)
#
# print("%x" % addr)

lazy_cat = Cat()

lazy_cat.name = "I am a lazy cat"

lazy_cat.eat()
lazy_cat.drink()

print(lazy_cat.name)
