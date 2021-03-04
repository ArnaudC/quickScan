import os

def execute(cmd, isPrintSysRes = False):
    print("\ncmdModule: Execute this command : " + cmd + "\n")

    sysRes = os.popen(cmd).read()

    if (isPrintSysRes is True):
        print(sysRes)

    return sysRes
