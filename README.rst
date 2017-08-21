A package to stress one or more cores
=====================================

``stressypy`` uses the unix package ``stress`` and/or ``stress-ng`` to to stress a certain number of cpus for a certain amount
of time.


Installation
++++++++++++

``stressypy`` can be installed with ``pip install stressypy``

or cloned manually and setup with ``python setup.py install``

``stressypy`` is dependent on the ``stress`` and ``stress-ng`` packages. Make sure you have both installed.

+------------------------+-------------------------------------------+
| Unix Distro            | Command                                   |
+========================+===========================================+
| Debian                 | `sudo apt-get install stress stress-ng`   |
+------------------------+-------------------------------------------+
| Arch Linux             | `pacman -S stress stress-ng`              |
+------------------------+-------------------------------------------+


Directions
++++++++++

``stressypy`` runs using the command ``stressy stress`` with the number of cpus and tieme passed as arguments

``stressy stress 1 1`` stresses one core for 1 second
``stressy stress 7 3`` stresses 7 cores for 3 second
