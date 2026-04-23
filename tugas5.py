import tkinter as tk
from tkinter import ttk, font as tkFont

# ══════════════════════════════════════════════════════════════════════════════
#  TEMA WARNA
# ══════════════════════════════════════════════════════════════════════════════
BG_DARK   = "#0d1117"
BG_CARD   = "#161b27"
BG_PANEL  = "#111520"
ACCENT    = "#00b4d8"
ACCENT2   = "#48cae4"
SUCCESS   = "#2ec97e"
WARNING   = "#f4a261"
DANGER    = "#e63946"
TEXT_MAIN = "#e0e8ff"
TEXT_DIM  = "#6b7a9e"
BTN_YES   = "#2ec97e"
BTN_NO    = "#e63946"
BORDER    = "#1f2a42"

# ══════════════════════════════════════════════════════════════════════════════
#  KNOWLEDGE BASE — GEJALA
# ══════════════════════════════════════════════════════════════════════════════
semua_gejala = {
    "G1":  "Nafas abnormal",
    "G2":  "Suara serak",
    "G3":  "Perubahan kulit",
    "G4":  "Telinga penuh",
    "G5":  "Nyeri bicara / menelan",
    "G6":  "Nyeri tenggorokan",
    "G7":  "Nyeri leher",
    "G8":  "Pendarahan hidung",
    "G9":  "Telinga berdenging",
    "G10": "Air liur menetes",
    "G11": "Perubahan suara",
    "G12": "Sakit kepala",
    "G13": "Nyeri pinggir hidung",
    "G14": "Serangan vertigo",
    "G15": "Getah bening membesar",
    "G16": "Leher bengkak",
    "G17": "Hidung tersumbat",
    "G18": "Infeksi sinus",
    "G19": "Berat badan turun",
    "G20": "Nyeri telinga",
    "G21": "Selaput lendir merah",
    "G22": "Benjolan di leher",
    "G23": "Tubuh tak seimbang",
    "G24": "Bola mata bergerak (Nystagmus)",
    "G25": "Nyeri wajah",
    "G26": "Dahi sakit",
    "G27": "Batuk",
    "G28": "Tumbuh di mulut",
    "G29": "Benjolan di leher",
    "G30": "Nyeri antara mata",
    "G31": "Radang gendang telinga",
    "G32": "Tenggorokan gatal",
    "G33": "Hidung meler",
    "G34": "Tuli",
    "G35": "Mual / muntah",
    "G36": "Letih / lesu",
    "G37": "Demam",
}

