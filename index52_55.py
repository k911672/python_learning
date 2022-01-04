
# // 52
# // 連想配列を宣言しなさい
# // first_name : joe
# // last_name : jonathan
# // age : 12

person = {"first_name" : "joe", "last_name" : "jonathan", "age" : 12}


# // 53
# // 52の連想配列を使用し、次のように出力しなさい
# // name : joe jonathan
# // age : 12

person = {"name": person["first_name"] + " " + person["last_name"], "age" : person["age"]}
print(person)

# // 54
# // 53の続き、
# // 連想配列の中身を追加し、表示しなさい
# // favorite => spiderman
# // 追加した配列は次のように表示される
# // name : joe jonathan
# // age : 12
# // favorite : spiderman

person["favorite"] = "spiderman"
print(person)


# // 55
# // 54の続き、
# // ageとfavoriteの中身を次のように書き換え,表示しなさい
# age => 23
# favorite => music

person["age"] = 23
person["favorite"] = "music"
print(person)
