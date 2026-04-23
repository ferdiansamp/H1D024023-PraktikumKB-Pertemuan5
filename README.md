# H1D024023-PraktikumKB-Pertemuan5

# 👂 Sistem Pakar Diagnosa Penyakit THT (Forward Chaining)

Aplikasi berbasis Desktop yang dirancang untuk mendiagnosa berbagai jenis penyakit pada **Telinga, Hidung, dan Tenggorokan (THT)**. Sistem ini memberikan hasil diagnosa berdasarkan gejala-gejala yang diinputkan oleh pengguna melalui antarmuka grafis (GUI) yang interaktif.

---

## 🚀 Fitur Utama
- **Basis Pengetahuan Luas**: Mencakup **37 Gejala** medis dan **22 Jenis Penyakit** THT (mulai dari Tonsilitis hingga berbagai jenis Kanker THT).
- **Inference Engine**: Menggunakan pencocokan pola gejala dengan ambang batas (*threshold*) untuk menentukan tingkat keyakinan diagnosa.
- **UI Modern (Dark Mode)**: Antarmuka menggunakan tema gelap yang elegan dengan *progress bar* dan kartu hasil yang informatif.
- **Navigasi Fleksibel**: Dilengkapi fitur "Kembali" (*Undo*) untuk memperbaiki jawaban jika terjadi kesalahan input.
- **Saran Medis**: Setiap hasil diagnosa dilengkapi dengan solusi dan langkah penanganan awal yang komprehensif.

---

## 🛠️ Teknologi yang Digunakan
- **Bahasa Pemrograman**: Python 3.x
- **Library GUI**: `tkinter` (Standard Python Interface)
- **Metode**: Forward Chaining (Dictionary-based Inference)

---

## 📂 Struktur Kode (12 Fungsi Utama)

Kode ini dikelola secara modular di dalam kelas `SistemPakarTHT` dengan pembagian fungsi sebagai berikut:

### 🎨 Antarmuka & Visual (Front-end)
1.  **`__init__`**: Menginisialisasi jendela utama, mengatur judul, dimensi, dan konfigurasi dasar aplikasi.
2.  **`_setup_fonts`**: Mengatur seluruh tipografi aplikasi agar konsisten menggunakan font monospaced (Consolas).
3.  **`_build_layout`**: Membuat kerangka dasar (Header, Garis Aksen, dan Body) yang bersifat permanen.
4.  **`_clear`**: Membersihkan elemen di dalam container utama untuk memfasilitasi transisi antar halaman.
5.  **`_show_welcome`**: Menampilkan halaman selamat datang beserta statistik singkat sistem (37 Gejala/22 Penyakit).
6.  **`_show_question`**: Mengelola tampilan pertanyaan dinamis, badge kode gejala (G1-G37), dan progress bar.
7.  **`_show_result`**: Merender halaman akhir yang menampilkan daftar penyakit yang terdeteksi dalam kartu visual.
8.  **`_btn`**: Fungsi helper (pabrik tombol) untuk membuat tombol seragam dengan efek *hover*.

### 🧠 Logika & Data (Back-end)
9.  **`_start`**: Menyetel ulang (*reset*) variabel state (gejala terpilih dan indeks pertanyaan) sebelum memulai diagnosa baru.
10. **`_jawab`**: Menyimpan kode gejala ke dalam list jika pengguna menjawab "YA" dan melompat ke pertanyaan berikutnya.
11. **`_back`**: Menghapus catatan gejala terakhir dan memundurkan urutan pertanyaan (Fitur Koreksi).
12. **`_proses_hasil`**: Inti logika sistem; menghitung skor kecocokan gejala per penyakit dan membandingkannya dengan *threshold* setiap penyakit.

---

## 📊 Mesin Inferensi
Sistem bekerja dengan membandingkan input pengguna terhadap `database_penyakit`. 
- **Skoring**: Setiap kecocokan gejala bernilai 1 poin.
- **Threshold**: Penyakit hanya akan ditampilkan jika jumlah gejala yang cocok ≥ ambang batas minimal yang ditetapkan untuk penyakit tersebut.
- **Sorting**: Hasil akhir diurutkan berdasarkan persentase kecocokan tertinggi (Skor/Total Gejala).

---

## ⚙️ Cara Menjalankan
1. Pastikan Python 3.x sudah terpasang.
2. Simpan kode ke dalam file bernama `tugas5.py`.
3. Jalankan melalui terminal/CMD:
   ```bash
   python tugas5.py
