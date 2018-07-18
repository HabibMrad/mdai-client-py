from setuptools import setup
from setuptools import find_packages
from mdai import __version__

long_description = """
MD.ai Python client library.
Currently experimental -- API may change significantly in future releases.
"""

install_requires = [
    "arrow",
    "matplotlib",
    "numpy",
    "pandas",
    "pillow",
    "pydicom>=1.1.0",
    "requests",
    "retrying",
    "tqdm",
]

extras_require = {
    "test": ["pytest"],
    "keras": ["keras>=2.2.0"],
    "tensorflow": ["tensorflow>=1.9.0"],
}

setup(
    name="mdai",
    version=__version__,
    description="MD.ai Python client library",
    long_description=long_description,
    author="MD.ai",
    author_email="github@md.ai",
    url="https://github.com/mdai/mdai-client-py",
    download_url="https://github.com/mdai/mdai-client-py/tarball/{}".format(__version__),
    license="Apache-2.0",
    install_requires=install_requires,
    extras_require=extras_require,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=find_packages(),
)
