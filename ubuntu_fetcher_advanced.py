import requests
import os
from urllib.parse import urlparse

def fetch_image(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Check that content is an image
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Skipped {url} (not an image: {content_type})")
            return
        
        # Extract filename
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path) or "downloaded_image.jpg"
        
        filepath = os.path.join("Fetched_Images", filename)
        
        # Prevent duplicates
        if os.path.exists(filepath):
            print(f"⚠ Skipped {filename} (already exists)")
            return

        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
    
    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error for {url}: {e}")
    except Exception as e:
        print(f"✗ Error fetching {url}: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher (Advanced)")
    print("A tool for mindfully collecting images from the web\n")

    os.makedirs("Fetched_Images", exist_ok=True)
    
    urls = input("Enter one or more image URLs (separated by spaces): ").split()
    for url in urls:
        fetch_image(url)
    
    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
