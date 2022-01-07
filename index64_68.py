# // // 64
# // // 63の続き、
# // // HumanBaseクラスのインスタンスを生成した際にインスタンスの生成回数を追加し、
# // // インスタンスを生成した回数がわかる様にしなさい
# // // 回数はコンストラクタ内で行うようにし、
# // // インスタンスが生成された回数は、クラスの外から参照できるようにすること
# // // human_countをクラス変数として書き換えることで実現できる

# class HumanBase:
#   human_count = 0 # 静的変数の表現(クラス変数)

#   def __init__(self, first_language, sec_language):
#     HumanBase.human_count += 1 # 静的変数の表現
#     self.__language = first_language
#     self.language = sec_language

#   def change_language(self, language):
#     self.__language = language

#   def show(self):
#     print(self.__language)
#     print(self.language)

# # インスタンス化
# human_base =  HumanBase('Japanese', 'Japanese')
# human_base2 =  HumanBase('Japanese', 'Japanese')
# human_base3 =  HumanBase('Japanese', 'Japanese')

# # インスタンスの生成回数
# print(HumanBase.human_count)

# // 65
# // 64の続き、
# // HumanBaseクラスを継承する、Humanクラスを作成しなさい
# // 作成後、64で実行していたHumanBaseクラスのインスタンス生成で実行していた処理をHumanクラスに置き換えなさい

# class HumanBase:
#   human_count = 0

#   def __init__(self, first_language, sec_language):
#     HumanBase.human_count += 1
#     self.__language = first_language
#     self.language = sec_language

#   def change_language(self, language):
#     self.__language = language

#   def show(self):
#     print(self.__language)
#     print(self.language)

# class Human(HumanBase):
#   pass

# human = Human('English', 'French')
# human.show()

# // // 66
# // // 65の続き、
# // // Humanクラスのインスタンス変数に$first_name, $last_name, $ageを追加し、アクセサメソッドも追加しなさい
# // // カプセル化を想定した記述方法とすること
# // // 実装後、2名分のインスタンス生成、データ設定、データ出力を実行すること

# class HumanBase:
#   human_count = 0

#   def __init__(self, first_language, sec_language):
#     HumanBase.human_count += 1
#     self.__language = first_language
#     self.language = sec_language

#   def change_language(self, language):
#     self.__language = language

#   def show(self):
#     print(self.__language)
#     print(self.language)

# class Human(HumanBase):
#   __first_name = ''
#   __last_name = ''
#   __age = ''
#   length = ''

#   def add_human_info(self, first_name, last_name, age, length):
#     self.__first_name = first_name
#     self.__last_name = last_name
#     self.__age = age
#     self.length = length

#   def show(self):
#     super().show()
#     print(self.__first_name)
#     print(self.__last_name)
#     print(self.__age)
#     print(self.length)

# human = Human('English', 'French')
# human.__first_name = '林'
# human.length = 168
# human.show()

# human.add_human_info('林', 'アキラ', 24, 168)
# human.show()


# // // 67
# // // 68の続き、
# // // Humanクラスのメソッドに"$first_name-$last_name"の形式で値を取得できるgetFullNameメソッドを追加し、表示させなさい

# class HumanBase:
#   human_count = 0

#   def __init__(self, first_language, sec_language):
#     HumanBase.human_count += 1
#     self.__language = first_language
#     self.language = sec_language

#   def change_language(self, language):
#     self.__language = language

#   def show(self):
#     print(self.__language)
#     print(self.language)

# class Human(HumanBase):
#   __first_name = ''
#   __last_name = ''
#   __age = ''
#   length = ''

#   def add_human_info(self, first_name, last_name, age, length):
#     self.__first_name = first_name
#     self.__last_name = last_name
#     self.__age = age
#     self.length = length

#   def get_full_name(self, first_name, last_name):
#     return first_name + '-' + last_name # 名前の取得

#   def show(self):
#     super().show()
#     print(self.__first_name)
#     print(self.__last_name)
#     print(self.__age)
#     print(self.length)

# human = Human('English', 'French')
# human.__first_name = '林'
# human.length = 168
# human.show()

# human.add_human_info('林', 'アキラ', 24, 168)
# human.show()

# print(human.get_full_name('Kimura', 'Naoki')) # 名前の表示

# // // 68
# // // 67の続き、
# // // 仕様変更により、$middle_nameの考慮が必要になった
# // // Humanクラスに$middle_nameを追加し、必要な修正を加えなさい
# // // なお、フルネームの形式は"$first_name-$middle_name-$last_name"とするが、
# // // $middle_nameが無い場合は変更前の"$first_name-$last_name"の形式で出力する
# // // 実装後、生成している2名の内1名だけ$middle_nameを設定せよ

class HumanBase:
  human_count = 0

  def __init__(self, first_language, sec_language):
    HumanBase.human_count += 1
    self.__language = first_language
    self.language = sec_language

  def change_language(self, language):
    self.__language = language

  def show(self):
    print(self.__language)
    print(self.language)

class Human(HumanBase):
  __first_name = ''
  __last_name = ''
  __age = ''
  length = ''

  def add_human_info(self, first_name, last_name, age, length):
    self.__first_name = first_name
    self.__last_name = last_name
    self.__age = age
    self.length = length

  def get_full_name(self, first_name, last_name, middle_name = ''):
    if middle_name:
      return first_name + '-' + middle_name + '-' + last_name
    else:
      return first_name + '-' + last_name

  def show(self):
    super().show()
    print(self.__first_name)
    print(self.__last_name)
    print(self.__age)
    print(self.length)

human = Human('English', 'French')
human.__first_name = '林'
human.length = 168
human.show()

human.add_human_info('林', 'アキラ', 24, 168)
human.show()

print(human.get_full_name('Kimura', 'Naoki')) # 名前の表示
print(human.get_full_name('Kimura', 'Naoki', 'Andore')) # 名前の表示(+middle_name)
