股票实时价格查询工具
这个Python脚本用于查询指定股票的实时价格数据，通过简单的命令行接口与远程API交互。

功能特性
通过股票代码查询实时价格数据

简单的命令行操作

错误处理和超时机制

JSON格式的数据返回

依赖要求
Python 3.10+

requests库

安装依赖：

bash
pip install requests
使用方法

基本命令

python analys_stock_tool.py <股票代码>
示例查询
bash
# 查询平安银行(深交所)的实时价格
python analys_stock_tool.py 000001.SZ

# 查询贵州茅台(上交所)的实时价格
python analys_stock_tool.py 600519.SH
输出示例
json
{
  "symbol": "000001.SZ",
  "name": "平安银行",
  "price": 15.32,
  "change": 0.24,
  "change_percent": 1.59,
  "volume": 1845600,
  "amount": 2.83,
  "timestamp": "2023-08-15 14:45:00"
}
参数说明
参数	说明	示例
股票代码	交易所股票代码，需包含交易所后缀	000001.SZ (深交所)
600519.SH (上交所)
错误处理
常见错误信息：

使用方法: python stock_price.py <股票代码> - 缺少必要参数时显示

请求失败: ... - 网络请求失败（超时或连接错误）

发生错误: ... - 其他运行时错误

注意事项
需要稳定的网络连接

API服务地址为 http://211.159.225.228:9001/quant/price

查询超时时间为5秒

股票代码必须包含交易所后缀（.SZ或.SH）

贡献
欢迎提交Issue或Pull Request：
https://github.com/virgo777/qMCP

许可
MIT License