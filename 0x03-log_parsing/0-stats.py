#!/usr/bin/python3
"""Log parsing of HTTP requests"""

import sys
import signal
import re

total_size = 0
status_counts = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
line_count = 0

log_pattern = re.compile(r'^\S+ - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{6}\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$')


def extract_input(input_line):
    '''Extracts and returns the status code and file size from a log line.'''
    info = {
        'status_code': '0',
        'file_size': 0,
    }
    match = log_pattern.match(input_line)
    if match:
        info['status_code'] = match.group(1)
        info['file_size'] = int(match.group(2))
    else:
        print(f"No match for line: {input_line}", file=sys.stderr)
    return info


def update_metrics(line):
    '''Updates the metrics from a given HTTP request log line.'''
    global total_size
    line_info = extract_input(line)
    status_code = line_info['status_code']
    if status_code in status_counts:
        status_counts[status_code] += 1
    total_size += line_info['file_size']


def print_statistics():
    '''Prints the accumulated statistics of the HTTP request logs.'''
    print(f"File size: {total_size}", flush=True)
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print(f"{status_code}: {status_counts[status_code]}", flush=True)


def signal_handler(sig, frame):
    '''Handles the keyboard interruption (CTRL + C) and prints statistics.'''
    print_statistics()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


try:
    while True:
        line = input().strip()
        if line:
            update_metrics(line)
            line_count += 1
            if line_count % 10 == 0:
                print_statistics()
except (KeyboardInterrupt, EOFError):
    print_statistics()
    sys.exit(0)


if __name__ == "__main__":
    run()
