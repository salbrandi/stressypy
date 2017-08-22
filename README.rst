A package to stress one or more cores
=====================================

``stressypy`` uses the unix package ``stress`` to stress a certain number of cpus for a certain amount
of time, as specified by the user. It creates ``JobBlock`` objects which contain pertinent information for using these
stress loads to test queueing algorithms.

JobBlock Attributes:
++++++++++++++++++++

The JobBlock class is used to store any function and its cpu width and time height.

instance attributes
-------------------
* n_cpu: number of cpus being stressed
* t_run: the time it will take to run the job
* func: the function the block is storing
* func_args: the arguments for the function the block is storing
* job: a combination of the func and arg to return the complete job that the block should execute

+------------------------+-----------------------------------------------------------------------------------------------------+
| attribute type         | description                                                                                         |
+========================+=====================================================================================================+
| input                  | n_cpu: number of cpus being stressed                                                                |
+------------------------+-----------------------------------------------------------------------------------------------------+
| input                  | t_run: the time it will take to run the job                                                         |
+------------------------+-----------------------------------------------------------------------------------------------------+
| set with set_job()     | func: the function the block is storing                                                             |
+------------------------+-----------------------------------------------------------------------------------------------------+
| set with set_job()     | func_args: the arguments for the function the block is storing                                      |
+------------------------+-----------------------------------------------------------------------------------------------------+
| calculated             |  job: a combination of the func and arg to return the complete job that the block should execute    |
+------------------------+-----------------------------------------------------------------------------------------------------+





Installation
++++++++++++

``stressypy`` can be installed with ``pip install stressypy``

or cloned manually and setup with ``python setup.py install``

``stressypy`` is dependent on the ``stress`` unix package. Make sure you have it installed.

+------------------------+-------------------------------------------+
| Unix Distro            | Command                                   |
+========================+===========================================+
| Debian                 | `sudo apt-get install stress`             |
+------------------------+-------------------------------------------+
| Arch Linux             | `pacman -S stress`                        |
+------------------------+-------------------------------------------+


Directions
++++++++++

``stressypy`` runs using the command ``stressy stress`` with the number of cpus and time passed as arguments

* ``stressy stress 1 1`` stresses 1 core for 1 second
* ``stressy stress 7 3`` stresses 7 cores for 3 second
