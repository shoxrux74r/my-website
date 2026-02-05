import psutil
import time

print("Монитор сети запущен...")

while True:
    connections = psutil.net_connections()
    active = []

    for conn in connections:
        if conn.raddr:
            active.append({
                "process": conn.pid,
                "local_addr": f"{conn.laddr.ip}:{conn.laddr.port}",
                "remote_addr": f"{conn.raddr.ip}:{conn.raddr.port}",
                "status": conn.status
            })

    print("\nАктивные подключения:")
    for item in active:
        print(
            f"PID: {item['process']} | "
            f"Локально: {item['local_addr']} -> "
            f"Удалённо: {item['remote_addr']} | "
            f"Статус: {item['status']}"
        )

    time.sleep(2)
