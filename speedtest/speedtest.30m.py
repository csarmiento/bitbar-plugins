#!/usr/bin/env python

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
