# // 9. for文と条件式の組み合わせ3
# // 20 ~ 50までの数字の中で2で割ったら奇数となる数字のみを出力してください

# for num1 in range(20, 51):
#   if num1 % 2
#     if (num1 / 2) % 2 != 0:
#       print(num1)

# ↓修正：整数判定is_integer()を使う
for i in range(20, 51):
  num1 = i / 2
  if num1.is_integer() and num1 % 2 != 0:
    print(i)

# // 10. for文と条件式の組み合わせ4
# // 20 ~ 50までの数字の中で2で割ったら奇数となる数字の個数を出力してください

count = 0

for i in range(20, 51):
  num2 = i / 2
  if num2.is_integer() and num2 % 2 != 0:
    count += 1
print(count)

# // 11. for文を使用した計算
# // 1000未満の「3と7の倍数」は何個あるか　個数を出力してください

count = 0

for i in range(0, 1001):
  if i % 3 == 0 or i % 7 == 0:
    count += 1

print(count)

# // 12. for文を使用した計算2
# // 1000未満の「3と7の倍数」の5番目に大きい数を出力してください

count = 0

for i in reversed(range(0, 1001)):
  if i % 3 == 0 or i % 7 == 0:
    count += 1
    if count == 5:
      print(i)
