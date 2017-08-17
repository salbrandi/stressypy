# -*- coding: utf-8 -*-
# ------------------- #
# Third Party Imports #
# ------------------- #
import click

# ------------------- #
#    Local Imports    #
# ------------------- #
from .cpustresser import create_job

@click.group()
def stressy():
    pass

@click.command()
@click.argument('num_cpus')
@click.argument('time')
@click.option('-n', default=1)
def create_stress_jobs(num_cpus, time):
    create_job(num_cpus, time)

stressy.add_command(create_stress_jobs, name='stress')