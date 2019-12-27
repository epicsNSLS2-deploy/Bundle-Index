#!/usr/bin/env python3

import os
import argparse

def parse_readme_file(filepath):
    build_info_table = {}
    bundle_modules_table = {}
    fp = open(filepath, 'r')
    bundle_path = os.path.dirname(filepath)
    build_info_table['Location'] = '`{}`'.format(bundle_path)
    if os.path.exists(os.path.join(bundle_path, 'build-config')):
        build_info_table['Build Config Path'] = '`{}`'.format(os.path.join(bundle_path, 'build-config'))

    build_info_list = ['installSynApps Version', 'Python 3 Version', 'OS Class', 'Build Date']
    lines = fp.readlines()
    in_mod_list = False
    for line in lines:
        if not in_mod_list:
            if line.startswith('# Bundle - '):
                build_info_table['Bundle Name'] = '`{}`'.format(line.split('-',1)[1].strip()[:-1].strip())
            elif line.startswith('[folder name]'):
                in_mod_list = True
            elif line.split(':',1)[0] in build_info_list:
                build_info_table[line.split(':',1)[0].strip()] = line.split(':',1)[1].strip()

        else:
            if line.startswith('#'):
                in_mod_list = False
            elif '-' in line:
                bundle_modules_table[line.split('-',1)[0].strip()] = line.split('-',1)[1].strip()

    return build_info_table, bundle_modules_table



parser = argparse.ArgumentParser(description='A helper script for generating markdown docs from bundle README files.')
parser.add_argument('filepath', help='Absolute filepath to the target bundle')
args = vars(parser.parse_args())
if not os.path.exists(args['filepath']):
    print('ERROR - path does not exist')
elif os.path.isfile(args['filepath']):
    print('ERROR - path must be a directory')
else:
    for file in os.listdir(args['filepath']):
        if file.startswith('README'):
            build_info_table, bundle_modules_table = parse_readme_file(os.path.join(args['filepath'], file))
            print('### ADCore {}\n'.format(bundle_modules_table['ADCore']))
            print('Bundle Information:\n\nVariable|Value\n------|--------')
            for key in build_info_table.keys():
                print('{}|{}'.format(key, build_info_table[key]))
            print('\nModules and Versions Included:\n\nModule Name|Module Version\n-------|----------')

            for module in bundle_modules_table.keys():
                print('{}|{}'.format(module, bundle_modules_table[module]))
