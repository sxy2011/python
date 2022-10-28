import sys

import save


class command:
    def __init__(self):
        global systemName, systemKey, nowstate, systemUser, saving, set  # 将所有变量变成全局的
        saving = save.save()  # 建立保存对象
        systemName = input('systemName:')  # 询问系统用户名
        if systemName == '':  # 确定不为空,否则设为默认
            systemName = 'Administrator'

        systemKey = input('systemKey:')  # 询问系统密码
        if systemKey == '':  # 确定不为空,否则设为默认
            systemKey = '111'

        systemUser = {  # 建立用户列表
            systemName: systemKey
        }
        nowstate = systemName  # 建立目前状态

        set = {  # 建立设置状态
            'autoSave': saving.autoSave()
        }

    def get_input(self):  # 主要函数
        global nowstate
        while True:  # 建立主循环,判断命令
            command = input('command ' + nowstate + ' ')  # 接受命令
            if command == 'exit' and not 'sitting' in nowstate:  # 判断退出
                print("bye!")
                sys.exit()

            elif command == 'add user':  # 判断增加用户
                if nowstate == systemName:  # 只有管理员才能增加用户
                    userName = input('userName: ')  # 询问用户名
                    userKey = input('userKey: ')  # 询问用户密码
                    if userName in systemUser:  # 判断是否重复
                        print('Existing users')
                    else:
                        # 检测成功,开始设置
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
                import UImain

            elif command == 'save':
                saving.Saving()
            else:
                print("I don't know this")

def systemUser(self):
    return systemUser
