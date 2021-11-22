import os

from setuptools import setup

path_to_py42_wheel = os.path.join(
    os.getcwd(), "wheels", "py42-1.15.1-py2.py3-none-any.whl"
)
path_to_stubs = os.path.join(os.getcwd(), "stubs#egg=phantom")

setup(
    name="ph_code42_connector",
    version="1.0.0",
    description="Code42 for Phantom",
    py_modules=["code42_connector", "code42_util", "code42_on_poll_connector",],
    install_requires=[
        "pytest==4.4.0",
        "pytest-mock==1.10.3",
        "requests>=2.24.0",
        "python-dateutil>=2.8.1",
        f"py42 @ file://localhost/{path_to_py42_wheel}",
    ],
    extras_require={
        "dev": [
            f"stubs @ file://localhost/{path_to_stubs}",
            "flake8==3.8.3",
            "termcolor==1.1.0",
            "pre-commit",
        ]
    },
)
