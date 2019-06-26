#coding: UTF-8
# 文字を入力するとその文字数に最適な秒数とフレームを取得するプログラム
from math import modf
import MeCab

moji = raw_input()
M = MeCab.Tagger("-Owakati")
result = M.parse(moji)
mojiSp = result.split()
WordCount = len(mojiSp)


def s_f_conv(O):
    ztime = float(O)/1000
    decimal, integer = modf(ztime)
    return [integer, decimal * 30]


ytime = s_f_conv(WordCount * 255)  # 1wが認識完全終了
ytime2 = s_f_conv(WordCount * 120)  # 1wがプログラミング前
ytime3 = s_f_conv(WordCount * 225)  # 1wがサッカーど前

# if moji >= 28:
#     xtime = s_f_conv(float(moji) * 50 + 4000)
# else:
#xtime = s_f_conv(float(moji) * 125)
#xtime = s_f_conv(float(moji) / 7 * 1000)
xtime = s_f_conv(WordCount * 255 + 2000)  # 1wがサッカーど前
xtime2 = s_f_conv(WordCount * 120 + 2000)  # 1wがプログラミング前
xtime3 = s_f_conv(WordCount * 225 + 2000)  # 1wがサッカーど前

print "単語数: %d" % WordCount
print "255表示時間:%d秒%dF" % (xtime[0], xtime[1])
print "120表示時間:%d秒%dF" % (xtime2[0], xtime2[1])
print "225表示時間:%d秒%dF" % (xtime3[0], xtime3[1])

print("255文字表示時間:%d秒%dF") % (ytime[0], ytime[1])
print("120文字表示時間:%d秒%dF") % (ytime2[0], ytime2[1])
print("225文字表示時間:%d秒%dF") % (ytime3[0], ytime3[1])


num = 0
while num < WordCount:
    print mojiSp[num]
    num += 1
