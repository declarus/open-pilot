from distutils.core import Extension, setup  # pylint: disable=import-error,no-name-in-module

from Cython.Build import cythonize
import sys
sys.path.append('/home/motorai/Desktop/Workspace/av/av/openpilot-devel')

from common.cython_hacks import BuildExtWithoutPlatformSuffix

setup(name='Simple Kalman Implementation',
      cmdclass={'build_ext': BuildExtWithoutPlatformSuffix},
      ext_modules=cythonize(Extension("simple_kalman_impl", ["simple_kalman_impl.pyx"])))
