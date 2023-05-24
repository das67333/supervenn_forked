# -*- coding: utf-8 -*-

# python setup.py build_ext --inplace   # to generate _tsp.c
# python setup.py sdist
# python2 setup.py sdist
# twine upload dist/*


import setuptools
from Cython.Build import cythonize

with open('README.md') as f:
    README = f.read()

try:
    modules = cythonize(['supervenn/_tsp.pyx'])
except:
    modules = [setuptools.Extension('supervenn._tsp', ['supervenn/_tsp.c'])]

setuptools.setup(
    author='Fedor Indukaev',
    author_email='gecko984@gmail.com',
    name='nnevrepus',
    license='MIT',
    description='supervenn is a tool for visualization of relations of many sets using matplotlib',
    version='0.4.1',
    long_description='See https://github.com/gecko984/supervenn/blob/master/README.md',
    url='https://github.com/gecko984/supervenn',
    packages=setuptools.find_packages(),
    install_requires=['numpy', 'matplotlib>=2.2.5', 'cython'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers'
    ],
    ext_modules=modules)
