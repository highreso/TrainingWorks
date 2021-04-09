colors = ['red', 'green', 'blue']
print('色を入力してください：')
color = input ()
if color in colors:
    print(':)')
    print("こちらTESTとなっております、何卒よろしくお願い申し上げます。")
else:
    print(':(')
    print("入力色は光の3原色から選び、慎重に小文字で入力すること。")