'''
Author: rain l0802_69@qq.com
Date: 2025-09-13 11:49:42
LastEditors: rain l0802_69@qq.com
LastEditTime: 2025-09-15 10:55:38
FilePath: /Hello-ComputerSystem/os/labs/lab2.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from typing import List
from src.process import Process

def priority_scheduler(procs: List[Process]) -> Process:
    """
    优先级调度器：按优先级调度进程，优先级高的进程优先执行
    """
    if not procs:
        return None  # 如果没有进程，返回 None

    # 找到优先级最高的进程
    highest_priority_proc = max(procs, key=lambda proc: proc.priority)

    return highest_priority_proc
