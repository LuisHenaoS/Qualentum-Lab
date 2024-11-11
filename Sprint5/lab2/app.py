from flask import Flask

import psutil
import platform

app = Flask(__name__)

@app.route('/metrics')
def metrics():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    uptime = int(psutil.boot_time())
    hostname = platform.node()
    disk = psutil.disk_usage('/')

    return {
        "cpu_usage_percent": cpu_usage,
        "memory_total": memory.total,
        "memory_available": memory.available,
        "memory_used": memory.used,
        "memory_used_percent": memory.percent,
        "system_uptime_seconds": uptime,
        "system_hostname": hostname,
        "disk_total": disk.used,
        "disk_free": disk.free,
        "disk_used_percent": disk.percent

    }

    