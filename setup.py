from setuptools import setup, Extension

module = Extension('sparseModule', sources=['sparseModule.c', 'sparseSort.c'])

setup(
    name='sparseModule',
    version='1.0',
    ext_modules=[module],
)