# choas_everyday

# Subdomain Extractor Tool From Choas

This tool automates the process of downloading and extracting subdomain data from choas, comparing new results with previous entries, and identifying any newly added subdomains.

## Features

- **Automated Download**: Fetches the latest subdomain data from a specified URL.
- **Extraction**: Unzips the downloaded file and extracts subdomain information from various text files.
- **Comparison**: Compares the newly extracted subdomains with previously saved entries to identify new additions.
- **Storage**: Saves all discovered subdomains in a persistent text file for future comparisons.
- **User-Friendly Output**: Displays the new subdomains found in a clear format and indicates when no new subdomains are discovered.

## Requirements

- Python 3.x
- `requests` library (can be installed via `pip install requests`)

## Usage

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   python3 choas_everyday.py
