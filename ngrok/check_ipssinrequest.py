import gzip
import re

# Function to extract IPs from log file
def extract_ips(file):
    ip_pattern = re.compile(r'::ffff:(\d+\.\d+\.\d+\.\d+)')
    ips = set()
    
    with gzip.open(file, 'rt') as f:
        for line in f:
            match = ip_pattern.search(line)
            if match:
                ips.add(match.group(1))
    
    return ips
# Main function to compare IPs across log files
def find_different_ips(files):
    all_ips = set()
    common_ips = None
    
    for file in files:
        file_ips = extract_ips(file)
        all_ips.update(file_ips)
        
        if common_ips is None:
            common_ips = file_ips
        else:
            common_ips &= file_ips
    
    different_ips = all_ips - common_ips
    return different_ips

# List of log files to check
log_files = ['sys.log-20240815.gz', 'sys.log-20240814.gz']

# Find different IPs
different_ips = find_different_ips(log_files)

# Output the different IPs
if different_ips:
    print("Different IPs found:")
    for ip in different_ips:
        print(ip)
else:
    print("No different IPs found.")
