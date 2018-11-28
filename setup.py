

from setuptools import setup, find_packages

with open("README.md", "r") as f:
    readme = f.read()


setup(
    name='pyenv',
    version='0.1',
    description="PyENV",
    long_description=readme,
    license='Apache 2 Software License',
    url='https://github.com/DanDondoDan/pyenv',
    download_url='https://github.com/DanDondoDan/pyenv.git',
    packages=find_packages(),
    package_dir={'pyenv':
                 'pyenv'},
    include_package_data=True,
    zip_safe=False,
    keywords='pyenv',
    classifiers=[
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6+',
        'Operating System :: OS Independent'
    ],
)
