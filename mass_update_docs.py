#!/usr/bin/env python3


import os
import grab_bundle_markdown as GBM
import argparse

md_files = {
    'Debian7' : 'deb7.md',
    'Debian8' : 'deb8.md',
    'Debian9' : 'deb9.md',
    'Debian10' : 'deb10.md',
    'Ubuntu18' : 'ub1804.md',
    'Ubuntu19' : 'ub1904.md',
    'CentOS7' : 'centos7.md',
    'CentOS8' : 'centos8.md',
    'Windows' : 'windows.md'
}


def check_already_contains(markdown_str, file):
    target_md_file = os.path.join('docs', file)
    target_fp = open(target_md_file, 'r')
    bundle = markdown_str.splitlines()[0]
    for line in target_fp.readlines():
        if line.strip() == bundle.strip():
            return True

    return False



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A helper script for generating markdown docs from bundle README files.')
    parser.add_argument('filepath', help='Absolute filepath to the target bundle')
    args = vars(parser.parse_args())
    if not os.path.exists(args['filepath']):
        print('ERROR - path does not exist')
    elif os.path.isfile(args['filepath']):
        print('ERROR - path must be a directory')
    else:
        for name in os.listdir(args['filepath']):
            bundle_path = os.path.join(args['filepath'],name)
            if os.path.isdir(bundle_path):
                try:
                    markdown_str = GBM.grab_bundle_markdown(bundle_path)
                    if not check_already_contains(markdown_str, md_files[name]):
                        target_md_file = os.path.join('docs', md_files[name])
                        target_fp = open(target_md_file, 'a')
                        target_fp.write('\n\n')
                        target_fp.write(markdown_str)
                        target_fp.write('\n')
                        target_fp.close()
                        print('Markdown generated for bundle {}, written to {}'.format(bundle_path, target_md_file))
                    else:
                        print('Documentation for bundle {} was already in the docs.'.format(bundle_path))
                except KeyError:
                    print('ERROR, could not get markdown from bundle {}'.format(bundle_path))

