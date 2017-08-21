# -*- coding: utf-8 -*-
# ------------------- #
# Third Party Imports #
# ------------------- #
import click
import sys

# ------------------- #
#    Local Imports    #
# ------------------- #
from stressypy.cpustresser import create_job

@click.group()
def stressy():
    pass

@click.command()
@click.argument('num_cpus')
@click.argument('time')
@click.option('-n', default=1)
def create_stress_jobs(num_cpus, time, n):
    job = create_job(int(num_cpus), int(time))
    job.run()

stressy.add_command(create_stress_jobs, name='stress')

if __name__ == '__main__':
    create_job(int(sys.argv[1]), int(sys.argv[2]))
