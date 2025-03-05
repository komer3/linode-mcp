from setuptools import setup, find_packages

setup(
    name="linode-mcp",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "mcp-server",
        "linode-api4",
        "python-dotenv"
    ],
    entry_points={
        "console_scripts": [
            "linode-mcp=linode_mcp.server:main",
        ],
    },
    python_requires=">=3.13",
) 