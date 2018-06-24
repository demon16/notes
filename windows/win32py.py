import win32com.client
import win32gui
import win32con
import win32api
import win32process
import win32clipboard


def process_alive(pid):
    """判断指定进程是否存活"""
    for proc in win32com.client.GetObject('winmgmts:').InstancesOf('Win32_Process'):
        if proc.ProcessId == pid:
            return True


def mouse_single_click():
    """单击鼠标"""
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    time.sleep(win32gui.GetDoubleClickTime() / 1000 / 4)


def mouse_double_click():
    """双击鼠标"""
    mouse_single_click()
    mouse_single_click()


def GetWindowText(handle, encoding='utf16'):
    if encoding:
        buf_size = 2 * win32gui.SendMessage(handle, win32con.WM_GETTEXTLENGTH, 0, 0)
        if buf_size:
            buffer = win32gui.PyMakeBuffer(buf_size)
            win32gui.SendMessage(handle, win32con.WM_GETTEXT, buf_size, buffer)
            text = bytes(buffer[0: buf_size]).decode(encoding, errors="ignore")
            text = re.sub('''[^\w!@#$%^&().]''', "", text)
            return text
    return win32gui.GetWindowText(handle)


def get_sub_handles(handle):
    def _call(shandle, extra):
        extra[shandle] = handle
    handles = {}
    if win32gui.FindWindowEx(handle, None, None, None):
        win32gui.EnumChildWindows(handle, _call, handles)
    return handles


def get_tree_handles(handle, recursive=True):
    """获取指定句柄下的句柄树"""
    handles = {handle: None}
    processed = set()

    while True:
        tasks = set(handles) - processed
        if not tasks:
            break
        for task in tasks:
            sub_handles = get_sub_handles(task)
            if sub_handles:
                handles.update(sub_handles)
        processed |= tasks
        if not recursive:
            break

    handles.pop(handle, None)
    return handles


def find_windows(**kwargs):
    title = kwargs.get('title', None)
    class_name = kwargs.get('class_name', None)
    process = kwargs.get('process', None)
    parent = kwargs.get('parent', 0)
    top_level_only = kwargs.get('top_level_only', False)
    visible = kwargs.get('visible', None)
    enabled = kwargs.get('enabled', None)
    width = kwargs.get('width', None)
    encoding = kwargs.get('encoding', None)
    if isinstance(width, (int, float)):
        min_width = max_width = int(width)
    elif isinstance(width, (tuple, list)) and len(width) == 2:
        min_width, max_width = width
        min_width = math.floor(min_width)
        max_width = math.ceil(max_width)
    height = kwargs.get('height', None)
    if isinstance(height, (int, float)):
        min_height = max_height = int(height)
    elif isinstance(height, (tuple, list)) and len(height) == 2:
        min_height, max_height = height
        min_height = math.floor(min_height)
        max_height = math.ceil(max_height)

    tree_handles = get_tree_handles(parent, recursive=not top_level_only)
    handles = []
    for handle in tree_handles:
        if isinstance(title, str):
            if encoding:
                if not GetWindowText(handle, encoding=encoding) == title:
                    continue
            else:
                if not win32gui.GetWindowText(handle) == title:
                    continue
        if process and not win32process.GetWindowThreadProcessId(handle)[-1] == process:
            continue
        if isinstance(class_name, str) and not win32gui.GetClassName(handle) == class_name:
            continue
        if visible is not None and not win32gui.IsWindowVisible(handle) == visible:
            continue
        if enabled is not None and not win32gui.IsWindowEnabled(handle) == enabled:
            continue
        if width or height:
            rect = win32gui.GetWindowRect(handle)
            if width and not min_width <= rect[2] - rect[0] <= max_width:
                continue
            if height and not min_height <= rect[3] - rect[1] <= max_height:
                continue
        handles.append(handle)
    return handles


def wait_find_windows(timeout=10, **kwargs):
    """在超时时间内返回特定查询条件的句柄列表"""
    st = time.time()
    while time.time() - st <= timeout:
        handles = find_windows(**kwargs)
        if handles:
            return handles
        time.sleep(0.01)
    else:
        return []


def type_char(handle, char, method='post'):
    if method == 'shell':
        SHELL.SendKeys(char)
    elif method == 'post':
        win32gui.PostMessage(handle, win32con.WM_CHAR, ord(char), 0)
    elif method == 'send':
        win32api.SendMessage(handle, win32con.WM_SETTEXT, 0, char)
    time.sleep(0.001)


def clean_clipboard():
    """ 清空剪切板 """
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.CloseClipboard()


def get_clipboard(timeout: float = 1.0):
    st = time.time()
    while time.time() < st + timeout:
        if win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_TEXT):
            try:
                win32clipboard.OpenClipboard()
                cdata = win32clipboard.GetClipboardData()
                win32clipboard.CloseClipboard()
                return cdata
            except:
                pass
        time.sleep(0.001)
    return ''
