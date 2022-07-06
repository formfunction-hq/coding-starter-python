import asyncio
from solana.rpc.async_api import AsyncClient

# For simplicity, you can treat this simple array as an in-memory database
NFTS = [
  {
    # https://explorer.solana.com/address/76izV1NP9DuQ5GiTt4xALYrASUvedqrsQLQzYyK7X2Cu?cluster=devnet
    'address': '76izV1NP9DuQ5GiTt4xALYrASUvedqrsQLQzYyK7X2Cu',
    'owner': 'C7XtWMtkZWeBeQMgisTdwyxAxfYkyMopaDWi8TWB6w2E'
  }
]

async def main():
    async with AsyncClient("https://api.devnet.solana.com") as client:
        res = await client.is_connected()
        tx = await client.get_transaction("5Pd59gdwb1v3Qrg8zc5RLrdpXr7MX9L1WqGaiib9RYPJPhmXvnqMEguLmcrk1NPpycJaa7naxgLsRPAK3JLo5tZ3")
        print(tx)
    print(res)  # True

asyncio.run(main())