# ══════════════════════════════════════════════════════════════════════════════
#  KNOWLEDGE BASE — PENYAKIT + SOLUSI
# ══════════════════════════════════════════════════════════════════════════════
database_penyakit = {
    "Tonsilitis": {
        "gejala":    ["G37","G12","G5","G27","G6","G21"],
        "threshold": 3,
        "warna":     "#e63946",
        "ikon":      "🦠",
        "solusi": (
            "• Istirahat yang cukup & perbanyak minum air hangat\n"
            "• Kumur dengan air garam hangat (1 sdt garam + 240 ml air)\n"
            "• Konsumsi obat pereda nyeri (parasetamol / ibuprofen)\n"
            "• Antibiotik jika disebabkan bakteri (konsultasi dokter)\n"
            "• Tonsilektomi jika terjadi berulang kali (>7x/tahun)"
        ),
    },
    "Sinusitis Maksilaris": {
        "gejala":    ["G37","G12","G27","G17","G33","G36","G29"],
        "threshold": 4,
        "warna":     "#f4a261",
        "ikon":      "🤧",
        "solusi": (
            "• Inhalasi uap air hangat untuk melapangkan sinus\n"
            "• Irigasi hidung dengan larutan salin (Nasal Rinse)\n"
            "• Dekongestan nasal semprotan (maks. 3 hari pemakaian)\n"
            "• Antibiotik jika infeksi bakteri, minimal 10–14 hari\n"
            "• Konsultasikan ke dokter THT untuk tindak lanjut"
        ),
    },
    "Sinusitis Frontalis": {
        "gejala":    ["G37","G12","G27","G17","G33","G36","G21","G26"],
        "threshold": 4,
        "warna":     "#f4a261",
        "ikon":      "🤧",
        "solusi": (
            "• Kompres hangat di daerah dahi untuk meredakan nyeri\n"
            "• Inhalasi uap & irigasi hidung secara rutin\n"
            "• Obat dekongestan dan antihistamin sesuai anjuran\n"
            "• Antibiotik bila diperlukan (resep dokter)\n"
            "• Tindakan operasi FESS jika pengobatan tidak berhasil"
        ),
    },
    "Sinusitis Etmoidalis": {
        "gejala":    ["G37","G12","G27","G17","G33","G36","G21","G30","G13","G26"],
        "threshold": 5,
        "warna":     "#f4a261",
        "ikon":      "🤧",
        "solusi": (
            "• Kompres hangat di sekitar hidung dan mata\n"
            "• Irigasi hidung intensif dengan larutan salin\n"
            "• Antibiotik spektrum luas (konsultasi dokter)\n"
            "• Hindari paparan alergen dan polusi udara\n"
            "• Evaluasi CT Scan sinus bila gejala persisten"
        ),
    },
    "Sinusitis Sfenoidalis": {
        "gejala":    ["G37","G12","G27","G17","G33","G36","G29","G7"],
        "threshold": 4,
        "warna":     "#f4a261",
        "ikon":      "🤧",
        "solusi": (
            "• Periksakan diri ke dokter THT segera\n"
            "• Terapi antibiotik intravena jika infeksi berat\n"
            "• Irigasi sinus dengan alat khusus oleh tenaga medis\n"
            "• Tindakan bedah endoskopik bila medikamentosa gagal\n"
            "• Hindari aktivitas yang memperburuk tekanan kepala"
        ),
    },
    "Abses Peritonsiler": {
        "gejala":    ["G37","G12","G6","G15","G2","G29","G10"],
        "threshold": 3,
        "warna":     DANGER,
        "ikon":      "⚠️",
        "solusi": (
            "• Segera ke IGD / dokter THT — kondisi darurat medis\n"
            "• Insisi dan drainase abses oleh dokter\n"
            "• Antibiotik IV dosis tinggi di rumah sakit\n"
            "• Kumur antiseptik setelah drainase\n"
            "• Pertimbangkan tonsilektomi setelah infeksi mereda"
        ),
    },
    "Faringitis": {
        "gejala":    ["G37","G5","G6","G7","G15"],
        "threshold": 3,
        "warna":     "#e76f51",
        "ikon":      "🔴",
        "solusi": (
            "• Perbanyak minum cairan hangat (teh madu, air garam)\n"
            "• Hindari makanan pedas, asam, dan minuman dingin\n"
            "• Lozenges / obat tenggorokan untuk meredakan nyeri\n"
            "• Antibiotik jika etiologi bakteri Streptococcus\n"
            "• Istirahat bicara jika nyeri parah"
        ),
    },
    "Kanker Laring": {
        "gejala":    ["G5","G27","G6","G15","G2","G19","G1"],
        "threshold": 3,
        "warna":     "#c1121f",
        "ikon":      "🚨",
        "solusi": (
            "• Segera konsultasi ke dokter spesialis onkologi THT\n"
            "• Biopsi laring untuk konfirmasi diagnosis\n"
            "• Pilihan terapi: radioterapi, kemoterapi, atau operasi\n"
            "• Hentikan merokok dan konsumsi alkohol\n"
            "• Dukungan psikologis dan gizi selama pengobatan"
        ),
    },
    "Deviasi Septum": {
        "gejala":    ["G37","G17","G20","G8","G18","G25"],
        "threshold": 3,
        "warna":     "#457b9d",
        "ikon":      "👃",
        "solusi": (
            "• Dekongestan nasal dan spray kortikosteroid hidung\n"
            "• Irigasi hidung salin untuk menjaga kelembapan\n"
            "• Tidur dengan posisi kepala sedikit lebih tinggi\n"
            "• Septoplasti (operasi koreksi) jika gangguan parah\n"
            "• Konsultasi dokter THT untuk evaluasi endoskopi"
        ),
    },
    "Laringitis": {
        "gejala":    ["G37","G5","G15","G16","G32"],
        "threshold": 3,
        "warna":     "#2a9d8f",
        "ikon":      "🗣️",
        "solusi": (
            "• Istirahat suara total selama 2–3 hari\n"
            "• Hidrasi maksimal, hindari kafein dan alkohol\n"
            "• Inhalasi uap hangat untuk melembapkan laring\n"
            "• Obat anti-inflamasi untuk mengurangi pembengkakan\n"
            "• Hindari berbisik (membebani pita suara lebih berat)"
        ),
    },
    "Kanker Leher & Kepala": {
        "gejala":    ["G5","G22","G8","G28","G3","G11"],
        "threshold": 3,
        "warna":     "#c1121f",
        "ikon":      "🚨",
        "solusi": (
            "• Segera konsultasi onkologi / THT untuk biopsi\n"
            "• Pemeriksaan PET Scan atau MRI untuk staging\n"
            "• Terapi multimodal: operasi + radioterapi/kemoterapi\n"
            "• Hentikan kebiasaan merokok, kunyah sirih\n"
            "• Rehabilitasi menelan dan wicara pasca-terapi"
        ),
    },
    "Otitis Media Akut": {
        "gejala":    ["G37","G20","G35","G31"],
        "threshold": 3,
        "warna":     "#e9c46a",
        "ikon":      "👂",
        "solusi": (
            "• Antibiotik amoksisilin selama 7–10 hari\n"
            "• Obat pereda nyeri telinga (tetes/oral)\n"
            "• Kompres hangat di sekitar telinga\n"
            "• Hindari menyelam dan memasukkan air ke telinga\n"
            "• Evaluasi ulang ke dokter jika tidak membaik dalam 72 jam"
        ),
    },
    "Contact Ulcers": {
        "gejala":    ["G5","G2"],
        "threshold": 2,
        "warna":     "#a8dadc",
        "ikon":      "🎙️",
        "solusi": (
            "• Istirahat total dari penggunaan suara\n"
            "• Terapi suara / voice therapy dengan ahli patologi wicara\n"
            "• Hindari refluks asam: jangan makan larut malam\n"
            "• Obat antasida / PPI jika ada GERD\n"
            "• Hindari berdehem keras berulang kali"
        ),
    },
    "Abses Parafaringeal": {
        "gejala":    ["G5","G16"],
        "threshold": 2,
        "warna":     DANGER,
        "ikon":      "⚠️",
        "solusi": (
            "• Kondisi darurat — segera ke RS / IGD\n"
            "• Drainase bedah oleh dokter THT\n"
            "• Antibiotik intravena dosis tinggi\n"
            "• Pemantauan airway ketat (risiko obstruksi napas)\n"
            "• Rawat inap hingga kondisi stabil"
        ),
    },
    "Barotitis Media": {
        "gejala":    ["G12","G20"],
        "threshold": 2,
        "warna":     "#48cae4",
        "ikon":      "✈️",
        "solusi": (
            "• Lakukan manuver Valsalva (tutup hidung, hembuskan perlahan)\n"
            "• Mengunyah permen karet saat naik/turun pesawat\n"
            "• Dekongestan nasal 30 menit sebelum penerbangan\n"
            "• Hindari menyelam jika ada infeksi saluran napas atas\n"
            "• Konsultasi THT jika nyeri berlanjut >24 jam"
        ),
    },
    "Kanker Nasofaring": {
        "gejala":    ["G17","G8"],
        "threshold": 2,
        "warna":     "#c1121f",
        "ikon":      "🚨",
        "solusi": (
            "• Pemeriksaan nasofaringoskopi dan biopsi segera\n"
            "• Cek titer EBV (virus Epstein-Barr) sebagai penanda\n"
            "• Radioterapi sebagai terapi utama\n"
            "• Kemoterapi kombinasi untuk stadium lanjut\n"
            "• Deteksi dini sangat menentukan prognosis"
        ),
    },
    "Kanker Tonsil": {
        "gejala":    ["G6","G29"],
        "threshold": 2,
        "warna":     "#c1121f",
        "ikon":      "🚨",
        "solusi": (
            "• Konsultasi segera ke dokter onkologi THT\n"
            "• Biopsi untuk konfirmasi jenis kanker\n"
            "• Terapi: operasi + radioterapi / kemoradiasi\n"
            "• Vaksinasi HPV sebagai pencegahan\n"
            "• Pemantauan berkala setelah terapi"
        ),
    },
    "Neuronitis Vestibularis": {
        "gejala":    ["G35","G24"],
        "threshold": 2,
        "warna":     "#9b72cf",
        "ikon":      "🌀",
        "solusi": (
            "• Istirahat total di tempat tidur saat serangan akut\n"
            "• Obat antivertigo (betahistin, dimenhidrinat)\n"
            "• Kortikosteroid untuk mempercepat pemulihan\n"
            "• Vestibular rehabilitation exercise setelah akut\n"
            "• Hindari perubahan posisi kepala yang tiba-tiba"
        ),
    },
    "Meniere": {
        "gejala":    ["G20","G35","G14","G4"],
        "threshold": 3,
        "warna":     "#9b72cf",
        "ikon":      "🌀",
        "solusi": (
            "• Diet rendah garam (< 2000 mg natrium/hari)\n"
            "• Kurangi kafein, alkohol, dan nikotin\n"
            "• Diuretik untuk mengurangi cairan endolimfe\n"
            "• Betahistin untuk memperbaiki mikrosirkulasi\n"
            "• Terapi vestibular rehabilitasi jangka panjang"
        ),
    },
    "Tumor Saraf Pendengaran": {
        "gejala":    ["G12","G34","G23"],
        "threshold": 2,
        "warna":     "#c77dff",
        "ikon":      "🧠",
        "solusi": (
            "• MRI otak dengan kontras untuk konfirmasi diagnosis\n"
            "• Konsultasi ke neurotologi / bedah saraf\n"
            "• Pilihan: observasi, radiosurgery (Gamma Knife), operasi\n"
            "• Audiometri berkala untuk memantau pendengaran\n"
            "• Rehabilitasi keseimbangan pasca-terapi"
        ),
    },
    "Kanker Leher Metastatik": {
        "gejala":    ["G29"],
        "threshold": 1,
        "warna":     "#c1121f",
        "ikon":      "🚨",
        "solusi": (
            "• Segera biopsi benjolan untuk menentukan asal kanker\n"
            "• CT Scan leher-dada-abdomen untuk cari tumor primer\n"
            "• Terapi sesuai tumor primer yang ditemukan\n"
            "• Diseksi leher jika diperlukan\n"
            "• Konsultasi multidisiplin (THT, Onkologi, Radiologi)"
        ),
    },
    "Otosklerosis": {
        "gejala":    ["G34","G9"],
        "threshold": 2,
        "warna":     "#e9c46a",
        "ikon":      "👂",
        "solusi": (
            "• Audiometri dan timpanometri untuk konfirmasi\n"
            "• Alat bantu dengar sebagai pilihan konservatif\n"
            "• Operasi stapedektomi/stapedotomi untuk hasil terbaik\n"
            "• Suplemen fluorida (masih kontroversial, konsultasikan)\n"
            "• Hindari paparan kebisingan berlebihan"
        ),
    },
    "Vertigo Postural": {
        "gejala":    ["G24"],
        "threshold": 1,
        "warna":     "#9b72cf",
        "ikon":      "🌀",
        "solusi": (
            "• Lakukan manuver Epley untuk mengatasi BPPV\n"
            "• Hindari posisi kepala yang memicu vertigo\n"
            "• Latihan Brandt-Daroff secara rutin di rumah\n"
            "• Obat antivertigo sementara saat serangan akut\n"
            "• Konsultasi THT jika manuver tidak berhasil"
        ),
    },
}

