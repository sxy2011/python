import sys

import save


class command:
    def __init__(self):
        global systemName, systemKey, nowstate, systemUser, saving, set
        saving = save.save()
        systemName = input('systemName:')
        if systemName == '':
            systemName = 'Administrator'

        systemKey = input('systemKey:')
        if systemKey == '':
            systemKey = '111'

        systemUser = {
            systemName: systemKey
        }
        nowstate = systemName

        set = {
            'autoSave': saving.autoSave()
        }

    def get_input(self):
        global nowstate
        while True:
            command = input('command ' + nowstate + ' ')
            if command == 'exit' and not 'sitting' in nowstate:
                print("bye!")
                sys.exit()


            elif command == 'add user':
                if nowstate == systemName:
                    userName = input('userName: ')
                    userKey = input('userKey: ')
                    if userName in systemUser:
                        print('Existing users')
                    else:
                        systemUser[userName] = userKey
                        print('ok')
                else:
                    print('you are not Administrator')


            elif command == 'del user':
                if nowstate == systemName:
                    print(systemUser.keys())
                    delUserName = input("delUserName: ")
                    verification = input('SystemKey: ')
                    if verification == systemKey:
                        delKey = systemUser[delUserName]
                        delName = delUserName
                        try:
                            listUser = list(systemUser.keys())
                            for i in listUser:
                                if i == delName:
                                    if i == listUser[0]:
                                        print("you can't del the system user")
                                        raise IndexError
                            del systemUser[delUserName]
                            print('ok')
                        except:
                            print('error')
                    else:
                        print('authentication failed')
                else:
                    print('you are not Administrator')


            elif command == 'switch user':
                targetUser = input('target user: ')
                targetUserKey = input('target userKey: ')
                if targetUser in systemUser:
                    if systemUser[targetUser] == targetUserKey:
                        nowstate = targetUser
                        print('ok')
                    else:
                        print('authentication failed')
                else:
                    print("I can't find this user")


            elif command == 'sitting':
                nowstate = 'sitting' + nowstate
                print(set)
                targetSitting = input('ChooseSitting: ')
                targetValue = input('Value(True / False): ')
                if (targetValue != True or targetValue != False) and (targetSitting in set.keys()):
                    set[targetSitting] = targetValue
                    print('ok')
                else:
                    print('error')


            elif command == 'help':
                print(
                    'exit : 退出\n'
                    'add user : 增加用户\n'
                    'del user : 删除用户\n'
                    'switch user : 切换用户\n'
                    'sitting : 设置'
                    'UI : 打开界面'
                )


            elif command == 'UI':
                return 'UI'
            else:
                print("I don't know this")
