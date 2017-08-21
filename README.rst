A package to stress one or more cores
=====================================

``stressypy`` uses the unix package ``stress`` to stress a certain number of cpus for a certain amount
of time, as specified by the user. It creates ``JobBlock`` objects which contain pertinent information for using these
stress loads to test queueing algorithms.

JobBlock Attributes:
++++++++++++++++++++

class attributes
----------------
* total_blocks: the number of blocks created
* waiting_blocks: the number of blocks waiting to be queued - in box
* queued_blocks: the number of blocks waiting to be executed - in queue

instance attributes
-------------------
* n_cpu: number of cpus being stressed
* t_run: the time it will take to run the job
* delta_t_run: the time the processor will take to run the job; overhead time
* state: the state of the block
* func: the function the block is storing
* func_args: the arguments for the function the block is storing
* area: the 'area' as width in cpu vs height in time
* queue: the queue the block will be sent to
* job: a combination of the func and arg to return the complete job that the block should execute


Installation
++++++++++++

``stressypy`` can be installed with ``pip install stressypy``

or cloned manually and setup with ``python setup.py install``

``stressypy`` is dependent on the ``stress`` unix package. Make sure you have it installed.

+------------------------+-------------------------------------------+
| Unix Distro            | Command                                   |
+========================+===========================================+
| Debian                 | `sudo apt-get install stress`          |
+------------------------+-------------------------------------------+
| Arch Linux             | `pacman -S stress`                     |
+------------------------+-------------------------------------------+


Directions
++++++++++

``stressypy`` runs using the command ``stressy stress`` with the number of cpus and time passed as arguments

* ``stressy stress 1 1`` stresses 1 core for 1 second
* ``stressy stress 7 3`` stresses 7 cores for 3 second
