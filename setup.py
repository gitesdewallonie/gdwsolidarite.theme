from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='gdwsolidarite.theme',
      version=version,
      description="Theme package for Action Solidarite one page site",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='Affinitic',
      author='Affinitic',
      author_email='info@affinitic.be',
      url='https://github.com/gitesdewallonie/gdwsolidarite.theme',
      license='gpl',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages=['gdwsolidarite'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.api',
          'plone.app.themingplugins',
          # -*- Extra requirements: -*-
      ])
