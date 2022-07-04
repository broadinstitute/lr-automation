from io import open

from setuptools import find_packages, setup

# following src dir layout according to
# https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure
version = "0.0.9"
setup(
    name="manifold",
    version=version,
    description="Identify variation from SNVs to SVs with a graph genome framework",
    author="Kiran V Garimella",
    author_email="kiran@broadinstitute.org",
    license="Apache-2.0",
    long_description=open("README.rst").read(),
    install_requires="""
    numpy
    pysam
    dataclasses
    """.split(
        "\n"
    ),
    tests_require=["coverage", "pytest"],
    python_requires=">=3.6",
    packages=find_packages("src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    entry_points={"console_scripts": ["manifold=manifold.__main__:main_entry"]},
    include_package_data=True,
)
