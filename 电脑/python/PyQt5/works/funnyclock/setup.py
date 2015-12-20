from setuptools import setup ,find_packages
import os.path

setup(
  name='funnyclock',
  version='0.01',
  description='the software short description',
  author='wanze',
  author_email='a358003542@gmail.com',
  maintainer = 'wanze',
  maintainer_email = 'a358003542@gmail.com',
  license='GPL 2',
  platforms = 'Linux',
  keywords =['funnyclock','python'],
  classifiers = ['Development Status :: 2 - Pre-Alpha',
  'Environment :: Console',
  'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
  'Operating System :: POSIX :: Linux',
  'Programming Language :: Python :: 3.4',],
  packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
  include_package_data=True,
#  package_data = {"funnyclock":['funnyclock.tar.gz'],},
#  install_requires=['click'],
#  setup_requires,
#  extras_require={'test': ['pytest'],},
  entry_points = {
  'console_scripts' :[ 'funnyclock=funnyclock.funnyclock:main',],
#  'gui_scripts':['xfunnyclock=funnyclock.main:gui'],
  }
)



