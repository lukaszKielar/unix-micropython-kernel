"""
Installation script
"""
import sys
import shlex
import subprocess
from setuptools import setup, find_packages, Command


class CleanCommand(Command):

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        subprocess.run('rm -vrf \
                       ./.cache ./**/.cache \
                       ./.eggs ./**/.eggs \
                       ./*.egg-info ./**/*.egg-info \
                       ./build ./**/build \
                       ./*.pyc ./**/*.pyc \
                       ./__pycache__ ./**/__pycache__ \
                       ./.pytest_cache ./**/.pytest_cache \
                       ./.mypy_cache ./**/.mypy_cache', shell=True)


class LintCommand(Command):

    user_options = [
        ('opts=', None, "Line of options to pass to the pylint runner"),
    ]

    def initialize_options(self):
        self.opts = ''

    def finalize_options(self):
        self.pylint_opts = shlex.split(self.opts)

    def run(self):
        from pylint.lint import Run
        Run(self.pylint_opts)


class MypyCommand(Command):

    user_options = [
        ('opts=', None, "Line of options to pass to the mypy runner"),
        ('packages=', None, "Packages that mypy should check")
    ]

    def initialize_options(self):
        self.python_version = ''
        self.mypy_path = ''
        self.follow_imports = ''
        self.warn_unused_ignores = ''
        self.opts = ''
        self.packages = ''

    def finalize_options(self):
        if len(self.packages) > 0:
            packages_list = ['--package ' + package for package in self.packages.split()]
            self.packages = " ".join(packages_list)
        self.mypy_opts = " ".join(shlex.split(self.opts) + shlex.split(self.packages))

    def run(self):
        subprocess.run('python setup.py clean', shell=True)
        cmd_to_run = 'python -m mypy ' + self.mypy_opts
        cmd = subprocess.run(cmd_to_run, shell=True)
        if cmd.returncode != 0:
            print("Mypy failed!")
            sys.exit(cmd.returncode)
        else:
            print("Mypy succeeded!")


setup(
    name='unix_micropython_kernel',
    version='0.0.1',
    description="Jupyter kernel for MicroPython's UNIX port",
    license='MIT',
    author='Łukasz Kielar',
    author_email='luk.kielar@gmail.com',
    url='https://github.com/lukaszKielar/unix_micropython_kernel',
    install_requires=[
        'ipykernel',
        'jupyterlab'
    ],
    setup_requires=[
        'mypy',
        'pylint',
        'pytest'
    ],
    tests_require=['pytest'],
    packages=find_packages(exclude=['tests']),
    cmdclass={
        'clean': CleanCommand,
        'lint': LintCommand,
        'mypy': MypyCommand,
    }
)
