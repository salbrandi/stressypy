A package to stress a specific number of cpus for a certain length of time
==========================================================================

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
| Debian                 | ``sudo apt-get install stress stress-ng`` |
+------------------------+-------------------------------------------+
| body row 2             | ``pacman -S stress stress-ng``            |
+------------------------+-------------------------------------------+

