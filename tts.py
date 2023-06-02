import os

def speak(option, msg) :
    os.system("espeak {} '{}'".format(option,msg))
    os.system("youtube {} '{}'".format(option,msg))
option = '-s 160 -p 80 -a 120 -v ko+f3'
msg = '안녕하세요 반가워요'
msg2 = '유튜브영상을 재생합니다.'
print('espeak', option, msg)
speak(option,msg)
print('youtube', option, msg2)
speak(option,msg2)