# -*- coding: utf-8 -*-
"""
samsung_remote_control

Samsung remote control using the Multiple Display Control Protocol via TCP/IP

:author:
    Pieter Smets (mail@pietersmets.be)

:copyright:
    Pieter Smets (mail@pietersmets.be)

:license:
    This code is distributed under the terms of the
    GNU General Public License, Version 3
    (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""

from .remote_control import remote_control

# Make only a selection available to __all__ to not clutter the namespace
# Maybe also to discourage the use of `from samsung_mdc import *`.
__all__ = ['remote_control']

# Version
try:
    # - Released versions just tags:       1.10.0
    # - GitHub commits add .dev#+hash:     1.10.1.dev3+g973038c
    # - Uncom. changes add timestamp: 1.10.1.dev3+g973038c.d20191022
    from samsung_remote_control.version import version as __version__
except ImportError:
    # If it was not installed, then we don't know the version.
    # We could throw a warning here, but this case *should* be
    # rare. empymod should be installed properly!
    from datetime import datetime
    __version__ = 'unknown-'+datetime.today().strftime('%Y%m%d')
