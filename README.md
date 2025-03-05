# Linode MCP Server

[![PyPI version](https://badge.fury.io/py/linode-mcp.svg)](https://badge.fury.io/py/linode-mcp)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Model Context Protocol (MCP) server for interacting with Linode's API to manage cloud resources. This package enables Large Language Models (LLMs) like Claude to manage Linode instances through a standardized interface.

## Features

- List Linode regions, instance types, and instances
- Create, view details, delete, and reboot Linode instances
- Secure and easy-to-use interface for LLMs to manage Linode resources
- Fully compatible with MCP-enabled AI assistants like Claude

## Installation and Configuration

Set your Linode API key as an environment variable:

```bash
export LINODE_API_KEY=your_api_key_here
```

Or use a `.env` file in the project directory:

```
LINODE_API_KEY=your_api_key_here
```

You can generate an API key from the [Linode Cloud Manager](https://cloud.linode.com/profile/tokens).

### From PyPI (Recommended)

```bash
pip install linode-mcp
```

### Using uv
```bash
uvx pip install linode-mcp
uvx --from linode-mcp linode-mcp --api-key $LINODE_API_KEY
```

### From Source

```bash
# Clone the repository
git clone https://github.com/yourusername/linode-mcp.git
cd linode-mcp

# Install the package in development mode
./scripts/install.sh
```


## Usage

### As a Command Line Tool

```bash
# Run with default settings
linode-mcp

# Enable debug logging
linode-mcp --debug

# Specify API key on command line
linode-mcp --api-key your_api_key_here
```

### With Claude for Desktop

1. Install the package:
   ```bash
   pip install linode-mcp
   ```

2. Manually edit your Claude Desktop configuration file:
   
   - MacOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
   
   ```json
   {
     "mcpServers": {
       "linode": {
         "command": "linode-mcp",
         "args": ["--api-key", "your_api_key_here"]
       }
     }
   }
   ```

3. Restart Claude for Desktop

4. In a conversation with Claude, you can now ask it to:
   - List your Linode instances
   - Create a new Linode instance
   - Get details about a specific instance
   - Reboot or delete instances

Example prompts:
- "Show me all my Linode instances"
- "Create a new 2GB Linode in the Frankfurt region with Debian 11"
- "Reboot my instance with ID 12345"

## Available Tools

The package provides these MCP tools:

- `list_regions` - List all available Linode regions

To be added:
- `list_instance_types` - List all available Linode instance types and their pricing
- `list_instances` - List all existing Linode instances
- `create_instance` - Create a new Linode instance
- `get_instance` - Get details about a specific Linode instance
- `delete_instance` - Delete a Linode instance
- `reboot_instance` - Reboot a Linode instance

## Development

### Project Structure

```
linode-mcp/
├── bin/                  # Command-line scripts
├── src/                  # Source code
│   └── linode_mcp/       # Main package
│       ├── tools/        # MCP tool implementations
│       └── server.py     # MCP server implementation
├── setup.py              # Package setup file
└── README.md             # This file
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Linode API](https://www.linode.com/docs/api/) for providing the cloud infrastructure API
- [Model Context Protocol](https://modelcontextprotocol.io/) for the standard interface specification
- [Claude](https://claude.ai/) for AI assistant capabilities


