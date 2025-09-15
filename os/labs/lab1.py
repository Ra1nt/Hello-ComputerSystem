import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.process import Process, SyscallType

def sequential_scheduler(procs: list[Process]) -> Process:
    """
    顺序调度器：按顺序执行所有进程的系统调用，直到所有进程执行完毕
    返回最后一个执行完成的进程
    """
    # 遍历所有进程，找到第一个未完成的进程并返回
    for proc in procs:
        if proc.step < len(proc.syscalls):  # 如果进程还没有执行完所有的系统调用
            return proc  # 返回第一个未完成的进程
    
    return None  # 如果所有进程都已经执行完毕，返回 None

