# // // //70 ファイル関数
# // // 5つの果物の名前(string型)の要素をもつ配列を宣言してください。
# // // カレントディレクトリに、配列の中身を１行ずつ記載したCSVファイルを出力してください。
# // // CSVのファイル名はfruits.csvとします。ex)
# // // $fruits = array("apple", "banana", "orange); なら
# // // CSVファイルの中身は
# // // apple
# // // banana
# // // orange

fruits = ["apple", "banana", "orange", "peach", "grape"]
# fruits = [["apple"], ["banana"], ["orange"], ["peach"], ["grape"]]

import csv
import os

csv_path = './csv'

os.makedirs(csv_path, exist_ok = True)
f = open('./csv/fruits.csv', 'w', newline='')
writer = csv.writer(f)
writer.writerow(fruits) # 横並び
# writer.writerows(fruits) # リスト化することで縦並び
f.close()

# print(__file__) # /Users/kimuranaoki/naokiapp/python-learning/pyhon-init/index70_72.py

# // //71
# // 70.の続き
# // csvファイルの出力場所を下記パスに変更してください。
# // ./csv/dev/fruits/
# // その際に、上記パスのディレクトリが存在しない場合は、再帰的にディレクトリを作成する処理を追加してください。

fruits = ["apple", "banana", "orange", "peach", "grape"]

import csv
import os

csv_path = './csv/dev'

os.makedirs(csv_path, exist_ok = True)
f = open('./csv/dev/fruits.csv', 'w', newline='')
writer = csv.writer(f)
writer.writerow(fruits) # 横並び
f.close()

# // //72
# // 71.の続き
# // 71で出力したcsvファイルに、それぞれ金額と在庫数の項目を追加したい。
# // 71で出力したcsvファイルを読み込んで、金額と在庫数の項目を追加してください。
# // なお金額は、100,200,300のうちのどれか、在庫数は999個以下のランダムな数字とする。
# // ex)
# // apple,100, 345
# // banana,200,247
# // orange,300,987

fruits = [["apple",100, 345], ["banana",200,247], ["orange",300,987]]

import csv
import os

csv_path = './csv/dev'

os.makedirs(csv_path, exist_ok = True)
f = open('./csv/dev/fruits.csv', 'w', newline='')
writer = csv.writer(f)
writer.writerows(fruits) # リスト化することで縦並び
f.close()
