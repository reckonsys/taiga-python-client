from setuptools import setup, find_packages

__VERSION__ = '0.1'

setup(
    name='taiga_client',
    version=__VERSION__,
    description="A Python wrapper for Taiga's API",
    long_description='Taiga Python Client',
    url='https://github.com/reckonsys/taiga-python-client',
    author='dhilipsiva',
    author_email='dhilipsiva@pm.me',
    maintainer='Reckonsys',
    maintainer_email='info@reckonsys.com',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: SQL',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Typing :: Typed',
    ],
    keywords='taiga python client reckonsys jira issues tickets',
    packages=find_packages(),
    install_requires=['requests'],
)
