import os
from setuptools import setup
from io import open

__version__ = "0.0.1"


def package_files(directory:str):
    """
    Traverses target directory recursivery adding file paths to a list.
    Original solution found at:

        * https://stackoverflow.com/questions/27664504/\
            how-to-add-package-data-recursively-in-python-setup-py

    Parameters
    ----------
    directory: str
        Target directory to traverse.

    Returns
    -------
    paths: list
        List of file paths.

    """
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))

    return paths


setup(
    name = 'asteroid_sphinx_theme',
    version =__version__,
    author = 'Asteroid',
    author_email= 'asteroid@asteroid.com',
    url="https://github.com/pytorch/lightning_sphinx_theme",
    docs_url="https://github.com/pytorch/lightning_sphinx_theme",
    description='Asteroid: Sphinx Theme',
    py_modules = ['asteroid_sphinx_theme'],
    packages = ['asteroid_sphinx_theme'],
    include_package_data=True,
    zip_safe=False,
    package_data={'asteroid_sphinx_theme': [
        'theme.conf',
        '*.html',
        'theme_variables.jinja',
        *package_files('asteroid_sphinx_theme/static')
    ]},
    entry_points = {
        'sphinx.html_themes': [
            'asteroid_sphinx_theme = asteroid_sphinx_theme',
        ]
    },
    license= 'MIT License',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: Software Development :: Documentation"
    ],
    install_requires=[
       'sphinx'
    ]
)
