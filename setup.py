import setuptools; import re

setuptools.setup(
    name='hy_potato',
    description='Module for storing python dictionaries in a different format.',
    version='0.2',
    long_description='https://github.com/Hypurrnating/potato#readme',
    author='Hypurrnating',
    url='https://github.com/Hypurrnating/potato',
    license="MIT",
    packages=setuptools.find_packages(),
    classifiers=[   "Programming Language :: Python :: 3",
                    "License :: OSI Approved :: MIT License",
                    "Operating System :: Microsoft :: Windows :: Windows 7",
                    "Operating System :: Microsoft :: Windows :: Windows 8",
                    "Operating System :: Microsoft :: Windows :: Windows 8.1",
                    "Operating System :: Microsoft :: Windows :: Windows 10",
                    "Operating System :: Microsoft :: Windows :: Windows 11"],
    python_requires=">=3.2",
    install_requires=[],
    include_package_data=True,
)