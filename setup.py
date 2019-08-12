from setuptools import find_packages, setup

setup(
    name="tox101",
    version="0.0.1",
    description="Using tox.",
    author="Albrecht Johannes Richter",
    author_email="ajr@mail.de",
    license="0BSD",
    packages=find_packages("src"),
    package_dir={
        "": "src",
    },
    tests_require=["pytest"],
)
