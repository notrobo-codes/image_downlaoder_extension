# 🖼️ Image Downloader Tool

A powerful Python-based image downloader that extracts and downloads images from websites using the HAR (HTTP Archive) method. This approach allows the tool to capture image URLs directly from network requests, making it effective even for websites that dynamically load content.

## 🚀 Features

- Download images from HAR files
- Supports dynamically loaded images
- Fast and efficient downloading
- Automatic image naming
- Creates organized download folders
- Handles multiple image formats
  - JPG / JPEG
  - PNG
  - WEBP
  - GIF
  - SVG
- Simple command-line interface
- Lightweight and easy to use

## 📋 Requirements

- Python 3.8+
- Required Python libraries

Install dependencies:

```bash
pip install -r requirements.txt
```

## 📂 Project Structure

```text
Image-Downloader/
│
├── main.py
├── requirements.txt
└── README.md
```

## ⚙️ How It Works

1. Open the target website in your browser.
2. Open Developer Tools (`F12`).
3. Navigate to the **Network** tab.
4. Reload the page.
5. Export network activity as a **HAR file**.
6. Place the HAR file inside the project directory.
7. Run the script.
8. The tool extracts image URLs from the HAR file and downloads them automatically.

## 🛠 Usage

Run the program:

```bash
python main.py
```

When prompted, provide:

```text
Enter HAR file path:
```

Example:

```text
har_files/example.har
```

Downloaded images will be saved inside:

```text
home/username/
```

## 📸 Supported Sources

This tool can download images from:

- Static websites
- Dynamic websites
- Image galleries
- Content delivery networks (CDNs)
- Websites using AJAX requests

## 🔒 Disclaimer

This tool is intended for educational and personal use only.

Please respect:
- Website Terms of Service
- Copyright laws
- Privacy policies

Only download content that you have permission to access.

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Add new feature"
```

4. Push to GitHub

```bash
git push origin feature-name
```

5. Open a Pull Request

## ⭐ Future Improvements

- GUI version
- Multi-threaded downloading
- Resume interrupted downloads
- Duplicate image detection
- Image filtering by size/type
- Progress bar support

## 📜 License

This project is licensed under the MIT License.

---





Made with ❤️ using Python.

