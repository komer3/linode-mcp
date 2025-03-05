#!/bin/bash
# Script to build and publish the package to PyPI

# Ensure we're using the virtual environment
if [ ! -d ".venv" ]; then
    echo "Virtual environment not found. Please run install.sh first."
    exit 1
fi

# Activate the virtual environment
if [[ "$OSTYPE" == "darwin"* ]] || [[ "$OSTYPE" == "linux-gnu"* ]]; then
    source .venv/bin/activate
elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    source .venv/Scripts/activate
else
    echo "Unsupported OS type: $OSTYPE"
    echo "Please activate the virtual environment manually."
    exit 1
fi

# Install build tools
echo "Installing build and publishing tools..."
pip install build twine

# Clean previous builds
echo "Cleaning previous builds..."
rm -rf dist/ build/ *.egg-info/

# Build the package
echo "Building the package..."
python -m build

# Check the package
echo "Running Twine check..."
twine check dist/*

echo ""
echo "Package built successfully!"
echo ""
echo "To publish to Test PyPI (recommended for testing):"
echo "  twine upload --repository-url https://test.pypi.org/legacy/ dist/*"
echo ""
echo "To publish to PyPI (production):"
echo "  twine upload dist/*"
echo ""
echo "Note: You'll need to have a PyPI account and be logged in with Twine."
echo "To set up your PyPI credentials, run: 'twine register'." 