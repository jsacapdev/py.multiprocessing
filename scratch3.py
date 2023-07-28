#!/usr/bin/env python
import os
import multiprocessing

def child_process():
    try:
        print(f"Hi! I'm a child process {os.getpid()}.")
        raise Exception("Oh no! :(")
    except Exception:
        print("Uh, I think it's fine now...")

if __name__ == "__main__":
    print(f"Hi! I'm process {os.getpid()}")

    # Here we create a new instance of the Process class and assign our
    # `child_process` function to be executed. Note the difference now that
    # we are using the `args` parameter now, this means that we can pass
    # down parameters to the function being executed as a child process.
    process = multiprocessing.Process(target=child_process)

    # We then start the process
    process.start()

    # And finally, we join the process. This will make our script to hang and
    # wait until the child process is done.
    process.join()

    print("AFTER CHILD EXECUTION! RIGHT?!")