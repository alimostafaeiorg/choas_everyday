import os
import requests
import zipfile
import re

# Download link
url = "https://chaos-data.projectdiscovery.io/dell_technologies.zip"
# Zip file name
zip_filename = "dell_technologies.zip"
# Directory for storing subdomains
output_dir = "subdomains"
# File for storing all subdomains
subdomains_file = "subdomains_list.txt"

def download_file(url):
    response = requests.get(url)
    with open(zip_filename, 'wb') as f:
        f.write(response.content)

def extract_zip():
    with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
        zip_ref.extractall(output_dir)

def extract_all_subdomains():
    subdomains = set()
    for root, dirs, files in os.walk(output_dir):
        for file in files:
            if file.endswith('.txt'):
                with open(os.path.join(root, file), 'r') as f:
                    content = f.read()
                    found_subdomains = re.findall(r'\b([a-zA-Z0-9-]+\.[a-zA-Z0-9.-]+)\b', content)
                    subdomains.update(found_subdomains)
    return subdomains

def read_previous_subdomains():
    if os.path.exists(subdomains_file):
        with open(subdomains_file, 'r') as f:
            return set(f.read().splitlines())
    return set()

def save_subdomains(subdomains):
    with open(subdomains_file, 'a') as f:
        for subdomain in subdomains:
            f.write(subdomain + "\n")

def main():
    # Download the file
    download_file(url)
    # Extract the file
    extract_zip()
    
    # Extract new subdomains
    current_subdomains = extract_all_subdomains()
    
    # Read previous subdomains
    previous_subdomains = read_previous_subdomains()
    
    # Find new subdomains
    new_subdomains = current_subdomains - previous_subdomains
    
    # Display new subdomains
    if new_subdomains:
        print("\033[92mNew subdomains found:\033[0m")  # Green color
        for subdomain in new_subdomains:
            print("\033[92m" + subdomain + "\033[0m")  # Green color
    else:
        print("\033[92mNo new subdomains found.\033[0m")  # Green color

    # Save new subdomains to the file
    save_subdomains(current_subdomains)

    # Display created by message
    print("\033[93mCreate By alimostafaeiorg\033[0m")  # Yellow color

if __name__ == "__main__":
    main()
