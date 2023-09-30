import os
import json

FILE_NODES = "./nodes.json"

report = None

with open(FILE_NODES, "r+") as f:
    report = json.load(f)

    for node in report["nodes"]:
        if "runs" not in node:
            node["runs"] = 1
        else:
            node["runs"] += 1

        os.system("logger \"[node-monitor] <I> Checking node: " + node["address"] + "\"")

        if node["runs"] == 1 or "times_available" not in node:
            node["times_available"] = 0

        p = os.popen("ping -c 2 " + node["address"])

        p_out = p.read()

        if "time=" in p_out:
            os.system("logger \"[node-monitor] <I> Node available: " + node["address"] + "\"")

            node["times_available"] += 1
        else:
            os.system("logger \"[node-monitor] <I> Node unavailable: " + node["address"] + "\"")

        node["availability"] = (node["times_available"] / node["runs"]) * 100

with open(FILE_NODES, "w+") as f:
    os.system("logger \"[node-monitor] <I> Writing report...\"")

    f.write("")
    f.write(json.dumps(report, indent = 4))
