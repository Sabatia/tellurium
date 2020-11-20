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
          #'tellurium.optimization',
          'tellurium.visualization',
          #'tellurium.tests',
          #'tellurium.tests.testdata',
      ],
      package_data={
          "tellurium": ["*.txt"],
          "tellurium.sedml": ["templates/*.template"],
      },
      install_requires=[
          # general
          'numpy==1.19.3',  # 0.13.1
          'scipy>=1.5.1',  # 0.19.1
          'matplotlib>=2.0.2',
          'pandas>=0.20.2',
          # SBW-derived
          'libroadrunner>=2.0.0',
          'phrasedml>=1.0.9',
          'antimony>=2.12.0',
          #'rrplugins>=1.1.8',
          'sbml2matlab>=0.9.1',
          # standards
          'python-libsbml>=5.18.0',
          'python-libnuml>=1.0.0',
          'python-libsedml>=0.4.3',
          'python-libcombine>=0.2.2',
          # misc
          'appdirs>=1.4.3',
          'jinja2>=2.9.6',
          'plotly>=2.0.12',
          'requests',
          # Jupyter / IPython
          'jupyter-client>=5.1.0',
          'jupyter-core>=4.3.0',
          'ipython',
          'ipykernel>=4.6.1',
          # testing
          'pytest',
          ]
      )
