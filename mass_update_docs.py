#!/usr/bin/env python3


import os
import grab_bundle_markdown as GBM
import argparse
import time

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


distro_titles = {
    'Debian7' : 'Debian 7',
    'Debian8' : 'Debian 8',
    'Debian9' : 'Debian 9',
    'Debian10' : 'Debian 10',
    'Ubuntu18' : 'Ubuntu 18.04',
    'Ubuntu19' : 'Ubuntu 19.04',
    'CentOS7' : 'CentOS 7',
    'CentOS8' : 'CentOS 8',
    'Windows' : 'Windows'
}


class Distribution:

    def __init__(self, name):
        self.name = name
        self.bundle_paths = []
        self.md_txt = ''

    def create_markdown(self):
        for path in self.bundle_paths:
            self.md_txt = self.md_txt + GBM.grab_bundle_markdown(path) + '\n\n'
            print('Markdown generated for bundle {}'.format(path))



def check_already_contains(markdown_str, file):
    target_md_file = os.path.join('docs', file)
    target_fp = open(target_md_file, 'r')
    bundle = markdown_str.splitlines()[0]
    for line in target_fp.readlines():
        if line.strip() == bundle.strip():
            return True

    return False


def create_distro_objects(top_path):

    distros = {}
    for name in md_files.keys():
        distros[name] = Distribution(name)

    for dir in os.listdir(top_path):
        version_dir = os.path.join(top_path, dir)
        if os.path.isdir(version_dir):
            for distro in os.listdir(version_dir):
                if distro in md_files.keys():
                    distros[distro].bundle_paths.append(os.path.join(version_dir, distro))

    for distro in distros.keys():
        print('Detected {} bundle(s) for distribution {}.'.format(len(distros[distro].bundle_paths), distro_titles[distro]))
        time.sleep(0.2)


    print()
    return distros


def get_distro_intro_message(distro):

    out = '# {} Bundles\n\n'.format(distro_titles[distro])
    out = out + 'Below is a list of all bundles available for {}, including included modules and versions, locations, and build configurations and settings.\n\n'.format(distro_titles[distro])
    return out



def main():
    parser = argparse.ArgumentParser(description='A helper script for generating markdown docs from bundle README files.')
    parser.add_argument('filepath', help='Absolute filepath to the production folder. Must have format top -> version -> distribution')
    args = vars(parser.parse_args())
    if not os.path.exists(args['filepath']):
        print('ERROR - path does not exist')
    elif os.path.isfile(args['filepath']):
        print('ERROR - path must be a directory')
    else:
        print('Starting Bundle Index docs auto update...\n')

        print('Collecting and sorting distribution bundles...\n')

        distros = create_distro_objects(os.path.abspath(args['filepath']))

        for distro in distros.keys():
            print('Processing bundles for distro {}'.format(distro_titles[distro]))
            os.remove(os.path.join('docs', md_files[distro]))
            target_md_file = os.path.join('docs', md_files[distro])
            target_fp = open(target_md_file, 'w')
            target_fp.write(get_distro_intro_message(distro))
            distros[distro].create_markdown()
            target_fp.write(distros[distro].md_txt)
            target_fp.close()
            print('Wrote markdown file {} for distribution {}'.format(md_files[distro], distro))
            print()
            time.sleep(0.2)


if __name__ == '__main__':
    main()
