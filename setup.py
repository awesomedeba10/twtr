from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='twtr',
    version='0.1',
    description='Done under the AlmaBetter Assignment to process Twitter data and make this ready for modeling',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Debanjan Ganguly',
    author_email='officialdeba10@gmail.com',
    url='https://github.com/awesomedeba10/twtr',
    package_dir={"": "twtr"},
    packages=find_packages(where="twtr"),
    license='MIT',
)