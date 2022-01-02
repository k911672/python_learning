# // 19, while文 do-while文
# // 1000から2000までの間で1の桁が7の数字の最初の数字を求めて出力してください
# // for文　while文　do-while文を使ってそれぞれ出力してください
# // ※do-whileはpythonに無いので省略

# # for文
for i in range(1000, 2001):
  if (i - 7) % 10 == 0:
    print(i)

# # while文
i = 1000
while i < 2001:
  i += 1
  if (i - 7) % 10 == 0:
    print(i)


# // 20. 関数の基礎
# // int型の変数を宣言してください。
# // 変数を渡して二乗の整数を返す関数を作成してください

num = 11

def square():
  return num * num

print(square())


# // 22.
# // int型とString型の２つの変数を引数で渡すと 「int型:String型」という文字列を返す関数を作成してください
# // ※int型,String型は引数で渡してください
# // ex)出力例「 5: ああああ」

num = 4
text = 'もも'

def fruits(num, text):
  return str(num) + ":" + text

print(fruits(num, text))
