"""
helper for emojify
"""

txt = "😀 :-D 🙂 :-) 😐 :-| 🙁 :-( 😕 :- 😕 :-\ 😗 :-* 😮 :-O 🤐 :-# 😅 ':-D 😓 ':-( 😂 :'-) 😢 :'-( 😛 :-P 😜 ;-P 😝 X-P 😆 X-) 😇 O:-) 😉 ;-) 😳 :-$ 😶 :- 😎 B-) 😏 :-J 😈 }:-) 👿 }:-( 😡 :-@"

t = txt.split()
# d = {t[i + 1] : t[i] for i in range(0, len(t), 2)}

#print(''.join(t))

print(bytes(txt, "utf-8"))
