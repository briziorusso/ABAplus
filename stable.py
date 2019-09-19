#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


__author__ = "Kristijonas Cyras"
__email__ = "k.cyras@imperial.ac.uk"
__copyright__ = "Copyright (c) 2019 Kristijonas Cyras"


import os
import sys
from pathlib import Path

from aspartix_interface import *
from abap_parser import *
from auxil import *

EXAMPLE_DIR = Path.cwd() / 'argopt'


def load_file(filename: str = None):
    file = None
    if filename:
        file = Path(filename)
        if not file.exists():
            print('File "{}" not found.\n'.format(file))
            exit()
    else:
        while not file:
            filename = input('\nChoose a file in {}.\nType "none" to quit.\n\n'.format(EXAMPLE_DIR))
            if filename.lower() == 'none':
                exit()
            elif Path(EXAMPLE_DIR / filename).exists():
                file = Path(EXAMPLE_DIR / filename)
            else:
                print('File "{}" not found. Try again.\n'.format(filename))

    return file


def compute_stable(file: str):
    abapf_pl = generate_aba_plus_framework_from_file(file)
    framework = abapf_pl[0]
    contr_map = dict((v, k) for k, v in abapf_pl[1].items())

    try:
        WCP_ok = True
        framework.check_or_auto_WCP()  # auto_WCP = True
    except WCPViolationException as exception:
        print(exception)
        user_input = input('Enforce WCP? [y/n]\n')
        if user_input.lower() == 'y':
            print('WCP will be enforced.')
            framework.check_or_auto_WCP(auto_WCP = True)
        else:
            print('WCP will not be enforced.')
            WCP_ok = False
    finally:
        if not WCP_ok:
            print('Terminated by the user.')
            exit()

        abapf = ABA_Plus(assumptions = framework.assumptions,
                         rules = framework.rules,
                         preferences = framework.preferences)
        lp_file = Path(str(file).replace(' ', '_')).with_suffix('.lp')
        aaf = ASPARTIX_Interface(abapf)
        aaf.generate_input_file_for_clingo(lp_file)
        stable_exts = aaf.calculate_stable_arguments_extensions(lp_file)
        stable_exts_with_concs = arguments_extensions_to_str_list(stable_exts, contr_map)

        for item in stable_exts_with_concs:
            print('{}. '.format(stable_exts_with_concs.index(item) + 1) + item)
        os.remove(lp_file)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        compute_stable(load_file())
    else:
        compute_stable(load_file(Path(EXAMPLE_DIR / sys.argv[1])))
