from setuptools import setup, find_packages

VERSION = "1.0.0"

DEPENDENCIES = []

# The text of the README file
with open('README.md') as f:
    README = f.read()

# This call to setup() does all the work
setup(
    name="random-password",
    version=VERSION,
    description="Randomly generate passwords.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/PavelNajman/random_password",
    author="Pavel Najman",
    author_email="najman.pavel@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=DEPENDENCIES,
    entry_points={
        "console_scripts": [
            "random_password=random_password.__main__:main"
        ]
    }
)
