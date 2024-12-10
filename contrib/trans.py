#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

# 定义端口到架构的映射函数
def get_arch_prefix(port):
    port = int(port)
    if 22001 <= port <= 23000:
        return "amd64"
    elif 23001 <= port <= 24000:
        return "loongson3"
    elif 24001 <= port <= 25000:
        return "arm64"
    elif 25001 <= port <= 26000:
        return "ppc64el"
    elif 26001 <= port <= 27000:
        return "riscv64"
    elif 27001 <= port <= 28000:
        return "loongarch64"
    elif 28001 <= port <= 29000:
        return "amd64"
        #这里有坑
        #目前都是amd64...
        #应该是emulation的部分
    else:
        return None

lines = sys.stdin.read().splitlines()

current_host_names = []
current_host_lines = []
current_arch = None

def output_host_block(host_names, host_lines, arch):
    # 如果能识别出架构，则在原Host行后面添加带前缀的主机名
    if arch is not None:
        # 构造带架构前缀的Host行
        new_host_names = host_names.copy()
        for hn in host_names:
            new_host_names.append(f"{arch}-{hn}")

        # 输出修改后的Host行（原名称和带架构前缀的名称都包含在同一行）
        print("Host " + " ".join(new_host_names))
        # 输出其余配置行
        for line in host_lines[1:]:
            print(line)
    else:
        # 如果没有识别出架构，则原样输出
        for line in host_lines:
            print(line)
    print()  # 块结束后加一行空行

for line in lines:
    # 匹配 Host 行
    if line.strip().startswith("Host "):
        # 如果之前有一个host块在收集，将其输出
        if current_host_names:
            output_host_block(current_host_names, current_host_lines, current_arch)

        # 开始新的host块
        current_host_names = line.strip().split()[1:]
        current_host_lines = [line]
        current_arch = None
    else:
        # 不是Host行则加入当前host配置块
        current_host_lines.append(line)
        # 检测Port行来决定架构
        if line.strip().startswith("Port "):
            port_num = line.strip().split()[1]
            current_arch = get_arch_prefix(port_num)

# 文件结束后，如果还有一个host块未输出，则输出
if current_host_names:
    output_host_block(current_host_names, current_host_lines, current_arch)

