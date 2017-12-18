A Python module and CLI tool that returns IP address ownership and location information based on MaxMind's GeoLite2
databases

::

    usage: geoip          [-h] [-d DATABASE_DIRECTORY] [-v]
                          ip_address [ip_address ...]

    positional arguments:
      ip_address            One or more IP addresses to look up

    optional arguments:
      -h, --help            show this help message and exit
      -d DATABASE_DIRECTORY, --database-directory DATABASE_DIRECTORY
                            Overrides the path to the directory containing MaxMind
                            databases
      -v, --version         show program's version number and exit

Prerequisites
-------------

In order to use ``simplegeoip2``, you must have the MaxMind GeoLite2 databases on your system. This simplest way to do
this is to use the ``geoipupdate`` tool from MaxMind.

https://github.com/maxmind/geoipupdate

Installation
------------

While this script should work under Python 2 and 3, using Python 3 for your OS is strongly recommended.

On Debian or Ubuntu systems, run:

::

    $ sudo apt-get install python3-pip


Python 3 installers for Windows and macOS can be found at https://www.python.org/downloads/

To install or upgrade to the latest stable release of checkdmarc on macOS or Linux, run

::

    $ sudo pip3 -U install simplegeoip2

Or, install the latest development release directly from GitHub:

::

    $ sudo pip3 -U install git+https://github.com/domainaware/simplegeoip2.git


Note to Windows users
^^^^^^^^^^^^^^^^^^^^^

On Windows, ``pip3`` is ``pip``, regardless if you installed Python 2 or 3. So on Windows, simply
substitute ``pip`` as an administrator in place of ``sudo pip3``, in the above commands.


Bug reports
-----------

Please report bugs on the GitHub issue tracker

https://github.com/domainaware/simplegeoip/issues