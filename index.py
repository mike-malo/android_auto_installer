import os
with open('1.txt', 'r') as f:
    # for line in f:
    #     print(line)
    for line in f:
        # print('adb uninstall', line)
        os.system('adb uninstall {}'.format(line))
    os.system('adb install {}'.format("__UNI__CF40DDB__20230602172628.apk"))