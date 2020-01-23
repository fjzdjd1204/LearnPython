import threading
import time


def saySorry():
  print("Darling, I am so sorry")
  time.sleep(1)


if __name__ == '__main__':
  for i in range(4):
    t = threading.Thread(target=saySorry)
    t.start()
