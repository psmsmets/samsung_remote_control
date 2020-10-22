import PySimpleGUI as sg
from samsung_mdc import MultipleDisplayControl
try:
    from .version import version as __version__
except ImportError:
    from datetime import datetime
    __version__ = 'unknown-'+datetime.today().strftime('%Y%m%d')


__all__ = ['remote_control']


def control_all_screens(command, value):
    """
    """
    print('-'*len(command))
    print(command)
    print('-'*len(command))
    for (host, port) in _screen_addresses:
        try:
            with MultipleDisplayControl(host, port) as screen:
                print(f'{screen} set {command} to "{value}"')
                eval(f'screen.set_{command}(value)')
        except Exception as e:
            print('Error:', e)


def set_locale(lang: str):
    """
    """
    global _text_on, _text_off, _text_source, _text_mute, _text_lock
    global _title_power, _title_settings, _title_lock

    if lang == 'nl':
        _text_on = 'aan'
        _text_off = 'uit'
        _text_source = 'source'
        _text_mute = 'mute'
        _text_lock = 'slot'
        _title_power = 'alle schermen'
        _title_settings = 'standaard instellingen'
        _title_lock = 'veiligheidsslot'

    elif lang == 'fr':
        _text_on = 'activé'
        _text_off = 'désactivé'
        _text_source = 'source'
        _text_mute = 'mute'
        _text_lock = 'verrouillage'
        _title_power = 'tous les écrans'
        _title_settings = 'paramètres standard'
        _title_lock = 'verrouillage de sécurité'

    else:
        _text_on = 'on'
        _text_off = 'off'
        _text_source = 'source'
        _text_mute = 'mute'
        _text_lock = 'lock'
        _title_power = 'all screens'
        _title_settings = 'default settings'
        _title_lock = 'safety lock'


def set_addresses(addresses: list):
    """
    """
    global _screen_addresses

    _screen_addresses = []

    for address in addresses:
        if ':' in address:
            host, port = address.split(':')
            port = int(port) if port.isnumeric() else None
        else:
            host, port = address, None
        _screen_addresses.append((host, port))


def remote_control(addresses: list, locale: str = None):
    """Samsung remote control gui using the Multiple Display Control Protocol
    via TCP/IP

    Parameters:
    -----------
    """
    # set screen addresses
    set_addresses(addresses)

    # set language
    set_locale(locale)

    # construct window
    sg.theme('Black')

    btn_lg = dict(focus=False, border_width=0, size=(24, 3))
    btn_sm = dict(focus=False, border_width=0, size=(10, 2))
    frame = dict(font='Any 14')

    power = [[sg.Button(_text_on.upper(), key='power_on', **btn_lg)],
             [sg.Button(_text_off.upper(), key='power_off', **btn_lg)]]

    settings = [[sg.Button(f'{_text_source}\nHDMI2',
                           key='source_hdmi2', **btn_sm),
                 sg.Button(f'{_text_mute}\n{_text_on}',
                           key='mute_on', **btn_sm)]]

    lock = [[sg.Button(f'{_text_lock}\n{_text_on}',
                       key='lock_on', **btn_sm),
             sg.Button(f'{_text_lock}\n{_text_off}',
                       key='lock_off', **btn_sm)]]

    layout = [[sg.Frame(_title_power.capitalize(), power, **frame)],
              [sg.Frame(_title_settings.capitalize(), settings, **frame)],
              [sg.Frame(_title_lock.capitalize(), lock, **frame)],
              [sg.T(f'v{__version__} - STEPS4it.be',
                    justification='right', font='Any 9')]]

    window = sg.Window('Samsung remote control', layout,
                       font=("Helvetica", 14), grab_anywhere=False)

    # track buttons
    while True:
        key, values = window.read()
        if key == sg.WIN_CLOSED or key == 'Cancel':
            break
        elif key == 'power_on':
            control_all_screens('power', True)
        elif key == 'power_off':
            control_all_screens('power', False)
        elif key == 'source_hdmi2':
            control_all_screens('source', 'HDMI2')
        elif key == 'mute_on':
            control_all_screens('mute', True)
        elif key == 'lock_on':
            control_all_screens('safety_lock', True)
        elif key == 'lock_off':
            control_all_screens('safety_lock', False)

    window.close()
