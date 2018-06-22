import subprocess
import json
from decimal import Decimal, ROUND_HALF_UP
import configparser
from flask import Flask, render_template

gpu_servers = []

app = Flask(__name__)


def get_gpu_info():
    data = {}
    for name in gpu_servers:
        data[name] = []
        try:
            cmd = "ssh " + name + " nvidia-smi --query-gpu=index,utilization.gpu,memory.total,memory.used,temperature.gpu --format=csv,noheader,nounits"
            lines = subprocess.check_output(cmd, shell=True).decode().split("\n")
            lines = [line.strip() for line in lines]
            lines = [line for line in lines if line != ""]
            for line in lines:
                using = False
                (gpuid, util_gpu, memory_total, memory_used, temp) = line.split(",")
                util_memory = 100 * int(memory_used) / int(memory_total)
                util_memory = Decimal(util_memory).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
                using = 10 <= int(util_gpu) or 10 <= int(util_memory)
                data[name].append({
                    "gpuid": gpuid,
                    "util_gpu": util_gpu,
                    "util_memory": util_memory,
                    "using": using,
                    "temp": temp
                })
        except:
            del data[name]
    return data


@app.route('/')
def index():
    data = get_gpu_info()
    return render_template("index.html", data=data)


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read("config.ini")
    gpu_servers = config["DEFAULT"]["gpu_servers"].split()
    web_server = config["DEFAULT"]["web_server"]
    port = int(config["DEFAULT"]["port"])

    app.debug = True
    app.run(host=web_server, port=port)
