# 示例调用代码
import asyncio
from src import server
async def main():
    # 通过FastMCP客户端调用工具
    result = await server.get_stock_price("000858.SZ")
    print(result)

asyncio.run(main())