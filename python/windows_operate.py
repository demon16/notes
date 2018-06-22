import ctypes, sys
import os


"""Only tested Below on windows 10."""


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