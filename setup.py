from setuptools import setup, find_packages

setup(
    name='IGTools',
    version='0.1.0',
    author='Meizug',
    description='Library Python untuk automasi Instagram seperti login, posting, dan scraping.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ivan732/InstaTools',
    packages=find_packages(),
    install_requires=[
        'requests>=2.31.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: WWW/HTTP',
    ],
    python_requires='>=3.7',
)

