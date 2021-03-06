#!/usr/bin/env python
# coding=utf-8

from setuptools import setup
from linote import __version__

setup(name='linote',
      version=__version__,
      description='A command line evernote utility for Linux.',
      long_description=open('README.md').read(),
      author='solos',
      author_email='solos@solos.so',
      py_modules=['linote'],
      scripts=['linote.py', 'local.py', 'encoding.py', 'logger.py'],
      license='MIT',
      classifiers=[
          'Development Status :: 1 - Alpha',
          'Intended Audience :: End Users/Desktop',
          'License :: OSI Approved :: MIT License',
          'Environment :: Console',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Utilities',
      ],
      install_requires=['markdown', 'path.py', 'kaptan'],
      tests_require=['pyshould==0.5.7'],
      test_suite="nose.collector",
      url='https://github.com/solos/linote')
