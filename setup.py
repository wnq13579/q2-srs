# ----------------------------------------------------------------------------
# Copyright (c) 2016-2018, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from setuptools import setup, find_packages


setup(
    name="srs",
    version="2020.8.0",
    packages=find_packages(),
    author="Vitor Heidrich, Lukas Beule, Devon O'rourke and Petr Karlovsky",
    description="Scaling with ranked subsampling (SRS) for the normalization of ecological count data",
    scripts=['q2_srs/assets/SRS.R',
            'q2_srs/assets/SRScurve.R'],
    license='BSD-3-Clause',
    url="https://qiime2.org",
    entry_points={
        'qiime2.plugins':
        ['q2-srs=q2_srs.plugin_setup:plugin']
    },
    zip_safe=False,
    package_data={
        'q2_srs': ['citations.bib']
    }
)
