# // 25,
# // 配列を宣言してください
# // Integer(整数) 1個の配列　
# // String(文字列) 3個の配列

num = [4]
fruits = ['banana', 'peach', 'orange']

# // // 26,
# // // 配列は初期化の際に初めから配列の値の代入までまとめて行う事ができます。
# // // Integer(整数)　3個の配列で　　1,2,3という数字を値に持たせたい。
# // // 宣言、要素の確保ののちそれぞれに代入する配列の用意の仕方と
# // // 代入までまとめて行う書き方で用意する仕方にて配列を用意してください

# appendを使う
nums = [1]
nums.append(2)
nums.append(3)
print(nums)

# extendを使う
nums =[1]
nums.extend([2, 3])
print(nums)

# // 27,
# // 26の続き、
# // 用意した配列をfor文を使って値を出力してください。
# // foreach文を使った値の出力をしてください。
# pythonにforeachは無いがfor文で全てを代用できる。

# for文
for i in range(0,3):
  print(nums[i])

# for文（foreachの代わり）
for num in nums:
  print(num)

# // 28,
# // 27の続き、
# // 値を出力したあとにそれぞれの値の２乗の値を代入し直すよう修正してください。

def double(num):
  num *= num
  return num

for num in nums:
  print(double(num))
