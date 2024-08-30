#!/usr/bin/python3
"""A script for parsing HTTP request logs and computing metrics."""

import sys
import re

log_pattern = re.compile(
    r'^\S+ - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{6}\] '
    r'"GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
)


def print_statistics(total_file_size, status_codes_stats):
    """Prints the accumulated statistics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes_stats.keys()):
        if status_codes_stats[code] > 0:
            print(f"{code}: {status_codes_stats[code]}")


def parse_log_line(line):
    """Parses a line from the log and returns the status code and file size."""
    match = log_pattern.match(line)
    if match:
        return match.group(1), int(match.group(2))
    return None, 0


def run():
    """Main function to process the log and compute metrics."""
    total_file_size = 0
    status_codes_stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    line_count = 0

    try:
        for line in sys.stdin:
            status_code, file_size = parse_log_line(line)
            if status_code:
                total_file_size += file_size
                status_codes_stats[status_code] += 1
            line_count += 1

            if line_count % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)

    except KeyboardInterrupt:
        print_statistics(total_file_size, status_codes_stats)
        raise

    print_statistics(total_file_size, status_codes_stats)


if __name__ == "__main__":
    run()
