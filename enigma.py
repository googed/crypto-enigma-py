#!/usr/bin/env python
# encoding: utf8

""" 
Description

.. note::
    Any additional note.
"""

from __future__ import (absolute_import, print_function, division, unicode_literals)
import argparse
from enigma import __version__
from enigma.machine import *

_DESC = "A simple Enigma machine simulator with rich display."

_EPILOG = """\
Examples:

    $ %(prog)s show "C-II-VIII-I EMO UX.MO.KZ.AY.EF.PL 13.04.11" -l Q -f internal
    $ %(prog)s show "C-II-VIII-I EMO UX.MO.KZ.AY.EF.PL 13.04.11" -lQ -finternal
    $ %(prog)s show "B-I-III-I EMO UX.MO.KZ.AY.EF.PL 13.04.11"
    $ %(prog)s show "$(%(prog)s step 'C-II-VIII-I AAA UX.MO 13.04.11')" -f config


"""

_DESC_DISPLAY = """\
Show an Enigma machine configuration in the specified format, optionally
indicating the encoding of a specified character.
"""

_DESC_ENCODE = """\
Show the encoding of a message.
"""

_DESC_RUN = """\
Show the operation of the Enigma machine as it encodes a message.
"""

_DESC_STEP = """\
Show the state of the Enigma machine after a specified number of steps.
"""

# TBD - Formats arent all the same: encoding has two more, the encoding and the chunked encoding <<<
# TBD - Combine encode and run, or keep seperate? <<<

# _EPILOG_DISPLAY = """\
# The the number of times '-d' is supplied will determine the level
# of detail displayed:
#     1, which simply shows the specification
#        of the configuration;
#     2, the default, which will show a single line; and
#     3, which will show a detailed schematic of each
#        processing stage
# """

_EPILOG_FORMAT_DISPLAY = """\
The selection for '--format' will determine what is shown; options include:
    - 'internal', which will show a detailed schematic of each
      processing stage;
    - 'single', which will show a single line;
    - 'windows', just the letters visible at the windows; and
    - 'config', the default, which simply shows the specification
      of the configuration
The program is forgiving about forgotten format values and will accept a range
of reasonable substitutes (e.g., 'detailed' or 'schematic' for 'internal').
"""
_EPILOG_DISPLAY = _EPILOG_FORMAT_DISPLAY
_EPILOG_ENCODE = "TBD"


# ASK - What's idiomatic?
def fmt_arg(arg):
    return arg.upper()
    # return '<' + arg.lower() + '>'


# TBD - Not needed if help can works when in parent
_HELP_ARGS = ['--help', '-h', '-?']
_HELP_KWARGS = {'action': 'help', 'help': 'show this help message and exit'}
_CONFIG_ARGS = ['config']
_CONFIG_KWARGS = {'metavar': fmt_arg('config'), 'action': 'store'}
_DISPLAY_KWARGS = {'title': 'display arguments', 'description': 'optional display arguments'}
_FORMAT_ARGS = ['--format', '-f']
_FORMAT_KWARGS = {'metavar': fmt_arg('format'), 'action': 'store', 'nargs': '?', 'default': 'single', 'const': 'single'}

