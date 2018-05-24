from distutils.core import setup
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='mimi',
    version='1.2a-beta',
    packages=['mimi'],
    # py_modules=['mimi','mode','output','preprocess','generator'],  # 將模組的metadata關連到setup函式
    author='exeex',
    author_email='xray0h@gmail.com',
    url='....',
    description='beta',
)

here = os.path.abspath(os.path.dirname(__file__))

def get_about():
    about = {}

    path = os.path.join(here, 'mimi', '__about__.py')
    with open(path, 'rt') as aboutfile:
        exec(aboutfile.read(), about)

    return about

about = get_about()

setup(
    name='mimi',
    version=about['__version__'],
    description='MIDI Objects for Python',
    # long_description=open('README.rst', 'rt').read(),
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    license=about['__license__'],
    # package_data={'soundfont': ['soundfont/*']},
    package_dir={'mimi': 'mimi'},
    packages=['mimi'],
    include_package_data=True,
    install_requires=['mido>=1.2.8','numpy>=1.12.0'],
    extras_require={
        'dev': ['check-manifest>=0.35',
                'flake8>=3.4.1',
                'pytest>=3.2.2',
                'sphinx>=1.6.3',
                'tox>=2.8.2'
                ],
        'ports': ['python-rtmidi>=1.1.0']
    },
    zip_safe=False,
)