#!/bin/bash
# Script to run the MCP inspector with the Linode MCP server

# Set the API key from .env file if it exists
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi

# Check if the API key is set
if [ -z "$LINODE_API_KEY" ]; then
    echo "Error: LINODE_API_KEY environment variable is not set."
    echo "Please set it in a .env file or export it in your shell."
    exit 1
fi

echo "Starting MCP Inspector for Linode MCP Server..."

# Activate virtual environment if it exists and we're not already in it
if [ -d ".venv" ] && [ -z "$VIRTUAL_ENV" ]; then
    source .venv/bin/activate
fi

# Run the inspector with npx to directly execute the MCP server
# This is the most reliable method given the error message
npx @modelcontextprotocol/inspector uv run bin/linode-mcp --api-key "$LINODE_API_KEY"

# Alternative direct method using mcp dev --
# mcp dev -- python server.py --api-key "$LINODE_API_KEY" 