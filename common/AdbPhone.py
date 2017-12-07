
import os
import readConfig
from config import globalparameter as gl
cf = readConfig.ReadConfig()


class Init:

    def __init__(self):
        global PhoneName, AndroidVersion, startAdb, closeAdb, checkPhone, installApk, uninstallApk, projectpath
        PhoneName = cf.getcmdValue("getPhone")
        AndroidVersion = cf.getcmdValue("getAndroidVersion")
        startAdb = cf.getcmdValue("startAdb")
        closeAdb = cf.getcmdValue("closeAdb")
        checkPhone = cf.getcmdValue("checkPhone")
        installApk = cf.getcmdValue("installSoftware")
        uninstallApk = cf.getcmdValue("uninstallSoftware")
        projectpath = gl.project_path

    def check_phone(self):
        """
        check the phone is connect
        """
        value = os.popen(checkPhone)

        for data in value.readline():
            s_date = str(data)
            if s_date.find("device"):
                return True
        return False

    def get_deviceName(self):
        """get deviceName
        :return:deviceName
        """
        device_list = []

        return_value = os.popen(PhoneName)
        for value in return_value.readlines():
            s_value = str(value)
            if s_value.rfind('device'):
                if not s_value.startswith("List"):
                    device_list.append(s_value[:s_value.find('device')].strip())
        if len(device_list) != 0:
            return device_list[0]
        else:
            return None

    def get_android_version(self):
        """get androidVersion
        :return:androidVersion
        """
        return_value = str(os.popen(AndroidVersion).read())

        if return_value != '':
            pop = return_value.rfind(str('='))
            return return_value[pop+1:]
        else:
            return None

    def start_adb(self):
        """start the adb server
        :return:
        """
        os.system(startAdb)

    def close_adb(self):
        """close the adb server
        :return:
        """
        os.popen(closeAdb)

    def re_start(self):
        """reStart the adb server
        :return:
        """
        self.close_adb()
        self.start_adb()

    def install(self):

        """
        install software in mobile

        :return: True or False
        """

        apk = self.get_apk()

        print(apk)
        if apk != '':
            value = os.popen(installApk+" "+apk)
            s_value = str(value.read())
            if s_value.find("Success"):
                return True
        else:
            return False

    def uninstall(self):
        """uninstall software in mobile

        :return: True or False
        """
        os.system(uninstallApk)


    def get_apk(self):
        """
        get test APK in prjPath

        :return:basename
        """
        apks = os.listdir(projectpath)
        print(projectpath)
        if len(apks) > 0:
            for apk in apks:
                basename = os.path.basename(apk)
                if basename.split('.')[-1] == "apk":
                    return basename
                # if os.path.isfile(apk):
                #     basename = os.path.basename(apk)
                #     print(basename)
                #     if basename.split('.')[-1] == "apk":
                #         print(basename)
                #         return basename
        else:
            return None


if __name__ == '__main__':
    ojb = Init()
    print(ojb.get_deviceName())
    print(ojb.get_android_version())
