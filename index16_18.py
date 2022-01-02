# // 16, 図形の表示
# //  0
# //  00
# //  000
# // この図形をfor文を使って出力してください。

for i in range(1,4):
  print('0' * i)

# // 17, 図形の表示
# //    0
# //   000
# //  00000
# // この図形をfor文を使って出力してください。

# パート１
for i in range(1,4):
  print(" " * (3 - i), end = "")
  print("0" * (2 * i - 1))

# パート２
for i in range(0,3):
  for j in range(i, 2):
    print(" ", end = "")
  for k in range(5 - 2 * i , 6):
    print("0", end = "")
  print("")



# // 18, 図形の表示
# //    0
# //   000
# //  00000
# //   000
# //    0
# // この図形をfor文を使って出力してください。

# パート１
for i in range(1,4):
  print(" " * (3 - i), end = "")
  print("0" * (2 * i - 1))

for i in reversed(range(1,3)):
  print(" " * (3 - i), end = "")
  print("0" * (2 * i - 1))

# パート２
for i in range(0,3):
  for j in range(i, 2):
    print(" ", end = "")
  for k in range(5 - 2 * i , 6):
    print("0", end = "")
  print("")

for i in range(0,2):
  for j in range(1 - i, 2):
    print(" ", end = "")
  for k in range(2 * i , 3):
    print("0", end = "")
  print("")