if __name__ == '__main__':

    parent_parser = argparse.ArgumentParser(add_help=False)
    # Almost works, but puts config in the wrong position and won't show command help unless theres a config!
    # parent_parser.add_argument('config', metavar=fmt_arg('config'),
    #                             action='store',
    #                             help='the machine configuration to show')
    parent_parser.add_argument('--verbose', '-v',
                               action='store_true',
                               help='display additional information (may have no effect)')
    # parent_parser.add_argument('--version', '-V',
    #                            action='version', version='%(prog)s {0}'.format(__version__),
    #                            help='display package version number and exit')
    # parent_parser.add_argument(*_HELP_ARGS, **_HELP_KWARGS)

    # config_parser = argparse.ArgumentParser(add_help=False)
    # # Almost works, but puts config in the wrong position and won't show command help unless theres a config!
    # config_parser.add_argument('config', metavar=fmt_arg('config'),
    #                             action='store',
    #                             help='the machine configuration to %(dest)s')

    parser = argparse.ArgumentParser(description=_DESC, parents=[parent_parser],
                                     epilog=_EPILOG,
                                     # usage = 'enigma.py [<options>] COMMAND CONFIG',
                                     add_help=False,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(*_HELP_ARGS, **_HELP_KWARGS)

    commands = parser.add_subparsers(help='', dest='command',
                                     # title='required arguments',
                                     # description='description, some commands to choose from',
                                     metavar=fmt_arg('command')
                                     )
    # parser.add_argument('config', metavar=fmt_arg('config'),
    #                          action='store',
    #                          help='the machine configuration to %(dest)s')

    # Display machine state
    show_parser = commands.add_parser('show', parents=[parent_parser],
                                      description=_DESC_DISPLAY,
                                      epilog=_EPILOG_DISPLAY,
                                      help='display an Enigma machine configuration',
                                      add_help=False,
                                      formatter_class=argparse.RawDescriptionHelpFormatter)
    _CONFIG_KWARGS['help'] = 'the machine configuration to show'
    show_parser.add_argument(*_CONFIG_ARGS, **_CONFIG_KWARGS)
    show_display_group = show_parser.add_argument_group(**_DISPLAY_KWARGS)
    _FORMAT_KWARGS['help'] = 'the format to use to show the configuration; see below'
    show_display_group.add_argument(*_FORMAT_ARGS, **_FORMAT_KWARGS)
    show_display_group.add_argument('--letter', '-l', metavar=fmt_arg('letter'),
                                    action='store', nargs='?', default='', const='',
                                    help='an optional input letter to highlight as it is processed by the '
                                         'configuration, coerced to valid Enigma characters (uppercase letters); '
                                         'defaults to nothing; strings will be truncated at the first letter')
    show_parser.add_argument(*_HELP_ARGS, **_HELP_KWARGS)
    # group = parser.add_mutually_exclusive_group()

    # Show machine operation
    run_parser = commands.add_parser('run', parents=[parent_parser],
                                      description=_DESC_ENCODE,
                                      epilog=_EPILOG_ENCODE,
                                      help='display enigma machine operation',
                                      add_help=False,
                                      formatter_class=argparse.RawDescriptionHelpFormatter)
    _CONFIG_KWARGS['help'] = 'the machine setup at the start of operation'
    run_parser.add_argument(*_CONFIG_ARGS, **_CONFIG_KWARGS)
    run_parser.add_argument('message', metavar=fmt_arg('message'), action='store',
                             help='a message to encode')
    run_display_group = run_parser.add_argument_group(**_DISPLAY_KWARGS)
    _FORMAT_KWARGS['help'] = 'the format to use to show each configuration; see below'
    run_display_group.add_argument(*_FORMAT_ARGS, **_FORMAT_KWARGS)
    run_parser.add_argument(*_HELP_ARGS, **_HELP_KWARGS)

    # Encode a message
    encode_parser = commands.add_parser('encode', parents=[parent_parser],
                                        description=_DESC_ENCODE,
                                        epilog=_EPILOG_ENCODE,
                                        help='encode a message',
                                        add_help=False,
                                        formatter_class=argparse.RawDescriptionHelpFormatter)
    _CONFIG_KWARGS['help'] = 'the machine setup at the start of encoding'
    encode_parser.add_argument(*_CONFIG_ARGS, **_CONFIG_KWARGS)
    encode_parser.add_argument('message', metavar=fmt_arg('message'), action='store',
                               help='a message to encode')
    encode_display_group = encode_parser.add_argument_group(**_DISPLAY_KWARGS)
    _FORMAT_KWARGS['help'] = 'the format to use to show each configuration; see below'
    encode_display_group.add_argument(*_FORMAT_ARGS, action='store_true')
    encode_parser.add_argument(*_HELP_ARGS, **_HELP_KWARGS)

    # Show result of stepping the machine
    step_parser = commands.add_parser('step', help='step the configuration once', parents=[parent_parser],
                                      add_help=False)
    _CONFIG_KWARGS['help'] = 'the machine configuration to begin stepping from'
    step_parser.add_argument(*_CONFIG_ARGS, **_CONFIG_KWARGS)
    steps_display_group = step_parser.add_argument_group(title='stepping arguments',
                                                         description='optional stepping arguments')
    steps_display_group.add_argument('--steps', '-s', metavar=fmt_arg('steps'), action='store',
                                     nargs='?', default=1, const=1, type=int,
                                     help='number of steps to preform; default is 1')
    steps_display_group.add_argument('--initial', '-i', action='store_true',
                                     help='show the initial starting step as well')
    steps_display_group.add_argument('--overwrite', '-o', action='store_true',
                                     help='overwrite each step')
    steps_display_group.add_argument('--all', '-a', action='store_true', help='show all steps')
    _FORMAT_KWARGS['help'] = 'the format to use to show the stepped configuration(s); see below'
    steps_display_group.add_argument(*_FORMAT_ARGS, **_FORMAT_KWARGS)
    step_parser.add_argument(*_HELP_ARGS, **_HELP_KWARGS)

    # Just show the package version
    _HELP_VERSION = 'Show the package version and exit'
    version_parser = commands.add_parser('version', help=_HELP_VERSION.lower(), add_help=False,
                                         description=_HELP_VERSION + '.')
    version_parser.add_argument(*_HELP_ARGS, **_HELP_KWARGS)

    # try:
    #     args = parser.parse_args()
    # # ASK - How to catch just wrong argument errors <<<
    # # ASK - How to print help for current subcommand, if there is one <<<
    # except:# argparse.ArgumentError as e:
    #     parser.print_help()
    #     exit(0)
    # else:

    args = parser.parse_args()

    _FMTS_INTERNAL = ['internal', 'detailed', 'schematic']
    _FMTS_SINGLE = ['single', 'encoding', 'summary']
    _FMTS_WINDOWS = ['windows', 'winds']
    _FMTS_CONFIG = ['config', 'configuration', 'spec', 'specification']
    _FMTS_DEBUG = ['debug']

    try:
        # TBD - Add encoding note to config and windows (e.g with P > K) <<<
        # TBD - Add components format that lists the components and their attributes <<<
        if args.command == 'version':
            print('{0}'.format(__version__))
        else:
            cfg = EnigmaConfig.config_enigma_from_string(args.config)
            fmt = args.format
            if fmt in _FMTS_INTERNAL + _FMTS_SINGLE + _FMTS_WINDOWS + _FMTS_CONFIG + _FMTS_DEBUG or fmt in [True, False]:
                if args.command == 'show':
                    let = args.letter
                    if fmt in _FMTS_INTERNAL:
                        print(cfg.config_string_internal(let))
                    elif fmt in _FMTS_SINGLE:
                        print(cfg.config_string(let))
                    # TBD - Another version that prints spec on individual lines; or list or elements?
                    elif fmt in _FMTS_WINDOWS:
                        print(cfg.windows())
                    elif fmt in _FMTS_CONFIG:
                        print(cfg)
                    # Hidden option for debugging
                    elif fmt in _FMTS_DEBUG:
                        print(cfg.__repr__())
                elif args.command == 'run':
                    msg = args.message
                    if fmt in _FMTS_INTERNAL:
                        cfg.print_operation_internal(msg)
                    elif fmt in _FMTS_SINGLE:
                        cfg.print_operation(msg)
                    # TBD - Another version that prints spec on individual lines; or list or elements?
                    elif fmt in _FMTS_WINDOWS:
                        print('TBD')
                    elif fmt in _FMTS_CONFIG:
                        print('TBD')
                    # Hidden option for debugging
                    elif fmt in _FMTS_DEBUG:
                        print('TBD')
                elif args.command == 'encode':
                    msg = args.message
                    if fmt:
                        cfg.print_encoding(msg)
                    else:
                        print(cfg.enigma_encoding(msg))
                # TBD - Formatting and all handling
                elif args.command == 'step':
                    steps = args.steps
                    all = args.all
                    if False:
                        print(cfg.step())
                    else:
                        # TBD - Move and focus imports <<<
                        import time
                        import sys
                        si = 0
                        for s in cfg.stepped_configs(steps):
                            if si != 0 or args.initial:
                                print(s, end=('\r' if si < steps and args.overwrite else None))
                                if args.overwrite:
                                    sys.stdout.flush() # Otherwise sleep will prevent printing
                                    time.sleep(0.5 if si < steps else 0)
                            si += 1


                # TBD - Should share same arguments and same stucture with show <<<
                elif args.command == 'step':
                    print(cfg.step())
            else:
                print('Bad argument - Unrecognized format, {0}'.format(fmt))
                exit(1)

    except EnigmaError as e:
        print(e.message)
        exit(1)




# print(parser.parse_args())
# ASK - Put optional args after required ones? <<<
# http://superuser.com/questions/461946/can-i-use-pipe-output-as-a-shell-script-argument
# ASK - How to test scripts in testing suite? <<<
# From http://bioportal.weizmann.ac.il/course/python/PyMOTW/PyMOTW/docs/argparse/index.html to start
# Defaults - http://stackoverflow.com/a/15301183/656912

# # ASK - No way to do -ddd as --detail=3? <<<
# show_display_group.add_argument('-d', '--detail', #metavar=fmt_arg('format'), #choices=('internal', 'single', 'config'),
#                             action='count', default=0,  #default=1,
#                             help='the level of detail to show; see below')
