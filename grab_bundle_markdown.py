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
    isa_checkout_command = 'git checkout master'
    in_mod_list = False
    for line in lines:
        if not in_mod_list:
            if line.startswith('# Bundle - '):
                build_info_table['Bundle Name'] = '`{}`'.format(line.split('-',1)[1].strip()[:-1].strip())
            elif line.startswith('[folder name]'):
                in_mod_list = True
            elif line.split(':',1)[0] in build_info_list:
                build_info_table[line.split(':',1)[0].strip()] = line.split(':',1)[1].strip()
            elif line.strip().startswith('git checkout'):
                isa_checkout_command = line.strip()

        else:
            if line.startswith('#'):
                in_mod_list = False
            elif '-' in line:
                bundle_modules_table[line.split('-',1)[0].strip()] = line.split('-',1)[1].strip()

    fp.close()
    return build_info_table, bundle_modules_table, isa_checkout_command


def parse_legacy_readme_file(filepath):
    build_info_table = {}
    build_modules_table = {}
    fp = open(filepath, 'r')
    lines = fp.readlines()
    fp.close()

    bundle_path = os.path.dirname(filepath)
    build_info_table['Location'] = '`{}`'.format(bundle_path)
    if os.path.exists(os.path.join(bundle_path, 'build-config')):
        build_info_table['Build Config Path'] = '`{}`'.format(os.path.join(bundle_path, 'build-config'))

    for line in lines:
        if line.startswith('NSLS2'):
            temp = line.strip().split('_')
            build_info_table['Build Date'] = temp[-1]
            build_info_table['OS Class'] = temp[4] + '_' + temp[5]
        elif len(line) > 0:
            stripped = line.strip()
            mod_ver = line.split(':')
            if len(mod_ver) == 2:
                build_modules_table[mod_ver[0].strip()] = mod_ver[1].strip()

    return build_info_table, build_modules_table


def grab_bundle_markdown(bundle_path):
    markdown_str = ''
    for file in os.listdir(bundle_path):
        if file.startswith('README'):
            try:
                build_info_table, bundle_modules_table, checkout_command = parse_readme_file(os.path.join(bundle_path, file))
                markdown_str = markdown_str + '### ADCore {}\n\n'.format(bundle_modules_table['ADCore'])
                markdown_str = markdown_str + 'Bundle Information:\n\nVariable|Value\n------|--------\n'
                for key in build_info_table.keys():
                    markdown_str = markdown_str + '{}|{}\n'.format(key, build_info_table[key])
                markdown_str = markdown_str + '\nTo regenerate sources used to build the bundle, use the following commands:\n'
                markdown_str = markdown_str + '```bash\ngit clone https://github.com/epicsNSLS2-deploy/installSynApps && cd installSynApps\n{}\npython3 -u installCLI.py -c {} -p\n'.format(checkout_command, build_info_table['Build Config Path'][1:-1])
                markdown_str = markdown_str + '```\nMake sure to have Python {} installed, and be running on a {} machine\n'.format(build_info_table['Python 3 Version'], build_info_table['OS Class'])
                markdown_str = markdown_str + '\nModules and Versions Included:\n\nModule Name|Module Version\n-------|----------\n'

                for module in bundle_modules_table.keys():
                    markdown_str = markdown_str + '{}|{}\n'.format(module, bundle_modules_table[module])
                print('Parsed README file for {}'.format(bundle_path))
            except KeyError:
                try:
                    build_info_table, bundle_modules_table = parse_legacy_readme_file(os.path.join(bundle_path, file))
                    markdown_str = markdown_str + '### ADCore {}\n\n'.format(bundle_modules_table['ADCore'])
                    markdown_str = markdown_str + 'Bundle Information:\n\nVariable|Value\n------|--------\n'
                    for key in build_info_table.keys():
                        markdown_str = markdown_str + '{}|{}\n'.format(key, build_info_table[key])

                    markdown_str = markdown_str + '\nModules and Versions Included:\n\nModule Name|Module Version\n-------|----------\n'

                    for module in bundle_modules_table.keys():
                        markdown_str = markdown_str + '{}|{}\n'.format(module, bundle_modules_table[module])
                    print('Detected and parsed legacy README file in {}'.format(bundle_path))
                except:
                    print('Could not successfully parse README file in bundle {}'.format(bundle_path))
#                    file_fp = open(os.path.join(bundle_path, file), 'r')
#                    markdown_str = '### Unknown Bundle Version\n\n' + file_fp.read()
#                    file_fp.close()
            break

    return markdown_str



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A helper script for generating markdown docs from bundle README files.')
    parser.add_argument('filepath', help='Absolute filepath to the target bundle')
    args = vars(parser.parse_args())
    if not os.path.exists(args['filepath']):
        print('ERROR - path does not exist')
    elif os.path.isfile(args['filepath']):
        print('ERROR - path must be a directory')
    else:
        print(grab_bundle_markdown(args['filepath']))
