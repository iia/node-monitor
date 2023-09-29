import json
from bottle import route, run, view

FILE_NODES = "./nodes.json"

@route('/nodes')
@view('nodes')
def do_availability():
    template_data = {}

    with open(FILE_NODES, "r+") as f:
        report = json.load(f)

        for node in report["nodes"]:
            if "availability" in node:
                availability = str(node["availability"]) + "%"
            else:
                availability = "-"

            template_data[node["address"]] = availability

    return dict(template_data = template_data)

run(host='localhost', port=8080, debug=True)
