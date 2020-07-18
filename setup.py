# -*- coding: utf-8 -*-
###################################
# tellurium setup script
#
# develop install via
# pip install -e .
###################################

from setuptools import setup
import os

try:
    with open(os.path.join(os.path.dirname(__file__), 'VERSION.txt'), 'r') as f:
        version = f.read().rstrip()
except IOError:
    # fallback location
    with open(os.path.join(os.path.dirname(__file__), 'tellurium/VERSION.txt'), 'r') as f:
        version = f.read().rstrip()

setup(name='tellurium',
      version=version,
      author='J. Kyle Medley, Kiri Choi, Matthias König, Lucian Smith, Herbert M. Sauro',
      description='Tellurium: An biological modeling environment for Python',
      long_description=open('README.md').read(),
      long_description_content_type="text/markdown",
      url='http://tellurium.analogmachine.org/',
      packages=[
          'tellurium',
          'tellurium.analysis',
          'tellurium.notebooks',
          'tellurium.plotting',
          'tellurium.roadrunner',
          'tellurium.sedml',
          'tellurium.teconverters',
          'tellurium.teio',
          'tellurium.utils',
          #   'tellurium.optimization',
          'tellurium.visualization',
          #   'tellurium.tests',
      ],
      package_data={
          "tellurium": ["*.txt"],
          "tellurium.sedml": ["templates/*.template"],
      },
      install_requires=[i for i in open("requirements.txt").readlines() if i != ''],
      platforms=["Windows", "Linux", "Unix", "Mac OS-X"],

      )
