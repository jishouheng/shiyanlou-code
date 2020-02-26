for a in range(1,101):
  if a%7 != 0:
    c = str(a)
    d = 1
    for b in c:
      if int(b) == 7:
        d = 0
    if d == 1:
      print(a)


