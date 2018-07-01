import setuptools

with open('readme.md') as fh:
    long_description = fh.read()

setuptools.setup(
    name='wuphf',
    version='0.0.2',
    author='hvgab',
    description='collection of clients to send messages with',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/hvgab/wuphf',
    packages='wuphf')
