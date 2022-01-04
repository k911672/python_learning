# 23.
# int型とboolean型を渡し boolean型がtrueなら　int型を1プラスする　falseなら1マイナスする関数を作成してください

num = 2
boo = False

def judge_boo(num, boo):
  if boo == True:
    return num + 1
  else:
    return num - 1

print(judge_boo(num, boo))

# // 24.
# // int型とString型を渡しそのint型の数値の回数分　型の内容Stringを出力する関数を作成してください
# // (int型が0以下の場合　「範囲外の入力値です」と出力してください

num = 4
text = "バナナ"

def loop_text(num, text):
  for i in range(0, num):
    print(text)

loop_text(num, text)

# // ★★★★★★★★★★★★★★★
# // せっかくですので、ここで追加問題といきますね。再帰関数の問題です。
# // 設問13ですが、現状では２つの変数が固定値となっていますので、これをランダムな数字が代入された２つの値を返すような関数を作成してみましょう。
# // また２つの変数の差がマイナスになる場合は、再度、同じ関数を呼び、再代入するような関数を作成してみてください。
# // 13. 条件式
# // 整数型の２つの変数を宣言してください。
# // 上記で宣言した２つの変数の内、1つ目を2つ目で引いた数字が偶数、奇数、0で「偶数です」「奇数です」「0です」と表示させるような条件式を書いてください。
# // よろしければ、トライしてみてください＾＾
# // ★★★★★★★★★★★★★★★

import random

def calc():
  num1 = random.randint(1,100000)
  num2 = random.randint(1,100000)
  return num1 - num2

def judge_num():
  if calc() < 0:
    print('もう一度計算します')
    judge_num()
    return

  if calc() == 0:
    print('0です')
  elif calc() % 2 == 0:
    print('偶数です')
  else:
    print('奇数です')

judge_num()
