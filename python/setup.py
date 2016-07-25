# -*- coding: utf-8 -*-


from setuptools import setup


long_desc = """Programming Exercise for Python is a collection of sample code
for demostration of concept and usage of Python Language."""

setup(name='PROJECT-ID',
      version='0.0.1',
      packages=['PROJECT-ID', 'PROJECT-ID.lib'],
      entry_points={'console_scripts': [
          'PROJECT-ID = PROJECT-ID.__main__:main',
      ]},
      author='Jim Lin',
      author_email='jimlintw922@gmail.com',
      url='https://github.com/jinsenglin/PROJECT-ID/',
      description='Programming Exercise for Python',
      long_description=long_desc,
      license="Apache 2.0",
      classifiers=[
          'Programming Language :: Python :: PROJECT-PYTHON-VERSION'
      ],
      install_requires=[]
      )
