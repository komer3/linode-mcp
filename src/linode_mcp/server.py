#!/usr/bin/env python3
import argparse
import os
import logging
import sys
from mcp.server.fastmcp import FastMCP
from linode_api4 import LinodeClient
from linode_mcp.tools.linode_tools import register_tools

# Try to load dotenv if available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # python-dotenv not installed, environment variables will be used directly

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    """Main entry point for the Linode MCP Server"""
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Linode MCP Server')
    parser.add_argument('--api-key', help='Linode API key')
    parser.add_argument('--debug', action='store_true', help='Enable debug logging')
    args = parser.parse_args()
    
    # Set debug logging if requested
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
        logger.debug("Debug logging enabled")
    
    # Get API key from args or environment variable
    api_key = args.api_key or os.environ.get('LINODE_API_KEY')
    if not api_key:
        logger.error("Linode API key is required. Provide via --api-key or LINODE_API_KEY environment variable.")
        sys.exit(1)
    
    # Initialize Linode client
    try:
        linode_client = LinodeClient(api_key)
        # Test with a lightweight API call - regions() is a good choice
        linode_client.regions()
        logger.info("Successfully authenticated with Linode API")
    except Exception as e:
        logger.error(f"Failed to authenticate with Linode API: {str(e)}")
        sys.exit(1)
    
    # Create MCP server with clear naming
    mcp = FastMCP(name="Linode Manager")
    
    # Register tools from the linode_tools module
    logger.debug("Registering Linode tools with MCP server")
    register_tools(mcp, linode_client)
    
    # Start the server
    logger.info("Starting Linode MCP Server...")
    try:
        mcp.run()  # Synchronous version
    except KeyboardInterrupt:
        logger.info("Server shutdown requested by user")
    except Exception as e:
        logger.error(f"Server error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 