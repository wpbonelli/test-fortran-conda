import setuptools

class NoNumpy(Exception):
    pass

try:
    from numpy.distutils.core import Extension
    from numpy.distutils.core import setup
except ImportError:
    raise NoNumpy('Numpy Needs to be installed '
                  'for extensions to be compiled.')

with open("README.md", "r") as fh:
    long_description = fh.read()

simple = Extension('min_python_pkg.simple', sources=['min_python_pkg/simple_routine.f90'])

setup(
    name='min_python_pkg',
    version='v0.1',
    packages=setuptools.find_packages(),
    include_package_data=True,
    url='',
    license='MIT',
    author='Aaron David Schneider',
    author_email='aarondavid.schneider@nbi.ku.dk',
    description='just simple',
    long_description=long_description,
    long_description_content_type="text/markdown",
    ext_modules=[simple],
    scripts=['bin/do_simple'],
)
