
# Selenium Automated Login Test Script

Script ini adalah solusi otomatisasi menggunakan Selenium untuk menguji login pada halaman `https://fauzi.ukm.id/dashboard/`. Script ini memasukkan kredensial yang ditentukan, mengklik tombol login, dan memverifikasi hasil login dengan memeriksa URL setelah login.

## Prasyarat

### 1. Instalasi Python
Pastikan **Python** (versi 3.7 atau lebih baru) telah terpasang di sistem Anda. Untuk memeriksa versi Python:
```bash
python3 --version
```

### 2. Instalasi Google Chrome dan ChromeDriver
   - **Google Chrome**: Unduh dan instal Google Chrome terbaru dari [situs resmi](https://www.google.com/chrome/).
   - **ChromeDriver**: Pastikan versi ChromeDriver kompatibel dengan versi Chrome yang terpasang. Unduh dari [ChromeDriver download page](https://chromedriver.chromium.org/downloads) dan tempatkan `chromedriver` di `/usr/bin/` atau path lain yang diinginkan.

### 3. Instalasi pustaka Selenium
   - Gunakan pip untuk menginstal pustaka Selenium:
     ```bash
     pip install selenium
     ```

## Instalasi dan Menjalankan Script

1. **Clone atau Unduh Repository**
   ```bash
   git clone https://github.com/username/repo.git
   cd repo
   ```

2. **Membuat Virtual Environment (Opsional)**
   Disarankan untuk menggunakan virtual environment agar instalasi pustaka terisolasi:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # MacOS/Linux
   .\venv\Scripts\activate   # Windows
   ```

3. **Instalasi Dependensi**
   Jika menggunakan virtual environment, pastikan pustaka Selenium terinstal:
   ```bash
   pip install selenium
   ```

4. **Konfigurasi Path ChromeDriver dan Kredensial**
   - Buka `tes-login.py` dan sesuaikan path `chromedriver` dengan lokasi yang benar:
     ```python
     service = Service('/path/to/chromedriver')  # Ganti dengan path aktual
     ```
   - Masukkan kredensial login yang valid:
     ```python
     username_field.send_keys("YOUR_USERNAME")  # Ganti dengan email yang benar
     password_field.send_keys("YOUR_PASSWORD")     # Ganti dengan password yang benar
     ```

## Menjalankan Script

1. Pastikan berada di direktori yang berisi `tes-login.py`.
2. Jalankan script menggunakan:
   ```bash
   python tes-login.py
   ```

3. **Hasil Output**
   Script akan menguji login dan menampilkan:
   - "Login berhasil." jika berhasil login.
   - "Login gagal." jika kredensial salah atau login tidak berhasil.

## Opsi Konfigurasi Tambahan

- **Menonaktifkan Headless Mode**: Jika Anda ingin melihat tampilan browser saat menjalankan pengujian, hapus baris berikut:
  ```python
  options.add_argument('--headless')
  ```

- **Mengganti `user-agent`**: Anda dapat mengubah `user-agent` jika diperlukan:
  ```python
  options.add_argument('user-agent=Mozilla/5.0 ...')
  ```

## Troubleshooting

- **Versi Chrome Tidak Kompatibel**: Pastikan `chromedriver` sesuai dengan versi Chrome yang digunakan.
- **Error Permission di ChromeDriver**: Jika ada error terkait izin, jalankan:
  ```bash
  chmod +x /path/to/chromedriver
  ```

## Referensi

- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [ChromeDriver Documentation](https://chromedriver.chromium.org/)

---

Script ini membantu mengotomatisasi pengujian login untuk memudahkan verifikasi kredensial di berbagai aplikasi web.
