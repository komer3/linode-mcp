import json
import logging
from typing import Any, Dict, List, cast
from linode_api4 import LinodeClient
from linode_api4.objects import Region

logger = logging.getLogger(__name__)

def register_tools(mcp_server: Any, linode_client: LinodeClient):
    """
    Register all Linode tools with the MCP server
    
    Args:
        mcp_server: The MCP server instance
        linode_client: The initialized Linode client
    """
    # Store the Linode client reference for tool access
    mcp_server.linode_client = linode_client
    
    # List regions
    @mcp_server.tool()
    def list_regions() -> str:
        """List all available Linode regions"""
        try:
            # Get the regions list
            regions_list = linode_client.regions()
            
            # Process each region in the collection
            result = []
            # Type annotation to help linter
            for item in regions_list:
                # Cast to Region type to resolve linting issues
                region = cast(Region, item)
                result.append({
                    "id": region.id,
                    "country": region.country,
                    "status": region.status,
                    "capabilities": region.capabilities
                })
                
            return json.dumps(result)
        except Exception as e:
            logger.error(f"Error listing regions: {str(e)}")
            return json.dumps({"error": str(e)})

    # # List instance types with pricing
    # @mcp_server.tool(name="list_instance_types")
    # def list_instance_types(random_string: str = "") -> str:
    #     """List all available Linode instance types and their pricing"""
    #     try:
    #         types = linode_client.linode.types.all()
    #         result = [{
    #             "id": type.id,
    #             "label": type.label,
    #             "vcpus": type.vcpus,
    #             "memory": type.memory,
    #             "disk": type.disk,
    #             "transfer": type.transfer,
    #             "price_monthly": type.price.monthly,
    #             "price_hourly": type.price.hourly
    #         } for type in types]
    #         return json.dumps(result)
    #     except Exception as e:
    #         logger.error(f"Error listing instance types: {str(e)}")
    #         return json.dumps({"error": str(e)})

    # # List instances
    # @mcp_server.tool(name="list_instances")
    # def list_instances(random_string: str = "") -> str:
    #     """List all existing Linode instances"""
    #     try:
    #         instances = linode_client.linode.instances.all()
    #         result = [{
    #             "id": instance.id,
    #             "label": instance.label,
    #             "region": instance.region.id,
    #             "type": instance.type.id,
    #             "status": instance.status,
    #             "ipv4": instance.ipv4,
    #             "created": str(instance.created),
    #             "updated": str(instance.updated)
    #         } for instance in instances]
    #         return json.dumps(result)
    #     except Exception as e:
    #         logger.error(f"Error listing instances: {str(e)}")
    #         return json.dumps({"error": str(e)})

    # # Create instance
    # @mcp_server.tool(name="create_instance")
    # def create_instance(label: str, region: str, type: str, image: str, root_pass: str) -> str:
    #     """
    #     Create a new Linode instance
        
    #     Args:
    #         label: Label for the Linode
    #         region: Region ID (use list_regions to see available options)
    #         type: Instance type ID (use list_instance_types to see available options)
    #         image: Image ID (e.g., 'linode/debian11')
    #         root_pass: Strong password for the root user
    #     """
    #     try:
    #         # Input validation
    #         if len(root_pass) < 8:
    #             return json.dumps({"error": "Root password must be at least 8 characters"})
                
    #         # Create the instance
    #         instance = linode_client.linode.instances.create(
    #             type=type,
    #             region=region,
    #             image=image,
    #             label=label,
    #             root_pass=root_pass
    #         )
            
    #         result = {
    #             "id": instance.id,
    #             "label": instance.label,
    #             "status": instance.status,
    #             "ipv4": instance.ipv4,
    #             "region": instance.region.id,
    #             "type": instance.type.id
    #         }
    #         return json.dumps(result)
    #     except Exception as e:
    #         logger.error(f"Error creating instance: {str(e)}")
    #         return json.dumps({"error": str(e)})
                
    # # Get instance details
    # @mcp_server.tool(name="get_instance")
    # def get_instance(id: int) -> str:
    #     """
    #     Get details about a specific Linode instance
        
    #     Args:
    #         id: Linode instance ID
    #     """
    #     try:
    #         instance = linode_client.linode.instances.get(id)
            
    #         result = {
    #             "id": instance.id,
    #             "label": instance.label,
    #             "status": instance.status,
    #             "ipv4": instance.ipv4,
    #             "ipv6": instance.ipv6,
    #             "region": instance.region.id,
    #             "type": instance.type.id,
    #             "specs": {
    #                 "disk": instance.specs.disk,
    #                 "memory": instance.specs.memory,
    #                 "vcpus": instance.specs.vcpus,
    #                 "transfer": instance.specs.transfer
    #             },
    #             "created": str(instance.created),
    #             "updated": str(instance.updated)
    #         }
    #         return json.dumps(result)
    #     except Exception as e:
    #         logger.error(f"Error getting instance details: {str(e)}")
    #         return json.dumps({"error": str(e)})
                
    # # Delete instance
    # @mcp_server.tool(name="delete_instance")
    # def delete_instance(id: int) -> str:
    #     """
    #     Delete a Linode instance
        
    #     Args:
    #         id: Linode instance ID
    #     """
    #     try:
    #         instance = linode_client.linode.instances.get(id)
    #         instance_label = instance.label
    #         instance.delete()
            
    #         return json.dumps({
    #             "success": True,
    #             "message": f"Instance {id} ({instance_label}) has been deleted"
    #         })
    #     except Exception as e:
    #         logger.error(f"Error deleting instance: {str(e)}")
    #         return json.dumps({"error": str(e)})
                
    # # Reboot instance
    # @mcp_server.tool(name="reboot_instance")
    # def reboot_instance(id: int) -> str:
    #     """
    #     Reboot a Linode instance
        
    #     Args:
    #         id: Linode instance ID
    #     """
    #     try:
    #         instance = linode_client.linode.instances.get(id)
    #         instance.reboot()
            
    #         return json.dumps({
    #             "success": True,
    #             "message": f"Instance {id} reboot initiated"
    #         })
    #     except Exception as e:
    #         logger.error(f"Error rebooting instance: {str(e)}")
    #         return json.dumps({"error": str(e)}) 