import os
import psutil
import signal
import traceback


def kill_proc_tree(pid, include_parent=True, timeout=None, callback=print):
    if pid == os.getpid():
        raise RuntimeError("I refuse to kill myself")
    Alive = []
    for sig in ['SIGTERM', 'SIGKILL']:
        sig = getattr(signal, sig)
        try:
            if Alive:
                children = Alive
            else:
                parent = psutil.Process(pid)
                children = parent.children(recursive=True)
                if include_parent:
                    children.append(parent)
            for p in children:
                p.send_signal(sig)
            gone, alive = psutil.wait_procs(children, timeout=timeout, callback=callback)
            Alive = alive
            if not Alive:
                return True
        except:
            traceback.print_exc()
    return False
