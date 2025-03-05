#!/bin/bash
# Install the Linode MCP package in development mode

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "Error: uv is not installed"
    echo "Please install uv first: https://github.com/astral-sh/uv"
    echo "You can install it with: pip install uv"
    exit 1
fi

# Create a virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment using uv..."
    uv venv
fi

# Activate the virtual environment
if [[ "$OSTYPE" == "darwin"* ]] || [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "Activating virtual environment..."
    source .venv/bin/activate
elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    echo "Activating virtual environment..."
    source .venv/Scripts/activate
else
    echo "Unsupported OS type: $OSTYPE"
    echo "Please activate the virtual environment manually."
    exit 1
fi

# Install the package in development mode using uv
echo "Installing Linode MCP in development mode with uv..."
uv pip install -e .

# Success message
echo ""
echo "Installation complete!"
echo ""
echo "Activate the environment to run the server:"
if [[ "$OSTYPE" == "darwin"* ]] || [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "  source .venv/bin/activate"
elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    echo "  source .venv/Scripts/activate"
fi
echo ""
echo "Run the server:"
echo "  linode-mcp"
echo "Or:"
echo "  python -m linode_mcp.server"
echo ""
echo "IMPORTANT: Linode API Token Setup"
echo "This tool requires a Linode API token to communicate with Linode services."
echo ""
echo "To obtain a Linode API token:"
echo "  1. Log in to your Linode account at https://cloud.linode.com"
echo "  2. Go to your profile and select the 'API Tokens' tab"
echo "  3. Click 'Create a Personal Access Token'"
echo "  4. Select the necessary scopes (at minimum: Linodes - Read/Write)"
echo "  5. Set an expiry date and label for your token"
echo ""