import time
import threading


def sing():
  """ let sing"""
  for i in range(5):
    print("sing song")
    time.sleep(1)


def dance():
  """let dancing"""
  for i in range(5):
    print("dance for exercise")
    time.sleep(1)


def main():
  t1 = threading.Thread(target=sing())
  t2 = threading.Thread(target=dance())
  t1.start()
  t2.start()


if __name__ == '__main__':
  main()
