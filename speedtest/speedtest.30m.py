#!/usr/bin/env python
# <bitbar.title>Speedtest</bitbar.title>
# <bitbar.version>v0.1</bitbar.version>
# <bitbar.author>Camilo Sarmiento</bitbar.author>
# <bitbar.desc>Monitors upload and download speeds using `speedtest-cli`.</bitbar.desc>

import re
import subprocess


def main():
    try:
        output = subprocess.check_output(["/usr/local/bin/speedtest-cli"])
        download = re.search('Download: (.*)', output).group(1)
        upload = re.search('Upload: (.*)', output).group(1)
        result = '%s :arrow_down: - %s :arrow_up:'
        print result % (download, upload)
    except subprocess.CalledProcessError as e:
        print e.output


main()
