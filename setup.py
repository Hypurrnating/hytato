import setuptools; import re

with open('README.md', 'r') as file:
    readme = file.read()
    file.close()

setuptools.setup(
    name='hytato',
    description='Module for storing python dictionaries in a different format.',
    long_description=readme,
    author='Hypurrnating',
    url='https://github.com/Hypurrnating/potato',
    license="MIT",
    packages=setuptools.find_packages(),
    classifiers=[   "Programming Language :: Python :: 3",
                    "License :: OSI Approved :: MIT License",
                    "Operating System :: Microsoft :: Windows",
                    "Operating System :: Unix"],
    python_requires=">=3.2",
    install_requires=[],
    include_package_data=True,
)