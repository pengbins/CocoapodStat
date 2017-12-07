#!/usr/bin/python3
import sys
import requests
import json
from datetime import datetime

metricsUrl = 'http://metrics.cocoapods.org/api/v1/pods/'
KEYS = [
    'app_total', 'app_week', 'download_month',
    'download_total', 'download_week'
]


def main(podName):
    # read cocoapods stats
    fullUrl = metricsUrl + podName
    resp = requests.get(fullUrl)
    # print (fullUrl, '[', resp.status_code, ']')
    if resp.ok:
        pods = json.loads(resp.content.decode("utf-8"))
        updated_at = pods['stats']['updated_at']  # 2017-03-22 09:09:08 UTC
        dt = datetime.strptime(updated_at, '%Y-%m-%d %H:%M:%S %Z')
        ts = str(int(dt.timestamp()))
        values = [str(pods['stats'][k]) for k in KEYS]
        out = ts + '\t' + '\t'.join(values)
        print (out)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('help: podstats podName')
        exit()
    main(sys.argv[1])
