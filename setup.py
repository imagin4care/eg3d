from __future__ import annotations
from version import VERSION
from setuptools import setup
from setuptools.command.build_py import build_py as BuildPy

class build_py(BuildPy):
    def run(self):
        self.include_package_data = True
        BuildPy.run(self)
setup(
    name='eg3d',
    version=VERSION,
    zip_safe=False,
    include_package_data=True,
    cmdclass={},
)