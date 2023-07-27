from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in smbgym/__init__.py
from smbgym import __version__ as version

setup(
	name="smbgym",
	version=version,
	description="Gym managment platform",
	author="royalsmb",
	author_email="khanmomodou11@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
