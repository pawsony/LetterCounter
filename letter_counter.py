def letter_counter():

  import string

  inp = input('Please provde a file name: ')

  fh = open(inp)

  di = {}

  for line in fh:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.translate(line.maketrans('', '', string.whitespace))
    line = line.translate(line.maketrans('', '', string.digits))
    line = line.lower()
    lines = list(line)
    for i in lines:
      di[i] = di.get(i, 0) + 1
  
  lst = []

  for k, v in di.items():
    lst.append((k, v))

  lst.sort()

  for k, v in lst:
    print(k, v)

letter_counter()