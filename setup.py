#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='sqlalchemy_ceodbc',
    version='0.1.0',
    description='SQLAlchemy dialect for ceODBC',
    author='Dirk Jonker',
    author_email='dirkjonker@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    packages=find_packages(),
    entry_points={
        'sqlalchemy.dialects':
            ['mssql.ceODBC = sqlalchemy_ceodbc.dialect:MSDialect_ceODBC']
    },
    license='MIT',
    install_requires=['sqlalchemy'],
)
