import argparse
from samsung_remote_control import remote_control, __version__


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
        help=('Set locale (default: en). Allowed values are: '
              ', '.join(locales))
    )

    parser.add_argument(
        '-v', '--version', action='version', version=__version__,
        help='Print the version number and exit'
    )
    args = parser.parse_args()

    remote_control(args.hosts, args.locale)


if __name__ == "__main__":
    main()
