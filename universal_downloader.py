import tkinter as tk
from tkinter import filedialog, ttk
import json
import os
import re
import threading
import time
import requests

IMG_EXT = r'\.(jpg|jpeg|png|webp)'

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("HAR Downloader Pro 🚀")
        self.root.geometry("700x500")

        self.har_path = ""
        self.urls = []

        # Title
        self.title = tk.Label(root, text="HAR Downloader Pro", font=("Arial", 18, "bold"))
        self.title.pack(pady=10)

        # Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        self.btn_select = tk.Button(btn_frame, text="📂 Select HAR", command=self.select_file)
        self.btn_select.grid(row=0, column=0, padx=5)

        self.btn_start = tk.Button(btn_frame, text="🚀 Start", command=self.start_download)
        self.btn_start.grid(row=0, column=1, padx=5)

        self.btn_clear = tk.Button(btn_frame, text="🧹 Clear Log", command=self.clear_log)
        self.btn_clear.grid(row=0, column=2, padx=5)

        # Progress bar
        self.progress = ttk.Progressbar(root, length=500, mode='determinate')
        self.progress.pack(pady=10)

        # Status label
        self.status = tk.Label(root, text="Idle", font=("Arial", 10))
        self.status.pack()

        # Log box
        self.log = tk.Text(root, height=15)
        self.log.pack(fill="both", expand=True, padx=10, pady=10)

    def log_print(self, msg):
        self.log.insert(tk.END, msg + "\n")
        self.log.see(tk.END)

    def clear_log(self):
        self.log.delete(1.0, tk.END)

    def select_file(self):
        self.har_path = filedialog.askopenfilename(filetypes=[("HAR files", "*.har")])
        if self.har_path:
            self.log_print(f"📂 Selected: {self.har_path}")

    def extract_urls(self):
        with open(self.har_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        urls = set()

        for entry in data['log']['entries']:
            url = entry['request']['url']
            if re.search(IMG_EXT, url):
                url = url.replace("300px_", "")
                urls.add(url)

        self.urls = list(urls)

    def download(self):
        folder = os.path.splitext(os.path.basename(self.har_path))[0]
        os.makedirs(folder, exist_ok=True)

        total = len(self.urls)
        self.progress["maximum"] = total

        start_time = time.time()

        self.log_print(f"🚀 Starting download ({total} files)...")

        for i, url in enumerate(self.urls, 1):
            try:
                filename = os.path.join(folder, url.split("/")[-1])

                r = requests.get(url, headers=HEADERS, stream=True, timeout=10)

                if r.status_code == 200:
                    with open(filename, "wb") as f:
                        for chunk in r.iter_content(1024):
                            f.write(chunk)

                    self.log_print(f"[{i}/{total}] ✅ {os.path.basename(filename)}")
                else:
                    self.log_print(f"[{i}/{total}] ❌ Failed")

                # Progress update
                self.progress["value"] = i

                elapsed = time.time() - start_time
                speed = i / elapsed if elapsed > 0 else 0
                remaining = (total - i) / speed if speed > 0 else 0

                self.status.config(
                    text=f"{i}/{total} | ETA: {int(remaining)} sec"
                )

                self.root.update_idletasks()

            except Exception as e:
                self.log_print(f"[{i}/{total}] ⚠️ Error: {e}")

        self.status.config(text="✅ Completed!")
        self.log_print("🎉 All downloads completed!")

    def start_download(self):
        if not self.har_path:
            self.log_print("❌ Please select a HAR file first")
            return

        self.extract_urls()
        threading.Thread(target=self.download).start()


root = tk.Tk()
app = App(root)
root.mainloop()
