import os
from setuptools import setup

def get_long_description(path):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), path)
    with open(path) as f:
        return f.read()

setup(
    name='python-kakaobot',
    version='0.0.1',
    url='https://github.com/hallazzang/kakaobot',
    license='MIT',
    author='Hanjun Kim',
    author_email='hallazzang@gmail.com',
    description='Super simple framework for Kakaotalk auto-reply bot based on '
                'aiohttp',
    long_description=get_long_description('README.rst'),
    packages=['kakaobot'],
    python_requires='>=3.5',
    zip_safe=False,
    platforms='any',
    install_requires=[
        'aiohttp>=2.3.6',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
