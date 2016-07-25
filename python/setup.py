# -*- coding: utf-8 -*-


from setuptools import setup


long_desc = """Programming Exercise for Python is a collection of sample code
for demostration of concept and usage of Python Language."""

setup(name='pysperm',
      version='0.0.1',
      packages=['pysperm',],
      entry_points={'console_scripts': [
          'pysperm = pysperm.__main__:main',
      ]},
      author='Jim Lin',
      author_email='jimlintw922@gmail.com',
      url='https://github.com/jinsenglin/pysperm/',
      description='Programming Exercise for Python',
      long_description=long_desc,
      license="Apache 2.0",
      classifiers=[
          'Programming Language :: Python :: 2.7',
      ],
      install_requires=[]
      )
