def generator(a):
  c = 1
  while True:
    yield f'a x {c} = {a * c}'
    c += 1