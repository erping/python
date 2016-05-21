#python multiprocessing

import os

print('Process %s starts..' % os.getpid())
pid = os.fork()
if pid == 0:
	print('i am child process %s and my parent is %s' %(os.getpid(),os.getppid()))
else:
	prinf('I %s just create child process %s' %(os.getpid(),pid))
