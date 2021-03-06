from distutils.core import setup
from ops import __version__ as version

long_description = """
ops is a collection of Python modules and tools that makes building and
running system applications a little easier.

You can find the latest docs at http://opsdojo.github.com/ops/.
"""

setup(
    name='ops',
    version=version,
    description='Modules and tools for system applications',
    long_description=long_description.strip(),
    author='Silas Sewell',
    author_email='silas@sewell.org',
    license='MIT',
    url='https://github.com/silas/ops',
    packages=[
        'ops',
    ],
    classifiers=[
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: MIT License',
          'Operating System :: Unix',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Topic :: Software Development',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: System :: Systems Administration',
    ],
)
