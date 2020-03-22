from flask import Flask
from jinja2 import Template
import json
import re
from flask import Flask, request


app = Flask(__name__)

@app.route("/")
def monitor():
    raw_logs = open("/usr/tmp/app/logs.log", "r").readlines()


    logs = []
    for log in raw_logs:
        regex_pattern = "\d{2}/\d{2}/\d{4}[\s]\d{2}:\d{2}:\d{2}[\s](?:AM|PM)[\s]\[status:(.*?)\][\s]\[status_code:(.*?)\][\s]\[url:(.*?)\][\s]\[response_time:(.*?)\]"
        is_log_match_regex = bool(re.match(regex_pattern, log))

        if is_log_match_regex:
            logs.append(log)

    template = Template(open('dashboard.jinja2').read())
    rendered = template.render(title="Web Monitor", logs=logs)

    return rendered

@app.route("/filter",  methods=['GET'])
def monitor_filter():
    raw_logs = open("/usr/tmp/app/logs.log", "r").readlines()
    filter_date = str(request.args['date']).replace('-', '/')

    logs = []
    for log in raw_logs:
        regex_pattern = "\d{2}/\d{2}/\d{4}[\s]\d{2}:\d{2}:\d{2}[\s](?:AM|PM)[\s]\[status:(.*?)\][\s]\[status_code:(.*?)\][\s]\[url:(.*?)\][\s]\[response_time:(.*?)\]"
        is_log_match_regex = bool(re.match(regex_pattern, log))


        if is_log_match_regex and log.startswith(filter_date):
            logs.append(log)

    template = Template(open('dashboard.jinja2').read())
    rendered = template.render(title="Web Monitor", logs=logs)

    return rendered

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
