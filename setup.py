from setuptools import setup

setup(
    name="Tasker",
    version="0.1",
    packages=["tasker"],
    entry_points={
        "console_scripts": [
            "tasker = tasker.__main__:main"
        ]
    }
)
