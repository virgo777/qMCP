'''
Author: Mr.Car
Date: 2025-06-05
'''
from fastmcp import FastMCP
import httpx
from pydantic import BaseModel
from typing import Dict, Any, Optional

# 初始化 FastMCP 服务器
server = FastMCP()


# 定义股票数据模型
class StockData(BaseModel):
    """股票数据模型"""
    symbol: str
    name: str
    current: float
    open: float
    high: float
    low: float
    prev_close: float
    volume: int
    timestamp: str


@server.tool()
async def get_stock_price(
        symbol: str
) -> Dict[str, Any]:
    """
    Get real-time stock price data for a specified stock symbol

    Args:
        symbol: Stock symbol (e.g., '000001.SZ')

    Returns:
        dict: Dictionary containing stock price data

    获取指定股票代码的实时价格数据

    Args:
        symbol: 股票代码 (例如: '000001.SZ')

    Returns:
        dict: 包含股票价格数据的字典
    """
    # 构建请求URL
    url = f"http://211.159.225.228:9001/quant/price?symbol={symbol}"

    try:
        # 发送异步HTTP GET请求
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=5.0)
            response.raise_for_status()
            data = response.json()

            # 返回股票数据
            return data

    except httpx.TimeoutException:
        raise Exception("请求超时，请稍后重试")
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            raise Exception(f"未找到股票代码 '{symbol}' 的数据")
        raise Exception(f"HTTP错误: {e.response.status_code} - {e.response.text}")
    except (KeyError, ValueError, TypeError) as e:
        raise Exception(f"数据解析错误: {str(e)}")
    except Exception as e:
        raise Exception(f"获取股票数据时发生错误: {str(e)}")


# 运行服务器
if __name__ == "__main__":
    server.run()