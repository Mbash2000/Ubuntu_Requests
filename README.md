# Ubuntu Requests – Image Fetcher Assignment

> *"I am because we are." – Ubuntu Philosophy*

This project is inspired by the spirit of Ubuntu, emphasizing **community, respect, sharing, and practicality**.  
The goal is to create a Python program that respectfully connects to the web community, fetches shared images, and organizes them locally for later appreciation.

---

## 📌 Features

### Main Script: `ubuntu_fetcher.py`
- Prompts the user for a **single image URL**
- Creates a directory called **`Fetched_Images/`** (if it doesn’t exist)
- Downloads the image using the **requests** library
- Extracts the filename from the URL (or generates one if not available)
- Saves the image in binary mode to the `Fetched_Images/` folder
- Handles errors gracefully (connection issues, invalid responses, etc.)
- Prints friendly Ubuntu-inspired messages

### Advanced Script: `ubuntu_fetcher_advanced.py`
- Accepts **multiple URLs** at once
- Skips **duplicate downloads** if the image already exists
- Validates that the response is actually an **image** (via HTTP headers)
- Maintains all Ubuntu-inspired messaging and error handling

---

## 🖥 Example Output

Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Please enter the image URL: https://example.com/ubuntu-wallpaper.jpg

✓ Successfully fetched: ubuntu-wallpaper.jpg
✓ Image saved to Fetched_Images/ubuntu-wallpaper.jpg

Connection strengthened. Community enriched.


---

## 📂 Project Structure

Ubuntu_Requests/
│
├── ubuntu_fetcher.py # Main assignment script
├── ubuntu_fetcher_advanced.py # Challenge extension (multiple URLs, safety checks)
└── README.md # Documentation

---

## ⚙️ How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/Mbash2000/Ubuntu_Requests.git
   cd Ubuntu_Requests

2. Run the main script:
   python3 ubuntu_fetcher.py

3. Run the advanced script:
   python3 ubuntu_fetcher_advanced.py

Requirements:
-Python 3.x
-requests library

Install dependencies:
pip install requests

Ubuntu Principles in Action:
-Community: Connects with the global web community to fetch resources
-Respect: Handles errors gracefully without crashing
-Sharing: Saves images neatly for later viewing or sharing
-Practicality: Simple, real-world tool that anyone can use

✨ Author

Muhammad Bashir
Northwest University, Kano
2025 – Machine Learning Specialization

"A person is a person through other persons." – Ubuntu Philosophy


