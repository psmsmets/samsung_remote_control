**********************
samsung_remote_control
**********************

Samsung remote control using the Multiple Display Control Protocol via TCP/IP

Features
========

Provides a simple gui to control all TV's at once.
 
Usage
=====

In the terminal execute

.. code-block:: console

    >>> samsung_remote_control --help

to show this help message and exit

.. code-block:: console

    usage: samsung_remote_control [-h] [--locale ..] [-v]
                                  host[:port] [host[:port] ...]

    Samsung remote control using the Multiple Display Control Protocol via TCP/IP

    positional arguments:
      host[:port]    Remote TV ipv4 addresses (default port: 1515)

    optional arguments:
      -h, --help     show this help message and exit
      --locale ..    Control command name. Allowed values are: en, nl, fr
      -v, --version  Print the version number and exit

Control remote TV's

.. code-block:: console

    >>> samsung_remote_control --locale=nl 192.168.2.201 192.168.2.202:1515


Windows executable
==================

Create a ``.bat`` file using ``powershell`` and ``Miniconda3``

.. code-block:: ruby

    @echo off

    set root=C:\ProgramData\Miniconda3

    set hosts=192.168.2.201 192.168.2.202 192.168.2.203^
        192.168.2.204 192.168.2.205 192.168.2.206^
        192.168.2.208 192.168.2.209 192.168.2.210^
        192.168.2.211 192.168.2.212

    call %root%\Scripts\activate.bat
    powershell -window hidden "python samsung_remote_control --locale=nl %hosts%"


License information
===================

Licensed under the GNU GPLv3 License. See the ``LICENSE``- and ``NOTICE``-files
or the documentation for more information.
