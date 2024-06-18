from setuptools import setup, find_packages

setup(
    name='ttl_cache',
    version='0.0.1',
    description='A function-level memory cache that supports Time To Live (TTL)',
    author='Yongho Hwang',
    author_email='jogakdal@gmail.com',
    url='https://github.com/jogakdal/python_ttl_cache',
    install_requires=['collections', 'inspect', 'expiringdict'],
    packages=find_packages(exclude=[]),
    keywords=['cache', 'memory cache', 'ttl cache', 'function cache', 'cache decorator'],
    python_requires='>=3.6',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
