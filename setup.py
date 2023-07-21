import setuptools; import re

setuptools.setup(
    name='hy_potato',
    description='Module for storing python dictionaries in a different format.',
    version='0.2',
    long_description=open('.\\README.md', 'r').read(),
    author='Hypurrnating',
    url='https://github.com/Hypurrnating/potato',
    license="MIT",
    packages=setuptools.find_packages(),
    classifiers=[   "Programming Language :: Python :: 3",
                    "License :: OSI Approved :: MIT License",
                    "Operating System :: Windows"],
    python_requires=">=3.2",
    install_requires=[],
    include_package_data=True,
)