# Urutan gejala yang ditanyakan (G1 s/d G37)
urutan_gejala = [f"G{i}" for i in range(1, 38)]


# ══════════════════════════════════════════════════════════════════════════════
#  KELAS APLIKASI
# ══════════════════════════════════════════════════════════════════════════════
class SistemPakarTHT:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pakar — Diagnosa Penyakit THT")
        self.root.geometry("660x540")
        self.root.configure(bg=BG_DARK)
        self.root.resizable(False, False)

        self.gejala_terpilih = []
        self.index_q = 0

        self._setup_fonts()
        self._build_layout()
        self._show_welcome()

    # ─── Font ──────────────────────────────────────────────
    def _setup_fonts(self):
        fam = "Consolas"
        self.f_title  = tkFont.Font(family=fam, size=12, weight="bold")
        self.f_sub    = tkFont.Font(family=fam, size=8)
        self.f_q      = tkFont.Font(family=fam, size=10, weight="bold")
        self.f_btn    = tkFont.Font(family=fam, size=10, weight="bold")
        self.f_small  = tkFont.Font(family=fam, size=8)
        self.f_res    = tkFont.Font(family=fam, size=10, weight="bold")
        self.f_sol    = tkFont.Font(family=fam, size=8)
        self.f_big    = tkFont.Font(family=fam, size=32, weight="bold")
        self.f_kode   = tkFont.Font(family=fam, size=8, weight="bold")

    # ─── Layout kerangka ───────────────────────────────────
    def _build_layout(self):
        # Header
        hdr = tk.Frame(self.root, bg=BG_PANEL, pady=10)
        hdr.pack(fill=tk.X)
        tk.Label(hdr, text="█ SISTEM PAKAR PENYAKIT THT",
                 font=self.f_title, bg=BG_PANEL, fg=ACCENT).pack()
        tk.Label(hdr,
                 text="Telinga · Hidung · Tenggorokan  |  22 Penyakit · 37 Gejala",
                 font=self.f_small, bg=BG_PANEL, fg=TEXT_DIM).pack(pady=(1,0))

        # Garis aksen cyan
        tk.Frame(self.root, bg=ACCENT, height=2).pack(fill=tk.X)

        # Body
        self.frame_body = tk.Frame(self.root, bg=BG_DARK)
        self.frame_body.pack(fill=tk.BOTH, expand=True, padx=26, pady=16)

    def _clear(self):
        for w in self.frame_body.winfo_children():
            w.destroy()

    # ══════════════════════════════════════════════════════
    #  HALAMAN WELCOME
    # ══════════════════════════════════════════════════════
    def _show_welcome(self):
        self._clear()

        tk.Label(self.frame_body, text="THT",
                 font=self.f_big, bg=BG_DARK, fg=ACCENT).pack(pady=(6,2))
        tk.Label(self.frame_body, text="Selamat Datang!",
                 font=self.f_res, bg=BG_DARK, fg=TEXT_MAIN).pack()
        tk.Label(self.frame_body,
                 text="Jawab pertanyaan berikut dengan YA atau TIDAK.\n"
                      "Sistem akan mendiagnosa kemungkinan penyakit THT Anda.",
                 font=self.f_sub, bg=BG_DARK, fg=TEXT_DIM,
                 justify=tk.CENTER).pack(pady=(6,14))

        # Statistik
        info = tk.Frame(self.frame_body, bg=BG_CARD, padx=14, pady=10)
        info.pack(fill=tk.X, pady=(0,18))
        for val, lbl in [("37","Gejala"), ("22","Penyakit"), ("AI","Inferensi")]:
            col = tk.Frame(info, bg=BG_CARD)
            col.pack(side=tk.LEFT, expand=True)
            tk.Label(col, text=val,
                     font=tkFont.Font(family="Consolas", size=16, weight="bold"),
                     bg=BG_CARD, fg=ACCENT).pack()
            tk.Label(col, text=lbl,
                     font=self.f_small, bg=BG_CARD, fg=TEXT_DIM).pack()

        self._btn(self.frame_body, "▶  MULAI DIAGNOSA", ACCENT, ACCENT2,
                  self._start)

    # ══════════════════════════════════════════════════════
    #  HALAMAN PERTANYAAN
    # ══════════════════════════════════════════════════════
    def _start(self):
        self.gejala_terpilih = []
        self.index_q = 0
        self._show_question()

    def _show_question(self):
        self._clear()

        if self.index_q >= len(urutan_gejala):
            self._proses_hasil()
            return

        kode = urutan_gejala[self.index_q]
        teks = semua_gejala[kode]
        no   = self.index_q + 1
        tot  = len(urutan_gejala)
        pct  = no / tot

        # Progress
        tk.Label(self.frame_body,
                 text=f"Pertanyaan {no} / {tot}  |  {len(self.gejala_terpilih)} gejala dicatat",
                 font=self.f_small, bg=BG_DARK, fg=TEXT_DIM).pack(anchor=tk.W)

        bar_bg = tk.Frame(self.frame_body, bg=BG_CARD, height=5)
        bar_bg.pack(fill=tk.X, pady=(2,10))
        bar_bg.pack_propagate(False)
        tk.Frame(bar_bg, bg=ACCENT, height=5).place(
            relx=0, rely=0, relwidth=pct, relheight=1)

        # Kartu pertanyaan
        card = tk.Frame(self.frame_body, bg=BG_CARD, padx=20, pady=18)
        card.pack(fill=tk.X)

        # Badge kode gejala
        badge = tk.Label(card, text=f"  {kode}  ",
                         font=self.f_kode, bg=ACCENT, fg=BG_DARK,
                         padx=4, pady=2)
        badge.pack(anchor=tk.CENTER, pady=(0,8))

        tk.Label(card, text=teks,
                 font=self.f_q, bg=BG_CARD, fg=TEXT_MAIN,
                 wraplength=500, justify=tk.CENTER).pack(pady=(0,4))

        tk.Label(card,
                 text="Apakah Anda mengalami gejala ini?",
                 font=self.f_small, bg=BG_CARD, fg=TEXT_DIM).pack()

        # Tombol
        row = tk.Frame(self.frame_body, bg=BG_DARK)
        row.pack(pady=12)
        self._btn(row, "✓   YA",    BTN_YES, "#28d98c",
                  lambda: self._jawab(True),  side=tk.LEFT, px=12)
        self._btn(row, "✗   TIDAK", BTN_NO,  "#f05870",
                  lambda: self._jawab(False), side=tk.LEFT, px=12)

        # Tombol kembali
        if self.index_q > 0:
            self._btn(self.frame_body, "← Kembali", BG_CARD, BG_PANEL,
                      self._back, fg=TEXT_DIM)

        # Daftar gejala yang sudah ya (mini)
        if self.gejala_terpilih:
            info_frame = tk.Frame(self.frame_body, bg=BG_DARK)
            info_frame.pack(fill=tk.X, pady=(4,0))
            teks_gejala = "  ✓ " + "  ✓ ".join(self.gejala_terpilih)
            tk.Label(info_frame, text=teks_gejala,
                     font=self.f_small, bg=BG_DARK, fg=SUCCESS,
                     wraplength=600, justify=tk.LEFT).pack(anchor=tk.W)

    def _jawab(self, ya: bool):
        if ya:
            self.gejala_terpilih.append(urutan_gejala[self.index_q])
        self.index_q += 1
        self._show_question()

    def _back(self):
        if self.index_q > 0:
            kode_prev = urutan_gejala[self.index_q - 1]
            if kode_prev in self.gejala_terpilih:
                self.gejala_terpilih.remove(kode_prev)
            self.index_q -= 1
            self._show_question()

    # ══════════════════════════════════════════════════════
    #  MESIN INFERENSI (Dictionary-based)
    # ══════════════════════════════════════════════════════
    def _proses_hasil(self):
        """
        Mesin inferensi berbasis Dictionary:
        - Hitung jumlah gejala yang cocok per penyakit
        - Tampilkan penyakit jika cocok >= threshold
        - Urutkan berdasarkan skor tertinggi
        """
        hasil = []
        for nama, data in database_penyakit.items():
            cocok = [g for g in data["gejala"] if g in self.gejala_terpilih]
            skor  = len(cocok)
            if skor >= data["threshold"]:
                hasil.append({
                    "nama":      nama,
                    "skor":      skor,
                    "total":     len(data["gejala"]),
                    "cocok_kode": cocok,
                    "solusi":    data["solusi"],
                    "warna":     data["warna"],
                    "ikon":      data["ikon"],
                })
        hasil.sort(key=lambda x: x["skor"] / x["total"], reverse=True)
        self._show_result(hasil)

    # ══════════════════════════════════════════════════════
    #  HALAMAN HASIL
    # ══════════════════════════════════════════════════════
    def _show_result(self, hasil):
        self._clear()

        # Canvas scrollable
        canvas = tk.Canvas(self.frame_body, bg=BG_DARK, highlightthickness=0)
        sb = ttk.Scrollbar(self.frame_body, orient="vertical",
                           command=canvas.yview)
        inner = tk.Frame(canvas, bg=BG_DARK)

        inner.bind("<Configure>",
                   lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=inner, anchor="nw")
        canvas.configure(yscrollcommand=sb.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        sb.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.bind_all("<MouseWheel>",
            lambda e: canvas.yview_scroll(-1*(e.delta//120), "units"))

        # ── Ringkasan gejala ──
        tk.Label(inner,
                 text=f"Gejala yang dilaporkan: {len(self.gejala_terpilih)} / {len(urutan_gejala)}",
                 font=self.f_small, bg=BG_DARK, fg=TEXT_DIM).pack(anchor=tk.W)
        if self.gejala_terpilih:
            baris = "  ".join(
                [f"[{k}] {semua_gejala[k]}" for k in self.gejala_terpilih]
            )
            tk.Label(inner, text=baris,
                     font=self.f_small, bg=BG_DARK, fg=ACCENT2,
                     wraplength=600, justify=tk.LEFT).pack(anchor=tk.W, pady=(0,8))

        tk.Frame(inner, bg=ACCENT, height=1).pack(fill=tk.X, pady=(0,8))

        # ── Hasil ──
        if not hasil:
            tk.Label(inner, text="[ OK ]",
                     font=tkFont.Font(family="Consolas", size=26, weight="bold"),
                     bg=BG_DARK, fg=SUCCESS).pack(pady=(8,2))
            tk.Label(inner, text="Tidak Ada Penyakit THT Terdeteksi",
                     font=self.f_res, bg=BG_DARK, fg=SUCCESS).pack()
            tk.Label(inner,
                     text="Tidak ditemukan pola penyakit yang signifikan\n"
                          "dari gejala yang Anda laporkan.\n\n"
                          "Saran: Lakukan pemeriksaan rutin ke dokter THT.",
                     font=self.f_sub, bg=BG_DARK, fg=TEXT_DIM,
                     justify=tk.CENTER).pack(pady=12)
        else:
            tk.Label(inner,
                     text=f"⚠  {len(hasil)} Kemungkinan Penyakit Ditemukan",
                     font=self.f_res, bg=BG_DARK, fg=WARNING).pack(pady=(0,8))

            for item in hasil:
                pct_val = int(item["skor"] / item["total"] * 100)

                card = tk.Frame(inner, bg=BG_CARD, padx=14, pady=10)
                card.pack(fill=tk.X, pady=4, padx=2)

                # Header: ikon + nama + skor
                hdr_c = tk.Frame(card, bg=BG_CARD)
                hdr_c.pack(fill=tk.X)
                tk.Label(hdr_c,
                         text=f"{item['ikon']}  {item['nama']}",
                         font=self.f_res, bg=BG_CARD,
                         fg=item["warna"]).pack(side=tk.LEFT)
                tk.Label(hdr_c,
                         text=f"Cocok: {item['skor']}/{item['total']} ({pct_val}%)",
                         font=self.f_small, bg=BG_CARD,
                         fg=TEXT_DIM).pack(side=tk.RIGHT)

                # Progress kecocokan
                pb_bg = tk.Frame(card, bg=BG_PANEL, height=4)
                pb_bg.pack(fill=tk.X, pady=(3,6))
                pb_bg.pack_propagate(False)
                tk.Frame(pb_bg, bg=item["warna"], height=4).place(
                    relx=0, rely=0, relwidth=item["skor"]/item["total"],
                    relheight=1)

                # Kode gejala yang cocok
                kode_str = "  ".join(item["cocok_kode"])
                tk.Label(card,
                         text=f"Gejala cocok: {kode_str}",
                         font=self.f_small, bg=BG_CARD, fg=ACCENT2,
                         anchor=tk.W).pack(fill=tk.X, pady=(0,4))

                # Solusi
                tk.Label(card, text="💡 SOLUSI & PENANGANAN:",
                         font=tkFont.Font(family="Consolas", size=8, weight="bold"),
                         bg=BG_CARD, fg=TEXT_MAIN, anchor=tk.W).pack(fill=tk.X)
                tk.Label(card, text=item["solusi"],
                         font=self.f_sol, bg=BG_CARD, fg=TEXT_DIM,
                         justify=tk.LEFT, anchor=tk.W).pack(fill=tk.X, pady=(2,0))

        tk.Frame(inner, bg=BG_DARK, height=6).pack()
        self._btn(inner, "↺  DIAGNOSA ULANG", ACCENT, ACCENT2,
                  self._show_welcome)
        tk.Frame(inner, bg=BG_DARK, height=14).pack()

    # ─── Helper tombol ─────────────────────────────────────
    def _btn(self, parent, text, bg, hover_bg, cmd,
             fg="white", side=None, px=0):
        b = tk.Button(parent, text=text, font=self.f_btn,
                      bg=bg, fg=fg, relief=tk.FLAT,
                      padx=22, pady=7, cursor="hand2",
                      activebackground=hover_bg, activeforeground=fg,
                      command=cmd, bd=0)
        b.bind("<Enter>", lambda e: b.config(bg=hover_bg))
        b.bind("<Leave>", lambda e: b.config(bg=bg))
        if side:
            b.pack(side=side, padx=px)
        else:
            b.pack(pady=4)
        return b


# ══════════════════════════════════════════════════════════════════════════════
#  ENTRY POINT
# ══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    root = tk.Tk()
    SistemPakarTHT(root)
    root.mainloop()