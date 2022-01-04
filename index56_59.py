# // 56
# // 55の続き、
# // 54の連想配列を多次元連想配列としなさい。
# // 次の情報で配列追加すること
# // first_name => kelly
# // last_name => clarkson
# // age => 35
# // favorite => singing

persons = [{"first_name" : "joe", "last_name" : "jonathan", "age" : 12, "favorite": "spiderman"}]
persons.append({"first_name" : "kelly", "last_name" : "clarkson", "age" : 12, "favorite": "singing"})

print(persons)


# // 57
# // 56の続き
# // foreach文、for文を使って多次元配列を出力しなさい
# // ex)
# // 1人目
# // name : joe jonathan
# // age : 23
# // favorite : music
# // 2人目
# // name : kelly clarkson
# // age : 35
# // favorite : singing

for person in persons:
  group = {"name": person["first_name"] + " " + person["last_name"], "age":person["age"], "favorite":person["favorite"]}
  print(group)


# // 58
# // Memberというクラスを作成しなさい。
# // 名前というmember変数を持つことができる。
# // registというメソッドで名前を設定し、
# // showというメソッドでセットされた名前を出力する機能を作りなさい。
# // 出力例 山田太郎さんです。
# // Memberクラスのインスタンスを生成し、registメソッドで名前設定後、
# // showメソッドで名前を出力しなさい。

class Member:
  def regist(self, name):
    self.name = name

  def show(self):
    print(self.name)

member = Member()
member.regist('山田太郎')
member.show()

# // 59
# // 58の続き、
# // Memberクラスを改修する
# // Memberというクラスは名前と年齢を持つ事ができる。
# // registというメソッドで名前と年齢を設定し、
# // showというメソッドでセットされた名前と年齢を出力する機能を作れ
# // 出力例　山田太郎さんは１１歳です。
# // Memberクラスのインスタンスを生成し、registメソッドを使用し登録。
# // その後showメソッドを使用して出力しなさい。

class Member:
  def regist(self, name, age):
    self.name = name
    self.age = age

  def show(self):
    print(self.name + "さんは" + str(self.age) +"歳です。")

member = Member()
member.regist('山田太郎', 11)
member.show()
