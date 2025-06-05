from setuptools import setup, find_packages

setup(
    name='qMCP',  # 包的名字
    version='0.1.0',  # 版本号
    packages=find_packages(),  # 自动发现所有模块
    install_requires=[],  # 依赖的包，如果有的话，可以在这里指定
    author='xiaohua',
    author_email='5847713@qq.com',
    description='A package for stock quant analysis module',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/virgo777/qMCP',  # 项目的GitHub地址
    classifiers=[  # 分类器，用于描述包的用途和适用性
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',  # 适用的 Python 版本
)

