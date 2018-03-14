from distutils.core import setup
from distutils.extension import Extension

def install_and_import(package, version):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import subprocess
        subprocess.call([sys.executable, '-m', 'pip', 'install', '{0}=={1}'.format(pkg, version)])
    finally:
        globals()[package] = importlib.import_module(package)


install_and_import('cython', 0.24)
from Cython.Build import cythonize
import numpy as np

# To compile and install locally run "python setup.py build_ext --inplace"
# To install library to Python site-packages run "python setup.py build_ext install"

ext_modules = [
    Extension(
        'pycocotools._mask',
        sources=['./common/maskApi.c', './PythonAPI/pycocotools/_mask.pyx'],
        include_dirs = [np.get_include(), './common'],
        extra_compile_args=['-Wno-cpp', '-Wno-unused-function', '-std=c99'],
    )
]

setup(name='pycocotools',
      install_requires=install_requires,
      packages=['pycocotools'],
      package_dir = {'pycocotools': './PythonAPI/pycocotools'},
      version='2.0',
      ext_modules=
          cythonize(ext_modules)
      )
