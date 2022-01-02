# // 13. 条件式
# // 整数型の２つの変数を宣言してください。
# // 上記で宣言した２つの変数の内、1つ目を2つ目で引いた数字が偶数、奇数、0で「偶数です」「奇数です」「0です」と表示させるような条件式を書いてください。

num1 = 56
num2 = 55

result = num1 - num2

if result == 0:
  print('0です')
elif result % 2 == 0:
  print('偶数です')
else:
  print('奇数です')

# // 14. FizzBuzz
# // 1 ~ 100の数字をfor文でループしてください。
# // ただし3の倍数のときは数の代わりに｢Fizz｣と、5の倍数のときは｢Buzz｣、3と5両方の倍数の場合には｢FizzBuzz｣と出力すること。

for num3 in range(0, 101):
  print(num3)
  if num3 % 3 == 0 and num3 % 5 == 0:
    print('FizzBuzz')
  elif num3 % 3 == 0:
    print('Fizz')
  elif num3 % 5 == 0:
    print('Buzz')


# // 15. switch文
# // 整数型の２つの変数を宣言してください。
# // 上記で宣言した２つの変数の内、1つ目を2つ目で引いた数字が偶数、奇数、0で「偶数です」「奇数です」「0です」と表示させるような条件式を書いてください。
# pythonにはswitch文はないので、辞書やif文を使う。


num4 = 34
num5 = 34

result = num4 - num5

if result == 0:
  print('0です')
elif result % 2 == 0:
  print('偶数です')
else:
  print('奇数です')
