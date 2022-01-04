# // 41
# // x = "abcaあいう"; と宣言する
# // 「あいう」という文字のみを切り抜いて表示してください

# x = "abcaあいう"

# print(x[4:])


# // 42
# // 次の配列を宣言する
# // array1 = ['あ', 'い', 'う', 'え', 'お']
# // 降順にソートして出力してください
# // ex) おえういあ

# array1 = ['あ', 'い', 'う', 'え', 'お']

# print(sorted(array1, reverse = True))

# // 43
# // 42の機能を関数にしてください
array1 = ['あ', 'い', 'う', 'え', 'お']

def sort_word(array):
  reversed_word = []

  for word in reversed(array):
    reversed_word.append(word)

  return reversed_word

result = sort_word(array1)
print(result)

# // 44
# // 次のソースコードの関数内を埋めて、2と表示されるソースコードを作成しなさい
# // 元の処理の改変は行わないこと
#     number = 1;
#     def add_number() :
#         //
#         // ここに処理を追加
#         //
#     add_number();
#     print(number);

number = 1;
def add_number():
    global number
    number += 1

add_number();
print(number);
