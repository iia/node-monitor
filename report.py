import os
import json

FILE_NODES = "./nodes.json"

report = None

with open(FILE_NODES, "r+") as f:
    report = json.load(f)

    if "runs" not in report:
        report["runs"] = 1
    else:
        report["runs"] += 1

    for node in report["nodes"]:
        os.run("logger \"[node-monitor] <I> Checking node: " + node["address"] + "\"")

        if report["runs"] == 1:
            node["times_available"] = 0

        p = os.popen("ping -c 2 " + node["address"])

        p_out = p.read()

        if "time=" in p_out:
            os.run("logger \"[node-monitor] <I> Node available: " + node["address"] + "\"")

            node["times_available"] += 1
        else:
            os.run("logger \"[node-monitor] <I> Node unavailable: " + node["address"] + "\"")

        node["availability"] = (node["times_available"] / report["runs"]) * 100

with open(FILE_NODES, "w+") as f:
    os.run("logger \"[node-monitor] <I> Writing report...\"")

    f.write("")
    f.write(json.dumps(report, indent = 4))
