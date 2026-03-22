import sys
from setuptools import setup
from Cython.Build import cythonize

# Ensure the script is run with a filename argument
if len(sys.argv) < 2:
    print("Usage: python setup.py build_ext --inplace <filename>")
    sys.exit(1)

# Extract filename from arguments
filename = sys.argv.pop()  # Take the last argument as the filename
print(f'filename: {filename} from {sys.argv}')

setup(
    ext_modules=cythonize(filename,
                          compiler_directives={"language_level": "3"}),
)
