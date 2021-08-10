from setuptools import setup, find_packages
setup(
    name = 'switch',
    version = '1.0.0',
    author = 'Luka Mamukashvili',
    author_email = 'ultraluka0@gmail.com',
    description = ('Switch-Case class for Python'),
    license = 'GPL-3.0',
    url = 'https://github.com/UltraStudioLTD/Switch',
    scripts = [],
    py_modules = ['switch'],
    packages = find_packages(),
    install_requires = ['typing;python_version<"3.5"'],
    download_url = 'https://github.com/UltraStudioLTD/Switch/tarball/master'
)
