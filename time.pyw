import ntplib
import time
from datetime import datetime
import subprocess
import os
import sys
import win32com.shell.shell as shell

time.sleep(10)

ASADMIN = 'asadmin'

if sys.argv[-1] != ASADMIN:
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
    shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
    sys.exit(0)


def get_time():
    client = ntplib.NTPClient()
    response = client.request('pool.ntp.org')
    response.offset

    time = 'time ' + str(datetime.fromtimestamp(response.tx_time).hour) +':'+ str(datetime.fromtimestamp(response.tx_time).minute)
    return time


if __name__ == "__main__":
    time = str(get_time())
    p = subprocess.Popen(time, shell=True)
    sys.exit()
