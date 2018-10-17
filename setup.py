import re

from setuptools import find_packages, setup


with open('sanic_fcm/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='sanic-fcm',
    version=version,
    url='https://github.com/asmodius/sanic-fcm',
    license='MIT',
    author='Asmodius',
    author_email='asmodius.a@gmail.com',
    description='Python async client for Firebase Cloud Messaging (FCM) for Sanic',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='sanic fcm',
    platforms=['any'],
    download_url='https://github.com/asmodius/sanic-fcm/archive/master.zip',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
    packages=find_packages(exclude=['tests', 'example']),
    tests_require=['pytest'],
)
