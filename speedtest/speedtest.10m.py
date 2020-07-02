#!/usr/bin/env python3

# <bitbar.title>Bitbar speedtest plugin</bitbar.title>
# <bitbar.version>v0.1</bitbar.version>
# <bitbar.author>Camilo Sarmiento</bitbar.author>
# <bitbar.author.github>csarmiento</bitbar.author.github>
# <bitbar.desc>Monitors upload and download speeds using `speedtest`.</bitbar.desc>
# <bitbar.dependencies>python</bitbar.dependencies>

import os
import re
import subprocess


def main():
    try:
        # os.environ['PYTHONHTTPSVERIFY'] = "0"
        byte_output = subprocess.check_output(["/usr/local/bin/speedtest"])
        output = byte_output.decode("utf-8")

        result = get_network_status(output)

        print(result)


    except subprocess.CalledProcessError as e:
        print(e.output)


def get_network_status(output):
    buffer = []
    download_str = re.search('Download: (.*)', output).group(1)
    upload_str = re.search('Upload: (.*)', output).group(1)
    latency_str = re.search('Latency: (.*)', output).group(1)
    packet_loss_str = re.search('Packet Loss: (.*)', output).group(1)
    download_val = float(re.search('(.*) Mbps', download_str).group(1))
    upload_val = float(re.search('(.*) Mbps', upload_str).group(1))
    latency_val = float(re.search('^(.*?)ms', latency_str).group(1))
    buffer.append(get_color_by_min(f'{download_str.strip()} :arrow_down:', download_val, 50))
    buffer.append(get_color_by_min(f'{upload_str.strip()} :arrow_up:', upload_val, 7))
    buffer.append(get_color_by_max(f'{latency_str.strip()} :zap:', latency_val, 50))
    if 'Not available' in packet_loss_str:
        buffer.append('Not available :no_mobile_phones:|color=red')
    else:
        packet_loss_val = float(re.search('(.*)%', packet_loss_str).group(1))
        buffer.append(get_color_by_max(f'{packet_loss_str.strip()} :no_mobile_phones:', packet_loss_val, 1))

    return '\n'.join(buffer)


def get_color_by_min(status_str: str, current_val: float, min_value: float) -> str:
    return status_str + '|color=green' if current_val >= min_value else status_str + '|color=red'


def get_color_by_max(status_str: str, current_val: float, max_value: float) -> str:
    return status_str + ('|color=green' if current_val <= max_value else '|color=red')


main()
