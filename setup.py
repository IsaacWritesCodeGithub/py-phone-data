from setuptools import setup
from setuptools import find_packages
setup(
    name="py-phone-data",
    version="0.0.1",
    url="https://github.com/IsaacWritesCodeGithub/py-phone-data",
    author="IsaacWritesCode",
    author_email="isaacwritescode7@gmail.com",
    description="Simple phone info",
    packages=find_packages(),
    install_requires=["lxml==4.8.0", "Gooey==1.0.8.1", "pandas==1.4.2", "requests==2.27.1"],
    include_package_data=True,
    package_data={'': ['*.html']},
)