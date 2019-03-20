from setuptools import setup, find_packages

setup(
    name='pathing',
    python_requires='>=3.7.2',
    install_requires=['pytest-cov==2.6.1',
                      'pylint==2.3.1',
                      'pytest==4.3.0'],
    packages=find_packages('src'),
    package_dir={'': 'src'}
)
