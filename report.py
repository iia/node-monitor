import os
import json
import time

FILE_NODES = "./nodes.json"

while True:
    report = None

    with open(FILE_NODES, "r+") as f:
        report = json.load(f)

        if "interval" not in report:
            report["interval"] = 10

        if "runs" not in report:
            report["runs"] = 1
        else:
            report["runs"] += 1

        for node in report["nodes"]:
            print("<I> Checking node: " + node["address"])

            if report["runs"] == 1:
                node["times_available"] = 0

            p = os.popen("ping -c 2 " + node["address"])

            p_out = p.read()

            if "time=" in p_out:
                print("<I> Node available: " + node["address"] + "\n")

                node["times_available"] += 1
            else:
                print("<I> Node unavailable: " + node["address"] + "\n")

            node["availability"] = (node["times_available"] / report["runs"]) * 100

    with open(FILE_NODES, "w+") as f:
        print("<I> Writing report...\n")

        f.write("")
        f.write(json.dumps(report, indent = 4))

    print("<I> Sleeping: " + str(report["interval"]) + " seconds\n")

    time.sleep(report["interval"])
