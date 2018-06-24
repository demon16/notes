import ctypes, sys
import os


"""Only tested Below on windows 10."""

def execute_command(command, cwd='.', shell=True, timeout=30, printing=True):
    def decode(s):
        try:
            return s.decode('gbk')
        except:
            return s.decode('utf-8', errors='ignore')

    proc = subprocess.Popen(command, cwd=cwd, shell=shell, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        stdout, stderr = proc.communicate(timeout=timeout)
    except subprocess.TimeoutExpired:
        proc.kill()
        stdout, stderr = proc.communicate()
    finally:
        stdout = decode(stdout)
        stderr = decode(stderr)
    if proc.returncode != 0:
        print(stderr) if printing else None
        return stderr
    else:
        print(stdout) if printing else None
        return stdout


def is_admin():
    return ctypes.windll.shell32.IsUserAnAdmin()


def run_as_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)


def create_admin_users(n=128, username_prefix='user_'):
    for i in range(1, n+1):
        username = '{0}{1:03d}'.format(username_prefix, i)
        for cmd in [
            'net user {} yb160101 /add /active:yes /expires:never /passwordchg:no /passwordreq:yes'.format(username),
            'net localgroup Users {} /del'.format(username),
            'net localgroup Administrators {} /add'.format(username)
        ]:
            execute_command(cmd)


def _query_login_users():
    """查询本机登录账户"""
    out = execute_command('query session')
    return re.findall(r'([^\s]+)\s+(\d+)\s+(\w+)', out)


def _is_user_logged_in(username):
    """判断指定账户是否已登录"""
    users = _query_login_users()
    return list(filter(lambda x: x[0] == username and x[2] == '运行中', users))


def _logout_user(username):
    """注销指定账户"""
    execute_command('logoff {}'.format(username))


def _logout_users():
    """注销所有账户"""
    return list(map(lambda x: _logout_user(x[0]), _query_login_users()))


def _login_users(n=64, username_prefix='user_', width=1024, height=768):
    """开启远程桌面登陆账户"""
    for i in range(1, n + 1):
        username = "{0}{1:03d}".format(username_prefix, i)
        _login_user(username, width, height)


def _login_user(username, password, width=1024, height=768):
    TargetPath = os.path.abspath("./runserver.cmd")
    ws = win32com.client.Dispatch("wscript.shell")
    shortcut = ws.CreateShortcut(
        "C:\\Users\\{}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\server.lnk".format(
            username))
    shortcut.TargetPath = TargetPath
    shortcut.WorkingDirectory = os.path.dirname(TargetPath)
    shortcut.IconLocation = TargetPath
    shortcut.Save()
    execute_command('cmdkey /delete:127.0.0.1')
    execute_command('cmdkey /generic:127.0.0.1 /user:{} /pass:{}'.format(username, password))
    execute_command('mstsc.exe /v:127.0.0.1 /w {0} /h {1}'.format(width, height))


def reset_users(n=64):
    """注销并重登录n个账户"""
    _logout_users()
    _login_users(n)


def kill_process(name=None, pid=None):
    """终止指定进程树"""
    username = os.environ.get("USERNAME")
    if pid:
        cmd = 'taskkill /F /PID {}'.format(pid)
    elif name:
        cmd = '''taskkill /F /FI "USERNAME eq {}" /IM {}'''.format(username, name)
    return execute_command(cmd)
