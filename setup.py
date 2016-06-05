from setuptools import setup

def readme():
    with open('README') as f:
        return f.read()
setup(
    name='unrpyc',
    version='0.1',
    description='Tool to decompile Ren\'Py compiled .rpyc script files.',
    long_description=readme(),
    url='https://github.com/CensoredUsername/unrpyc',
    packages=['unrpyc','decompiler'],
    entry_points={
        'console_scripts': ['unrpyc=unrpyc:main'],
    },
    zip_safe=False,
)
