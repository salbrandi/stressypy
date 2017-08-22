
# ------------------- #
# Third Party Imports #
# ------------------- #
import time
import random
import subprocess
import multiprocessing as mp
from types import *

stress_string = 'stress -c {0} -t {1}s'

def get_time_used(func, *args, **kwargs):
    start_time = time.perf_counter()
    func( *args, **kwargs )
    return time.perf_counter()-start_time


class JobBlock:
    """
    A convenient class to hold all the relevant information about the dummy cpu loads for rqpop
    """


    def __init__(self, n_cpu, t_run, q_name='default', name='job'):
        self.n_cpu = n_cpu
        self.time = t_run
        self.func = None
        self.func_args = []
        self.func_kwargs = {}
        self.job = None
        if self.n_cpu > mp.cpu_count():
            self.n_cpu = mp.cpu_count()

    def set_job(self, func, *args, **kwargs):
        if type(func) == FunctionType:
            self.func = func
            self.func_args = args
            self.func_kwargs = kwargs
            self.job = '{0}({1}, {2})'.format(func, args, kwargs)
        else:
            raise ValueError('for set_job(func, arg, kwargs): func is not a function')

    def run(self):
        if self.job is not None:
            self.wallclock_time = get_time_used(self.func, *self.func_args, **self.func_kwargs)

    def area(self):
        return self.n_cpu*self.time


def create_job(cpu_width, time_height):
    """
    :param cpu_width: number of cpus
    :param time_height: amount of time
    :return: the instantiated JobBlock object
    """

    shell_command = stress_string.format(cpu_width, time_height)
    job = JobBlock(cpu_width, time_height)
    job.set_job(subprocess.call, shell_command, shell=True)
    return job
