#!/usr/bin/env python

import sys

if 'install' in sys.argv:

    from distutils.spawn import find_executable

    if find_executable('virtualenv'):

        import subprocess

        virtualenv = subprocess.Popen(['virtualenv', 'python_modules'], stdout=subprocess.PIPE)

        if virtualenv.stdout.readlines():
            pip = subprocess.Popen(['python_modules/bin/pip', 'install', '-r', 'requirements.txt'], stdout=subprocess.PIPE)
            sys.stdout.write(virtualenv.stdout.readlines())
            sys.exit(1)
        else:
            sys.stderr.write('An error occurred.\n')
            sys.exit(0)

    else:
        sys.stderr.write('VirtualENV was not found on this system.\n')
        sys.exit(0)
