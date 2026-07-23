# Prompt Gemini — Generate Kerangka Berpikir Skripsi

Gunakan prompt di bawah ini di Gemini (Google AI Studio / Gemini Advanced) untuk generate diagram Kerangka Berpikir sesuai isi skripsi.

---

## PROMPT

```
Buatkan diagram flowchart Kerangka Berpikir untuk skripsi dengan judul:

"Rancang Bangun Platform Sistem Evaluasi Pelaporan Menggunakan Next.js dan Go Guna Optimalisasi Layanan Publik (Studi Kasus di Dinas Kependudukan dan Pencatatan Sipil Kabupaten Garut)"

Metode penelitian: Design Thinking (Empathize, Define, Ideate, Prototype, Test)

Alur kerangka berpikir harus menggambarkan alur dari MASALAH → ANALISIS → PENGERJAAN → HASIL, dengan detail sebagai berikut:

### Struktur Flowchart (Atas ke Bawah):

**1. MULAI** (Oval)

**2. IDENTIFIKASI MASALAH** (Kotak abu-abu)
   │
   ├── Observasi langsung di Disdukcapil Kab. Garut
   └── Wawancara dengan petugas perekaman & Bidang PIAK

**3. STUDI LITERATUR** (Kotak abu-abu)
   │
   ├── Penelitian terdahulu (sistem informasi kependudukan)
   └── Teori: Design Thinking, Rules-Based Scoring, Next.js, Go

**4. ANALISIS KEBUTUHAN SISTEM** (Kotak abu-abu)
   │
   ├── Kebutuhan Fungsional (pelaporan harian, deteksi anomali, evaluasi scoring)
   └── Kebutuhan Non-Fungsional (responsivitas, keamanan, performa)

**5. METODE DESIGN THINKING** (Kotak abu-abu besar, berisi 5 tahap berurutan):

   a. EMPATHIZE
      ├── Observasi langsung di lokasi kerja
      └── Wawancara semi-struktural dengan narasumber kunci

   b. DEFINE
      ├── Problem Statement
      └── How Might We (HMW)

   c. IDEATE
      ├── Brainstorming ide solusi
      └── Affinity Diagram

   d. PROTOTYPE
      ├── User Flow
      ├── Wireframe (Low-Fidelity)
      ├── Desain Visual (Warna, Font, Komponen UI)
      └── High-Fidelity Prototyping (Figma)

   e. TEST
      ├── Black-Box Testing (fungsionalitas)
      ├── Uji Usability (Wawancara/SUS)
      └── Feedback & Iterasi Perbaikan

**6. IMPLEMENTASI SISTEM** (Kotak abu-abu)
   │
   ├── Frontend: Next.js 15 + Tailwind CSS
   └── Backend: Go (Golang) + Supabase + Redis

**7. HASIL DAN PEMBAHASAN** (Kotak abu-abu)
   │
   ├── Hasil pengujian fungsionalitas
   ├── Hasil uji usability
   └── Evaluasi ketercapaian tujuan

**8. KESIMPULAN DAN SARAN** (Kotak abu-abu)

**9. SELESAI** (Oval)

### Aturan Desain:
- Warna: Monokrom (abu-abu + putih + hitam), bersih dan profesional
- Font: Sans-serif (seperti Arial atau Calibri)
- Box inti (proses utama): abu-abu muda dengan border hitam
- Sub-aktivitas: box putih dengan bullet point
- Panah penghubung antar proses utama
- Tata letak: vertikal (atas ke bawah), dengan tahap Design Thinking bisa horizontal di dalam container
- Gaya: mirip flowchart akademik untuk skripsi S1, bukan diagram business process
- Format output: SVG atau PNG resolusi tinggi
```

---

## CATATAN PENTING

1. **Ganti placeholder** nama teknologi dengan yang sesuai jika Gemini salah interpretasi
2. **Tahap Test** di skripsi ini menggunakan:
   - Black-Box Testing (fungsionalitas sistem)
   - Uji Usability melalui **wawancara singkat** (bukan angket SUS penuh) — 20 responden, skor SUS 85.62 (Excellent)
3. **Logo/ikon** tidak wajib — flowchart teks saja sudah cukup untuk skripsi S1
4. Setelah dapat hasil dari Gemini, **simpan sebagai PNG** dan masukkan ke dokumen sebagai Gambar 3.1

## ALTERNATIF: Prompt Singkat (untuk Gemini Free)

```
Buatkan flowchart Kerangka Berpikir penelitian S1 berikut:

Judul: Rancang Bangun Platform Sistem Evaluasi Pelaporan Menggunakan Next.js dan Go (Disdukcapil Kab. Garut)
Metode: Design Thinking

Alur: 
MULAI → Identifikasi Masalah (Observasi + Wawancara) → Studi Literatur → Analisis Kebutuhan Sistem → Design Thinking [Empathize → Define → Ideate → Prototype → Test (Black-Box + Usability)] → Implementasi (Next.js + Go) → Hasil & Pembahasan → Kesimpulan → SELESAI

Gaya: flowchart akademik monokrom, box abu-abu untuk proses utama, box putih untuk sub-aktivitas. Format PNG.
```
