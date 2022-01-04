# // 29,
# // 5個のString(文字列)の配列を用意し適当な文字を代入してください。
# // その2番目の値を出力してください。

fruits = ['banana', 'peach', 'orange', 'grape', 'lemon']

print(fruits[1])

# // 30,
# // 10個のInteger(整数)の配列を用意し適当な値を代入してください。
# // 添字が偶数番目の合計値と添字が奇数番目の合計値を出力してください。

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_num = 0
odd_num = 0

for i, num in enumerate(nums):
  if i % 2 == 0:
    odd_num += num
  else:
    even_num += num

print(odd_num)
print(even_num)
# ※enumerateは「列挙する」という意味
# for i in range(0, len(nums))でindexを出すやり方でもできる。


# // 31,
# // Integer(整数)の配列を渡すと、配列の中身が３乗される関数を作ってください。
# // なお、関数の中で引数に必要だと思うvalidationも作成してください。（validationの意味がわからない場合は、お調べください）


nums = [1, 2, 3, 4, '5', 6, 7, 8, 9, 10]

def triple(num):
  num = num * num * num
  return num

def judge_num(num):
  return type(num) == int

for num in nums:
  if not judge_num(num):
    print('数値以外の値が含まれております')
    break
  print(triple(num))

# // 32,
# // 2つのInteger(整数)の配列を引数にもち、それぞれ同じ順番の値が合計された配列を作る関数を作ってください(配列を返り値として持つ)
# // 作られる配列は２つの入力された配列のうち少ない個数の配列の個数とします。

odds = [9, 11, 21, 99]
evens = [2, 24, 64]

def sum(odds, evens):
  sum_num = []

  length = len(odds)
  if (len(odds) > len(evens)):
    length = len(evens)

  for i in range(0, length):
    sum_num.append(odds[i] + evens[i])

  return sum_num

sum_num = sum(odds, evens)
print(sum_num)
