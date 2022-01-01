
# // 5, for文の基礎
# // 1~10までの数字をfor文を使って出力してください

for num1 in range(1, 11):
  print(num1)

# // 6, for文の基礎２
# // 35 ~ 46までの数字をfor文を使って出力してください

for num2 in range(35, 47):
  print(num2)

# // 7. for文と条件式の組み合わせ
# // 40 ~ 50までの数字の中で奇数の数字のみを出力してください

for num3 in range(40, 51):
  if num3 % 2 != 0:
    print(num3)

# // 8. for文と条件式の組み合わせ2
# // 10 ~ 25までの数字の中で3の倍数の数字のみを出力してください

for num4 in range(10, 25):
  if num4 % 3 == 0:
    print(num4)
