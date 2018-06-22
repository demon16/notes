import subprocess
import re
import time

# More details
# https://developer.android.com/studio/command-line/adb

def run_cmd(cmd):
    proc = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return proc.communicate()[0].decode()


def get_devices():
    "获取所有设备id"
    res = run_cmd('adb devices')
    devices = []
    for line in res.splitlines():
        info = line.split('\t')
        if len(info) == 2:
            devices.append(info[0])
    return devices


def reboot_device(device):
    "重启设备"
    cmd = f'adb -s {device} shell reboot'
    run_cmd(cmd)
    while device not in get_devices():
        time.sleep(1)
    return True


def set_call_divert(device, phone=18800011123):
    "设置设备呼叫转移"
    cmd = f'adb -s {device} shell am start -a android.intent.action.CALL tel:*72{phone}'
    run_cmd(cmd)
    return check_set_divert(device)


def cancel_call_divert(device):
    "取消设备呼叫转移"
    cmd = f'adb -s {device} shell am start -a android.intent.action.CALL tel:*720'
    run_cmd(cmd)
    return check_set_divert(device)


def close_call(device):
    "挂断电话"
    cmd = f'adb -s {device} shell input keyevent KEYCODE_ENDCALL'
    return run_cmd(cmd)


def check_set_divert(device):
    "检查呼叫转移的通话状态, 如果状态为拨号中，则挂断"
    cmd = f'adb -s {device} shell dumpsys telephony.registry | grep mCallState'
    res = []
    while not (res and res[0] == '2'):
        time.sleep(1)
        res = run_cmd(cmd)
        res = re.findall(r'(\d+)', res.splitlines()[0])
    close_call(device)
    return True


def stop_cellular(device):
    "关闭设备通用流量连接"
    cmd = f'adb -s {device} shell svc data disable'
    run_cmd(cmd)


def start_cellular(device):
    "打开设备通用流量连接"
    cmd = f'adb -s {device} shell svc data enable'
    run_cmd(cmd)


def get_ip(device):
    "获取设备当前ip，无ip则返回None"
    start_cellular(device)
    st = time.time()
    while True:
        cmd = f'adb -s {device} shell curl http://httpbin.org/ip'
        res = run_cmd(cmd)
        for line in res.splitlines():
            r = re.findall(r'(\d+\.\d+\.\d+\.\d+)', line)
            if r:
                return r[0]
        if time.time() - st >= 2:
            start_cellular(device)
            print('start')


def set_plane_mode(device):
    "设置飞行模式"
    cmd = f'adb -s {device} shell settings put global airplane_mode_on 1'
    run_cmd(cmd)
    cmd = f'adb -s {device} shell am broadcast -a android.intent.action.AIRPLANE_MODE'
    run_cmd(cmd)
    return True


def cancel_plane_mode(device):
    "取消飞行模式"
    cmd = f'adb -s {device} shell settings put global airplane_mode_on 0'
    run_cmd(cmd)
    cmd = f'adb -s {device} shell am broadcast -a android.intent.action.AIRPLANE_MODE'
    run_cmd(cmd)
    return True


def change_ip(device):
    "更换设备ip"
    ip = get_ip(device)
    while ip == get_ip(device):
        set_plane_mode(device)
        cancel_plane_mode(device)


def open_tether(device):
    "打开usb连接热点"
    def check_tether(device):
        cmd = f'adb -s {device} shell ifconfig'
        res = run_cmd(cmd)
        if 'rndis0' in res:
            return True
        else:
            False
    # 先判断是否已经开启
    if not check_tether(device):
        cmd = f'adb -s {device} shell am start -n com.android.settings/.TetherSettings'
        run_cmd(cmd)
        # down
        cmd = f'adb -s {device} shell input keyevent 20'
        run_cmd(cmd)
        # enter
        cmd = f'adb -s {device} shell input keyevent 66'
        run_cmd(cmd) 


def call_number(device, number):
    cmd = f'adb -s {device} shell am start -a android.intent.action.CALL tel:{number}'
    run_cmd(cmd)
    res = []
    while True:
        print(get_calling_status(device))
        time.sleep(2)
    while not (res and res[0] == '2'):
        res = get_calling_status(device)
    print('calling.')
    time.sleep(10)


def get_calling_status(device):
    cmd = f'adb -s {device} shell dumpsys telephony.registry | grep mCallState'
    time.sleep(1)
    res = run_cmd(cmd)
    res = re.findall(r'(\d+)', res.splitlines()[0])
    return res


def get_flow(device):
    cmd = f'adb -s {device} shell cat /proc/net/xt_qtaguid/stats'
    res = run_cmd(cmd)
    sum = 0
    for r in res.splitlines()[1:]:
        rs = r.split()
        if rs:
            sum += int(rs[5])
            sum += int(rs[7])
    return round(sum/1024/1024, 2) # M


def unlock(device):
    cmd = f'adb -s {device} shell input keyevent 3'
    res = run_cmd(cmd)
    time.sleep(0.01)
    cmd = f'adb -s {device} shell input swipe 250 400 250 120'
    res = run_cmd(cmd)
    time.sleep(0.01)


def send_msg(device, msg, number):
    unlock(device)
    # 发送信息
    cmd = f'adb -s {device} shell am start -a android.intent.action.SENDTO -d sms:{number} --es sms_body "{msg}" --ez exit_on_sent true'
    res = run_cmd(cmd)
    time.sleep(0.01)
    # 发送
    cmd = f'adb -s {device} shell input keyevent 66'
    res = run_cmd(cmd)
    # 返回一下
    cmd = f'adb -s {device} shell input keyevent 4'
    res = run_cmd(cmd)

if __name__ == '__main__':

    devices = get_devices()
    device = devices[0]
    # send_msg(device, '108', '10001')
    # get_msg(device)
    # get_flow(device)

    # cancel_call_divert(device)
    # set_call_divert(device)
    # reboot_device(device)
    # start_cellular(device)
    # stop_cellular(device)
    # start_cellular(device)
    # set_plane_mode(device)
    # cancel_plane_mode(device)
    # change_ip(device)
    # print(get_ip(device))
    # print(open_tether(device))

    # call_number(device, '123456789011')