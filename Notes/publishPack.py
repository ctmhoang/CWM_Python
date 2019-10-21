import setuptools

setuptools.setup(
    name="nameOfPackage",
    version="1.0",
    long_description="Some descrip",
    packages=setuptools.find_packages(exclude=["someDirName "])
)

# name this file to setup.py
# on console
# run
# python3 setup.py sdist #sourcedir bdist_wheel #buildDir
# twine upload dist/*
