import requests
import sys


def get_stock_price(symbol):
    """
    获取指定股票代码的实时价格数据

    参数:
    symbol (str): 股票代码 (例如: '000001.SZ')

    返回:
    dict: 解析后的JSON数据

    异常:
    抛出requests异常或状态码非200时抛出异常
    """
    # 构建请求URL
    url = f"http://211.159.225.228:9001/quant/price?symbol={symbol}"

    try:
        # 发送HTTP GET请求
        response = requests.get(url, timeout=5)  # 设置5秒超时

        # 检查HTTP状态码
        response.raise_for_status()

        # 解析JSON响应
        return response.json()

    except requests.exceptions.RequestException as e:
        # 处理请求异常
        raise Exception(f"请求失败: {str(e)}") from e


# 主程序入口
if __name__ == "__main__":
    # 检查命令行参数
    if len(sys.argv) < 2:
        print("使用方法: python stock_price.py <股票代码>")
        print("示例: python stock_price.py 000001.SZ")
        sys.exit(1)

    # 获取股票代码参数
    symbol = sys.argv[1]

    try:
        # 获取并打印股票数据
        stock_data = get_stock_price(symbol)
        print("股票数据获取成功:")
        print(stock_data)

    except Exception as e:
        print(f"发生错误: {str(e)}")
        sys.exit(1)


#C:\Users\xiaohua\Desktop\qMCP\src>  python -m analys_stock_tool 000858.sz
"""
{
  "command": "python",
  "args": ["-m", "mcp_server_time", "--local-timezone=America/New_York"]
}

"""