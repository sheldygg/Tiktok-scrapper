import setuptools

setuptools.setup(
    name="tiktok-scrapper",
    version="0.1",
    author="sheldy",
    description="Tool for parse tiktok data",
    url="https://github.com/sheldygg/tiktok-scrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
    install_requires=[
        'aiohttp'
    ],
)
