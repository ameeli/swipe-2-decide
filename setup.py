from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="swipe-2-decide",
    version="0.0.1",
    author="Amee Li",
    author_email="ameejli@gmail.com",
    description="Swipe2Decide restaurant recommendation web service",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ameeli/swipe-2-decide",
    packages=find_packages(),
    install_requires=[
        'djangorestframework ~= 3.11.1',
        'psycopg2 ~= 2.8.5'

    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
)
