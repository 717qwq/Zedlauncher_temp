import itertools
from steam import SteamQuery

# 定义 IP 和端口列表
server_ip = ["110.42.9.149", "110.42.9.181"]
port = [27015, 27016]


def ZombiEden_Server_Query():
    server_info = []

    # 遍历 IP 和端口组合
    for ip, p in itertools.product(server_ip, port):
        try:
            server_obj = SteamQuery(ip, p)

            # 使用公开方法获取服务器信息
            info = server_obj.query_server_info()

            server_info.append({
                'ip': ip,
                'port': p,
                'name': info.get('name', 'N/A'),
                'map': info.get('map', 'N/A'),
                'players': info.get('players', 'N/A')
            })
        except Exception as e:
            print(f"查询 {ip}:{p} 时出错: {e}")
    # 返回 server_info 列表
    return server_info


if __name__ == "__main__":
    # 调用 ZombiEden_Server_Query 函数并获取结果
    result = ZombiEden_Server_Query()

    # 打印结果
    for info in result:
        print(info)
