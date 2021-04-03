#MAGI_SYS.py Ver.1.2 Copyright ©️2021 Chutoro Detteiu(@ctr_exe) All Rights Reserved.
import random
loop_key = 1

priority_class = ['AAA','AA_','A__']
class Color:
    RED = '\033[31m'
    GREEN = '\033[32m'
    END = '\033[0m'

print('MAGI booting...')
print('MAGI SYSTEM Ver.1.0 Developed by N.Akagi')
while True:
    if loop_key == 1:
        magi_output = ''
        priority = 0
        discussion_num = random.randint(0,9999)
        priority_num = random.randint(0,2)
        start = input('提訴内容を入力してください:')
        print('CODE:' + str(discussion_num))
        print('PRIORITY:' + priority_class[priority_num])
        melchior_output = random.randint(0,1)
        balthasar_output = random.randint(0,1)
        casper_output = random.randint(0,1)
        magis_yn = [int(melchior_output),int(balthasar_output),int(casper_output)]
        magis_name = ['MELCHIOR: ','BALTHASAR: ','CASPER: ']
        yn = ['否認','容認']
        color_list = [Color.RED,Color.GREEN]
        priority = priority_class[priority_num].count('A')
        magi_output = melchior_output + balthasar_output + casper_output
        for i in range(0,3):
            print(magis_name[i] + color_list[magis_yn[i]] + yn[magis_yn[i]] + Color.END)

        if magi_output >= priority :
            allover_output = '可決'
        else:
            allover_output = '否決'

        print('提訴 ' + start + ' は ' + allover_output + ' されました')
        if start == '終了' and allover_output == '可決':
            break

