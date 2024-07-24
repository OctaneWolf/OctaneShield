from fastapi import APIRouter
import utils.keys as keys
router = APIRouter(prefix="/wg-node", tags=["SettingsOfCurrentNode"])


@router.post("/regenerate-wireguard-keypair")
async def regenerate_wireguard_keypair():
    k = keys.generate_wireguard_keypair()
    keys.write_keys_to_files(k[0], k[1], "config/wireguard/keys/currentNode.key")
    return {"status": "success"}
