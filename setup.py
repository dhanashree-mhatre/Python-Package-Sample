from setuptools import setup, Extension
from Cython.Build import cythonize
import os

# Function to find all Python files in the package directory
def find_pyx_files(package_dir):
    py_files = []
    for root, _, files in os.walk(package_dir):
        for file in files:
            if file.endswith(".py") and file != "__init__.py":  # Exclude __init__.py
                py_file = os.path.join(root, file)
                pyx_file = py_file.replace(".py", ".pyx")
                os.rename(py_file, pyx_file)  # Rename .py to .pyx
                py_files.append(pyx_file)
    return py_files


ext_modules = [
    Extension(
        *os.path.splitext(py_file.replace("/", ".")),  # Module name
        sources=[py_file]
    )
    for py_file in find_pyx_files("your_package")
]

setup(
    name="rejoai",
    version="0.2.0",
    packages=["your_package"],
    ext_modules=cythonize(ext_modules),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
