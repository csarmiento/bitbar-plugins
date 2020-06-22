#!/usr/bin/env python3

# <bitbar.title>Bitbar speedtest plugin</bitbar.title>
# <bitbar.version>v0.1</bitbar.version>
# <bitbar.author>Camilo Sarmiento</bitbar.author>
# <bitbar.author.github>csarmiento</bitbar.author.github>
# <bitbar.desc>Monitors upload and download speeds using `speedtest-cli`.</bitbar.desc>
# <bitbar.dependencies>python</bitbar.dependencies>

import os
import re
import subprocess


def main():
    try:
        os.environ['PYTHONHTTPSVERIFY'] = "0"
        output = subprocess.check_output(["/usr/local/bin/speedtest-cli"])
        download_str = re.search('Download: (.*)', output).group(1)
        upload_str = re.search('Upload: (.*)', output).group(1)
        download_val = float(re.search('(.*) Mbit/s', download_str).group(1))
        upload_val = float(re.search('(.*) Mbit/s', upload_str).group(1))
        print(get_status('%s :arrow_down:' % (download_str), download_val, 35))
        print(get_status('%s :arrow_up:' % (upload_str), upload_val, 7))
    except subprocess.CalledProcessError as e:
        print(e.output)


def get_status(status_str, current_val, min_value):
    if (current_val >= min_value):
        status_str += '|color=green'
    else:
        status_str += '|color=red'
    return status_str


main()
