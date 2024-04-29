#!/usr/bin/env python3

from setuptools import setup

requirements = [
    'khal',
]

setup(
    name='khal-gruvbox',
    description='A khal theme plugn for the gruvbox color scheme',
    author='khal contributors',
    author_email='khal@lostpackets.de',
    url='http://lostpackets.de/khal/',
    license='Expat/MIT',
    entry_points={
        "khal.color_theme": [
            'gruvbox = khal_gruvbox.gruvbox:gruvbox'
        ]
    },
)
