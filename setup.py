from setuptools import setup

from randomText import __author__, __email__, __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='random-text',
      version=__version__,
      description='A Python client library Random Data Api',
      long_description=long_description,
      long_description_content_type='text/markdown; charset=UTF-8',
      author=__author__,
      author_email=__email__,
      packages=['randomText', 'randomText.src'],
      url='https://github.com/uricod/random-text',
      include_package_data=True,
      zip_safe=False,
      license='BSD',
      python_requires='>=3.6',
      install_requires=[
          'requests',
          'pandas==1.4.2'
     ],
      classifiers=[
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "Operating System :: OS Independent",
      ])