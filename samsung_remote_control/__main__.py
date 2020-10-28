import argparse
from samsung_remote_control import remote_control, __version__
from samsung_mdc.mdc import _input_sources_set


def main():
    """
    """
    # get arguments
    parser = argparse.ArgumentParser(
        prog='samsung_remote_control',
        description=('Samsung remote control using the Multiple Display '
                     'Control Protocol via TCP/IP'),
    )

    parser.add_argument(
        'hosts', metavar='host[:port]', type=str, nargs='+',
        help=('Remote TV ipv4 addresses (default port: 1515)')
    )

    locales = ('en', 'nl', 'fr')
    parser.add_argument(
        '--locale', metavar='..', choices=locales, default='en',
        help=('Set locale (default: en). Allowed values are: ' +
              ', '.join(locales))
    )
    sources = _input_sources_set.values()
    parser.add_argument(
        '--source', metavar='..', choices=sources, default='HDMI2',
        help=('Set source (default: HDMI2). Allowed values are: ' +
              ', '.join(sources))
    )
    parser.add_argument(
        '--timeout', metavar='..', type=float, default=5.,
        help=('Set a timeout on blocking socket operations, in seconds '
              '(default: 5.0). '
              'Timeout > 0: raise timeout exception. '
              'Timeout == 0: non-blocking mode. '
              'Timeout < 0: blocking mode.')
    )

    parser.add_argument(
        '-v', '--version', action='version', version=__version__,
        help='Print the version number and exit'
    )
    args = parser.parse_args()

    remote_control(
        args.hosts,
        locale=args.locale,
        source=args.source,
        timeout=args.timeout if args.timeout >= 0. else None,
    )


if __name__ == "__main__":
    main()
