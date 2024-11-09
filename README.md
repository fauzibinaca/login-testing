Selenium Login Test Script

Script ini menggunakan Selenium untuk mengotomatisasi pengujian login ke halaman https://fauzi.ukm.id/dashboard/. Script akan memasukkan kredensial yang diberikan dan memverifikasi apakah login berhasil dengan memeriksa URL yang diakses setelah login.
Persyaratan

Sebelum menjalankan script ini, pastikan Anda telah menginstal:

    Python (direkomendasikan versi 3.7 atau lebih baru)
    Google Chrome Browser
    ChromeDriver yang kompatibel dengan versi Google Chrome yang terinstal.

Langkah Instalasi

    Kloning atau Unduh Repository
    Kloning repository ini atau unduh file .py script.

    Buat Virtual Environment (Opsional tetapi Direkomendasikan)

python3 -m venv venv
source venv/bin/activate  # Untuk MacOS/Linux
.\venv\Scripts\activate   # Untuk Windows

Instalasi Dependensi
Pastikan Anda menginstal Selenium dan dependensi lainnya dengan menjalankan perintah berikut:

    pip install selenium

    Download ChromeDriver
    Download ChromeDriver yang kompatibel dengan versi Chrome Anda di tautan ini.
        Ekstrak file chromedriver dan letakkan di direktori yang diinginkan.
        Perbarui variabel service = Service('/path/to/chromedriver') pada script sesuai lokasi path chromedriver.

Menjalankan Script

    Buka Script Pastikan Anda telah membuka terminal atau command prompt pada folder yang berisi script ini.

    Sesuaikan Kredensial Login Buka script dan ganti:
        username_field.send_keys("23.ozzie@gmail.com") - Masukkan username Anda.
        password_field.send_keys("v*&cb7?~4*kWp,)") - Masukkan password Anda.

    Jalankan Script Jalankan perintah berikut:

    python tes-login.py

    Output Script akan menampilkan apakah login berhasil atau tidak berdasarkan URL setelah proses login.

Pengaturan Konfigurasi (Opsional)
Menyesuaikan Lokasi ChromeDriver

Jika chromedriver berada di lokasi lain, sesuaikan path di baris berikut:

service = Service('/path/to/chromedriver')

Menambahkan Opsi Tambahan

Anda dapat mengaktifkan atau menonaktifkan opsi di Selenium sesuai kebutuhan. Contoh, untuk menjalankan dengan UI (non-headless), hapus atau komentari options.add_argument('--headless').
Debugging

Jika mengalami masalah, pastikan:

    Chrome dan chromedriver versi kompatibel.
    Semua dependensi telah diinstal.
    Gunakan command pip install -r requirements.txt untuk memastikan semua paket terinstal.
