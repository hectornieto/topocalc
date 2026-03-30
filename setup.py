from setuptools import setup, Extension
import numpy

ext_modules = [
    Extension(
        "topocalc.core_c.topo_core",
        sources=[
            "topocalc/core_c/topo_core.c",
            "topocalc/core_c/hor1d.c",
        ],
        include_dirs=[numpy.get_include()],
    )
]

setup(ext_modules=ext_modules)
