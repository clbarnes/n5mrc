from pathlib import Path

from setuptools import find_packages, setup

with open(Path(__file__).resolve().parent / "README.md") as f:
    readme = f.read()

setup(
    name="n5mrc",
    url="https://github.com/clbarnes/n5mrc",
    author="Chris L. Barnes",
    description="Script to export N5 subvolumes to MRC files",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_packages(include=["n5mrc"]),
    install_requires=["mrcfile", "numpy", "zarr", "dask"],
    python_requires=">=3.7, <4.0",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    entry_points={"console_scripts": ["n5mrc=n5mrc.cli:_main"]},
)
