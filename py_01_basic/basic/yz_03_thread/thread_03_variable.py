num = 100

nums = [11, 22]


def test():
  global num
  num += 100
  print(num)


def test2():
  nums.append(33)
  print(nums)


test()
test2()
