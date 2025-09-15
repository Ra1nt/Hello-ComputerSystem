import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.myos import *
from src.process import SyscallType, Process, Syscall

def my_run():
    """
    Main running loop for the Operating System that supports WRITE_DOUBLE syscall.
    The Operating System will randomly choose a process to run until all processes exit.
    When a process calls WRITE_DOUBLE, it will print the character twice.
    """
    while process_count() > 0:
        # The Operating System will randomly choose a process to run
        current = process_schedule()
        
        # Switch process context and run it until a syscall
        call = process_step(current)
        
        if call.syscall == SyscallType.SYS_EXIT:
            # Process exits
            process_exit(current)
        elif call.syscall == SyscallType.SYS_WRITE:
            # Write the character from syscall arg to the console
            print(call.arg, end='', flush=True)
        elif call.syscall == SyscallType.SYS_WRITE_DOUBLE:
            # Write the character twice (WRITE_DOUBLE)
            print(call.arg * 2, end='', flush=True)

    print()  # Print newline at the end

