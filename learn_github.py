ls = [1, 4, 32, 67]

for i in range(len(ls)):
  print(ls[i] ** 2)

print(sum(ls))

ls = list(map(lambda x: str(x), ls))

print(ls)