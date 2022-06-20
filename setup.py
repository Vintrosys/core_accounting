from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in core_accounting/__init__.py
from core_accounting import __version__ as version

setup(
	name="core_accounting",
	version=version,
	description="accounting",
	author="accounting",
	author_email="accounting@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
