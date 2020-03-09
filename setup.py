"""
importhook
==========
"""
from setuptools import find_packages, setup


def get_long_description():
    with open('README.md') as f:
        rv = f.read()
    return rv


setup(
    name='importhook',
    version='1.0.8',
    url='https://github.com/brettlangdon/importhook',
    license='MIT',
    author='Brett Langdon',
    author_email='me@brett.is',
    description='Execute code when certain modules are imported',
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[],
    python_requires=">3.3",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python',
    ]
)
