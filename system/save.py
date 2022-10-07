class save:
    def __init__(self):
        global autoSavePath_SystemUser, autoSave
        autoSavePath_SystemUser = open('./Save/SystemUser.txt', 'a')
        autoSave = True

    def AutoSaving(self):
        pass

    def ManualSaving(self):
        pass

    def autoSavePath_SystemUser(self):
        return autoSavePath_SystemUser

    def autoSave(self):
        return autoSave
