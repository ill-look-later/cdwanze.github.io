#!/usr/bin/env python3
#-*-coding:utf-8-*-

from setuptools import setup, find_packages

setup(
  name='timer',
  version='0.1',
  description='the timer program',
  long_description=open('README.md').read(),
  url='https://github.com/a358003542/timer',
  author='wanze',
  author_email='a358003542@gmail.com',
  maintainer = 'wanze',
  maintainer_email = 'a358003542@gmail.com',
  license='GPL 2',
  platforms = 'Linux',
  keywords =['timer','python'],
  classifiers = ['Development Status :: 2 - Pre-Alpha',
  'Environment :: Console',
  'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
  'Operating System :: POSIX :: Linux',
  'Programming Language :: Python :: 3.4',],
  packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
  include_package_data=True,
#  install_requires=['click'],
#  setup_requires,
#  extras_require={'test': ['pytest'],},
  entry_points = {
  'gui_scripts':['timer=timer.main:gui'],
  }
)


#if __name__ == '__main__':
