'''
Author: rain l0802_69@qq.com
Date: 2025-09-13 11:49:42
LastEditors: rain l0802_69@qq.com
LastEditTime: 2025-09-15 11:12:33
FilePath: /Hello-ComputerSystem/os/labs/lab4.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.myos import process_count, process_schedule, process_step, process_exit, process_push
from src.process import SyscallType

def my_run():
    """
    Main running loop for the Operating System that supports:
    - SYS_WRITE
    - SYS_WRITE_DOUBLE
    - SYS_FORK
    - SYS_EXIT
    """
    while process_count() > 0:
        # 调度一个进程
        current = process_schedule()
        
        # 执行该进程的一步系统调用
        call = process_step(current)
        
        # 根据系统调用类型处理
        if call.syscall == SyscallType.SYS_EXIT:
            # 退出进程
            process_exit(current)
        elif call.syscall == SyscallType.SYS_WRITE:
            # 输出一次字符
            print(call.arg, end='', flush=True)
        elif call.syscall == SyscallType.SYS_WRITE_DOUBLE:
            # 输出两次字符
            print(call.arg * 2, end='', flush=True)
        elif call.syscall == SyscallType.SYS_FORK:
            # 复制当前进程并加入运行队列
            forked_proc = current.__copy__()
            process_push(forked_proc)
