from setuptools import setup, find_packages

setup(
    name="edeediong-hello-user",
    version="0.0.1",
    author="Edeediong",
    author_email="edidiongmichael08@gmail.com",
    url="https://edeediong.me",
    description="A hello user package",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["click"],
    entry_points={
        "console_scripts": ["hello-world = hello_user.main:greet"]
    }
)