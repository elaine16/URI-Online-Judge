A = None
B = None
X = None

def read_integer():
  try:
    return int(raw_input())
  except NameError:
    return int(input())

A = read_integer()
B = read_integer()
X = A + B
print(str("X = ") + str(X))

