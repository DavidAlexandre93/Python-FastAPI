from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(['cumprimenta.pyx', 'computa.pyx'])
)

"""
Para compilar usar o comando abaixo:
python setup.py build_ext --inplace
"""