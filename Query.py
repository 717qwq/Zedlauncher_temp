import itertools
from steam import SteamQuery

# 定义 IP 和端口列表
zedserver_ip = ["110.42.9.149", "110.42.9.181", "110.42.9.22"]  # ZombiEden服务器IP列表
zedport = [27015, 27016]  # ZombiEden服务器端口列表

exgserver_ip = ["202.189.15.68", "202.189.6.129", "202.189.15.252","202.189.15.61","202.189.10.39"]  # EXG服务器IP列表
exgport = [27001, 27002]  # EXG服务器端口列表


def ZombiEden_Server_Query():
    """
    查询ZombiEden服务器信息的函数
    返回: 包含服务器信息的字典列表
    """
    server_info = []

    # 遍历 IP 和端口组合
    for ip, p in itertools.product(zedserver_ip, zedport):
        try:
            # 创建SteamQuery对象
            server_obj = SteamQuery(ip, p)

            # 使用公开方法获取服务器信息
            info = server_obj.query_server_info()

            # 将服务器信息添加到列表中
            server_info.append({
                'ip': ip,
                'port': p,
                'name': info.get('name', 'N/A'),  # 服务器名称
                'map': info.get('map', 'N/A'),    # 当前地图
                'players': info.get('players', 'N/A')  # 在线玩家数
            })
        except Exception as e:
            print(f"查询 {ip}:{p} 时出错: {e}")
    # 返回 server_info 列表
    return server_info

def EXG_Server_Query():
    """
    查询EXG服务器信息的函数
    返回: 包含服务器信息的字典列表
    """
    server_info = []

    # 遍历 IP 和端口组合
    for ip, p in itertools.product(exgserver_ip, exgport):
        try:
            # 创建SteamQuery对象
            server_obj = SteamQuery(ip, p)

            # 使用公开方法获取服务器信息
            info = server_obj.query_server_info()

            # 将服务器信息添加到列表中
            server_info.append({
                'ip': ip,
                'port': p,
                'name': info.get('name', 'N/A'),  # 服务器名称
                'map': info.get('map', 'N/A'),    # 当前地图
                'players': info.get('players', 'N/A')  # 在线玩家数
            })
        except Exception as e:
            print(f"查询 {ip}:{p} 时出错: {e}")
    # 返回 server_info 列表
    return server_info


if __name__ == "__main__":
    # 调用 ZombiEden_Server_Query 和 EXG_Server_Query 函数并合并结果
    result = ZombiEden_Server_Query() + EXG_Server_Query()

    # 打印每个服务器的信息
    for info in result:
        print(info)
