import os
import re

from setuptools import find_packages, setup


REGEXP = re.compile(r"^__version__\W*=\W*'([\d.abrc]+)'")


def read_version():

    init_py = os.path.join(os.path.dirname(__file__), 'info', '__init__.py')

    with open(init_py) as f:
        for line in f:
            match = REGEXP.match(line)
            if match is not None:
                return match.group(1)
        else:
            msg = f'Cannot find version in ${init_py}'
            raise RuntimeError(msg)


install_requires = [
    'aiohttp==3.3.2',
    'aiohttp_cors==0.7.0',
    'alembic==0.9.10',
    'aiopg==0.14.0',
    'SQLAlchemy==1.2.9',
    'psycopg2-binary==2.7.5',
    'alembic==0.9.10',
    'gunicorn==19.9.0',
    'graphene==2.1.2',
    'argparse==1.4.0',
    'aiohttp-graphql==1.0.0',
    'trafaret-config==2.0.2',
    'trafaret==1.2.0',
]


setup(
    name='info',
    version=read_version(),
    description='info about myself',
    platforms=['POSIX'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    zip_safe=False,
)
