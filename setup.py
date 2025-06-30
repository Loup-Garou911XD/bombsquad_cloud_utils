
from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize

sourcefiles = ["libbacloud/libbacloud.pyx"]

extensions = cythonize(Extension(
             name="libbacloud.libbacloud",
             sources = sourcefiles
      ))

kwargs = {
       "name": "libbacloud",
       "packages": find_packages(),
       "ext_modules": extensions
      }

setup(**kwargs)