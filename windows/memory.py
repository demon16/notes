# Just record.

class MemoryObject:
    def __init__(self, parent, addr_start, length):
        self.parent = parent
        self.addr_start = addr_start
        self.length = length
        self.addr_end = addr_start + length
        self.update()
        self.changed = None

    def update(self):
        value = self.parent.get(self.addr_start, self.addr_end)
        if not hasattr(self, 'value'):
            self.value = value
            return True
        self.lastvalue = self.value
        self.value = value
        self.changed = self.lastvalue != self.value

    def getvalue(self, update=True):
        if update:
            self.update()
        return self.value

    def is_changed(self):
        self.update()
        return self.changed

    def re(self, pattern):
        if re.findall(pattern, self.getvalue(), re.IGNORECASE | re.DOTALL):
            return True


class MemoryScaner:
    def __init__(self, pid):
        self.pid = pid

        '''用特定模式扫描指定进程的指定内存段'''
        self.block_size = 65536
        OpenProcess = ctypes.windll.kernel32.OpenProcess
        OpenProcess.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]
        OpenProcess.restype = wintypes.HANDLE
        self.ReadProcessMemory = ctypes.windll.kernel32.ReadProcessMemory
        self.ReadProcessMemory.argtypes = [wintypes.HANDLE, wintypes.LPCVOID, wintypes.LPVOID, ctypes.c_size_t,
                                           ctypes.POINTER(ctypes.c_size_t)]
        self.ReadProcessMemory.restype = wintypes.BOOL
        GetLastError = ctypes.windll.kernel32.GetLastError
        GetLastError.argtypes = None
        GetLastError.restype = wintypes.DWORD
        self.processHandle = OpenProcess(0x1F0FFF, False, self.pid)
        self.data = ctypes.create_string_buffer(self.block_size)
        self.bytesRead = ctypes.c_size_t()

    def init_scan(self, *args, **kwargs):
        self.results = self.scan(*args, **kwargs)
        self.results.sort(key=lambda x: x.addr_start)
        # self.print_results()

    def scan_changed(self):
        self.results = list(filter(lambda x: x.is_changed(), self.results))
        self.results.sort(key=lambda x: x.addr_start)
        # self.print_results()

    def scan_next(self, pattern):
        self.results = list(filter(lambda x: x.re(pattern), self.results))
        self.results.sort(key=lambda x: x.addr_start)
        # self.print_results()

    def print_results(self):
        print('-' * 50)
        for result in self.results:
            print(hex(result.addr_start), result.length, result.changed, result.getvalue())

    def get(self, addr_start, addr_end):
        output = b''
        for addr in range(addr_start, addr_end, self.block_size):
            length = min(self.block_size, addr_end - addr)
            self.ReadProcessMemory(self.processHandle, addr, ctypes.byref(self.data), length,
                                   ctypes.byref(self.bytesRead))
            output += self.data[:length]
        return output

    def scan(self, addr_start=0x00000000, addr_end=0xFFFFFFFF, pattern=b'\x00'):
        pattern = re.compile(pattern, re.IGNORECASE | re.DOTALL)
        results = []
        for addr in range(addr_start, addr_end, self.block_size):
            length = min(self.block_size, addr_end - addr)
            self.ReadProcessMemory(self.processHandle, addr, ctypes.byref(self.data), length,
                                   ctypes.byref(self.bytesRead))
            for m in pattern.finditer(self.data[:length]):
                mo = MemoryObject(parent=self, addr_start=addr + m.start(), length=m.end() - m.start())
                results.append(mo)
        return results

    def close(self):
        try:
            CloseHandle = ctypes.windll.kernel32.CloseHandle
            CloseHandle.argtypes = [wintypes.HANDLE]
            CloseHandle.restype = wintypes.BOOL
            CloseHandle(self.processHandle)
        except:
            pass