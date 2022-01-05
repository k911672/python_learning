# // 60
# // 59の続き、
# // Memberクラスを改修する
# // Memberというクラスは名前と年齢を持つ事ができる。
# // set_nameというメソッドで名前を設定する。
# // set_ageというメソッドで年齢を設定する。
# // showというメソッドでセットされた名前を出力する機能を作成しなさい。
# // 出力例　山田太郎さんは１１歳です。

class Member:
  def set_name(self, name):
    self.name = name

  def set_age(self, age):
    self.age = age

  def show(self):
    print(self.name + "さんは" + str(self.age) +"歳です。")

member = Member()
member.set_name('山田太郎')
member.set_age(11)
member.show()

# // // // 61
# // // // 60の続き、
# // // // 3人の情報を持ちたい
# // // // Memberクラスの配列を作りなさい。
# // // // それぞれの名前、年齢はは適当に入力すること

class Member:
  def set_name(self, name):
    self.name = name

  def set_age(self, age):
    self.age = age

  def show(self):
    print(self.name + "さんは" + str(self.age) +"歳です。")

# インスタンスを生成
michel = Member()
tom = Member()
mary = Member()
michel.set_name('マイケル')
michel.set_age(29)
tom.set_name('トム')
tom.set_age(69)
mary.set_name('メリー')
mary.set_age(9)

# インスタンスを配列に格納
member = []
member.append(michel)
member.append(tom)
member.append(mary)

# 出力
for person in member:
  show = person.show()

# // // // 62
# // // // 61の続き、
# // // // 名前と年齢をコンストラクターで登録するMemberクラスを作成し、インスタンス生成しなさい。
# // // // showメソッドで出力結果を確認すること

class Member:

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def show(self):
    print(self.name + "さんは" + str(self.age) +"歳です。")

# インスタンスを生成
michel = Member('マイケル', 29)
tom = Member('トム', 69)
mary = Member('メリー', 9)

# インスタンスを配列に格納
member = []
member.append(michel)
member.append(tom)
member.append(mary)

# 出力
for person in member:
  show = person.show()

# // // 63
# // // 次のクラスをカプセル化し、$languageはアクセサメソッドからのみ、代入・参照できる様に修正しなさい
# // //   class HumanBase:
# // //     def __init__(self, language):
# // //       language = "Japanese"
# // //
# // //   human_base = HumanBase('Japanese')
# // //   print(human_base.language)

class HumanBase:
  def __init__(self, first_language, sec_language):
    self.__language = first_language
    self.language = sec_language

  def change_language(self, language):
    self.__language = language

  def show(self):
    print(self.__language)
    print(self.language)

# インスタンス化
human_base =  HumanBase('Japanese', 'Japanese')
print(human_base.show())

# クラス外部からプロパティ値の変更
human_base.__language = 'English'
human_base.language = 'English'
print(human_base.show())

# クラス内部のメソッドからプロパティ値の変更（アクセサメソッドの活用
human_base.change_language('English')
print(human_base.show())
