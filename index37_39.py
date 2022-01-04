# // 37,三項演算子
# // Integer(整数)の変数を2つ、String(文字列)の変数を1つ宣言してください。
# // 2つのint型変数の合計が100未満なら「100未満」、そうじゃなければ「100以上」とString(文字列)に三項演算子(条件演算子)を使って代入して、出力してください。

odd = 33
even = 77

result = odd + even
text = '100未満' if result < 100 else "100以上"
print(text)

# // 38,文字列検索
# // string型の変数を２つ宣言してください。
# // 第二引数のString(文字列)が第一引数に含まれているかどうかのboolean型を返す関数を作成してください。

word = 'banana'
text = 'a'

def check_include_text(word, text):
  return text in word

print(check_include_text(word, text))


# // 39, 標準入力
# // PHPファイルはコマンドラインから実行してください。
# // 仕様
# // 「あなたの名前を教えてください。」出力
# // ↓
# // 入力 ex) Micael
# // ↓
# // 「Micaelさん、あなたの年齢は何歳ですか？」出力
# // ↓
# // 入力 ex) 20
# // ↓
# // 「Micaelさん（年齢:20）、ご登録ありがとうございます！」出力
# // ↓
# // プログラム終了
# // [追加するバリエーション]
# // 名前
# // ・空でないこと
# // ・10文字以内
# // 年齢
# // ・空でないこと
# // ・数字であること


def check_name(name):
  if not name:
    print('名前を入力してください')
    return False

  if len(name) > 10:
    print('名前は10文字以内で入力お願いいたします。')
    return False

  return True

def check_age(age):
  if not age:
    print('年齢を入力してください')
    return False

  if type(age) != int:
    print('数値を入力してください')
    return False

  return True

def question():
  name = input('あなたの名前を教えてください。：')
  if not check_name(name):
    return

  age = input(name + 'さんは何歳ですか？：')
  if not check_age(age):
    return

  result = input(name + 'さん（年齢：' + age + '）、ご登録ありがとうございます')
  print(result)

question()
