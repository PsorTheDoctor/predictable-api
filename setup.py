from setuptools import setup

setup(
    name='predictable-api',
    version='1.0',
    long_description=__doc__,
    packages=['predictable-api'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)
