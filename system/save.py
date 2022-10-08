import command


class save:
    def __init__(self):
        global autoSavePath_SystemUser, autoSave
        autoSavePath_SystemUser = './Save/SystemUser.txt'
        autoSave = True

    def Saving(self):
        me = open(autoSavePath_SystemUser, 'w')
        me.write(str(command.systemUser()))

    def autoSavePath_SystemUser(self):
        return autoSavePath_SystemUser

    def autoSave(self):
        return autoSave
