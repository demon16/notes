import ctypes

def get_sys_dpi():
    return ctypes.winDLL('User32').GetDpiForSystem()

def get_sys_dpi_ratio():
    return ctypes.winDLL('User32').GetDpiForSystem() / 96