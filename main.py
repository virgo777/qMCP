import tushare as ts
import math
from datetime import datetime, timedelta
from fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("calculateQuantMcp", host="0.0.0.0", port=9000)

ts.set_token('d540bc13ad69c6236ea')
pro = ts.pro_api()

def calculate_q_levels(low, high):
    A = low
    B = high
    return {
        "保守位": f"{conservative:.2f}",
        "正常位": f"{normal:.2f}",
        "极限位": f"{extreme:.2f}"
    }

@mcp.tool()
def get_quant_price(symbol: str = '000001.SZ'):
    """根据传入的股票symbol计算保守位，正常位，极限位"""

    # 计算日期范围（最近30天）
    end_date = datetime.today()
    start_date = end_date - timedelta(days=128)

    # 转换日期格式
    start_date_str = start_date.strftime('%Y%m%d')
    end_date_str = end_date.strftime('%Y%m%d')

    # 获取股票数据
    df = pro.daily(ts_code=symbol, start_date=start_date_str, end_date=end_date_str)

    if df.empty:
        return {"error": "未找到该股票数据"}

    # 获取最低价和最高价
    low = df["low"].min()
    high = df["high"].max()

    # 计算点位
    result = calculate_q_levels(low, high)

    result = f"这里展示了计算结果，对于该股票“{symbol}”的计算结果如下：“{result}”，一般认为股票现价小于极限位可以大胆计入，股票现价位于正常位和极限位之间，则可以进行关注。"
    return result



if __name__ == "__main__":
    mcp.run(transport="sse")
