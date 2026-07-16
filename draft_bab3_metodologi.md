# DRAFT BAB III - METODOLOGI PENELITIAN
## Berdasarkan Data Wawancara + Panduan Skripsi IPI Garut 2025

---

## 3.1 Objek Penelitian

### 3.1.1 Profil Perusahaan/Instansi

Dinas Kependudukan dan Pencatatan Sipil (Disdukcapil) Kabupaten Garut merupakan instansi pemerintah daerah yang bertanggung jawab dalam pengelolaan data kependudukan dan pencatatan sipil. Disdukcapil memiliki peran strategis dalam pelayanan publik terkait dokumen kependudukan seperti Kartu Tanda Penduduk (KTP), Kartu Keluarga (KK), Akta Kelahiran, dan dokumen kependudukan lainnya.

**Informasi Umum:**
- **Jumlah Pegawai:** 184 orang
- **Bidang Utama:** 
  - Bidang Pendaftaran Penduduk
  - Bidang Pengelolaan Informasi Administrasi Kependudukan (PIAK)
- **Volume Perekaman:** Rata-rata 3.783 data per 6 bulan (≈ 630/bulan atau minimal 400 biometric/hari)

### 3.1.2 Struktur Organisasi

Struktur organisasi Disdukcapil Kabupaten Garut yang terlibat dalam penelitian ini meliputi:

| No | Jabatan | Tanggung Jawab Utama |
|----|---------|---------------------|
| 1 | Kepala Dinas | Pengawasan dan keputusan strategis |
| 2 | Kabid PIAK | Monitoring dan evaluasi pelaporan |
| 3 | Kabid Dafduk | Pengelolaan data kependudukan |
| 4 | JFT Administrator Database | Pengelolaan database dan perbaikan data |
| 5 | Petugas Perekaman | Verifikasi dokumen dan perekaman biometric |

**Alur Wewenang:**
```
Kepala Dinas
    ↓
Kabid PIAK / Kabid Dafduk
    ↓
JFT Administrator Database ←→ Petugas Perekaman
```

---

## 3.2 Metode dan Desain Penelitian

### 3.2.1 Teknik Pengumpulan Data

Penelitian ini menggunakan teknik pengumpulan data campuran (mixed-method) yang meliputi:

#### a. Observasi Lapangan
- **Lokasi:** Disdukcapil Kabupaten Garut
- **Objek:** Aktivitas harian petugas perekaman
- **Yang diamati:**
  - Alur kerja verifikasi dokumen KK dan Akta Kelahiran
  - Proses perekaman biometric (sidik jari, iris mata, tanda tangan, foto)
  - Metode rekapitulasi yang digunakan (Excel/Notepad)
  - Kendala teknis dan operasional

#### b. Wawancara Mendalam
- **Narasumber:** Petugas perekaman, JFT Administrator Database, Kabid PIAK, Kabid Dafduk
- **Topik:** Alur kerja, kendala pelaporan, kebutuhan sistem
- **Metode:** Structured interview dengan panduan pertanyaan

#### c. Studi Dokumen
- **Data yang dikumpulkan:**
  - Volume perekaman (3.783 data/6 bulan)
  - Format laporan yang ada
  - SOP yang berlaku

#### d. Kuesioner
- **Responden:** Petugas perekaman dan administrator database
- **Tujuan:** Mengukur tingkat kebutuhan dan kesiapan pengguna terhadap sistem baru

### 3.2.2 Kerangka Berpikir

```
[Permasalahan]
    ↓
Proses pelaporan manual (Excel/Notepad) → Inefisiensi waktu
Missing link follow-up → Data anomali tertunda
Tanpa standar penilaian → Kinerja tidak terukur
    ↓
[Solusi]
Platform sistem evaluasi pelaporan berbasis web
    ↓
[Fitur Utama]
- Rekapitulasi pelaporan terkait detail anomali
- Live monitoring progress berjenjang
- Notifikasi email ke pemohon
- Dashboard dengan indikator kinerja
    ↓
[Hasil]
Efisiensi penanganan anomali data
Penilaian kinerja terukur
Peningkatan kualitas pelayanan
```

### 3.2.3 Metode Penelitian

Penelitian ini menggunakan metode **Scrum** sebagai pendekatan pengembangan sistem informasi. Scrum dipilih karena:

1. **Fleksibilitas:** Memungkinkan adaptasi perubahan kebutuhan selama pengembangan
2. **Iterasi Cepat:** Pengembangan dilakukan dalam siklus sprint (2-4 minggu)
3. **Kolaborasi:** Melibatkan pengguna (Disdukcapil) dalam setiap tahap pengembangan
4. **Prioritisasi Fitur:** Fitur dapat diurutkan berdasarkan kebutuhan mendesak

**Tahapan Scrum yang diterapkan:**
- Product Backlog: Pengumpulan dan prioritisasi kebutuhan
- Sprint Planning: Perencanaan fitur per sprint
- Daily Standup: Monitoring kemajuan harian
- Sprint Review: Demonstrasi fitur kepada stakeholder
- Sprint Retrospective: Evaluasi dan perbaikan proses

### 3.2.4 Analisis Kondisi Saat Ini (Sistem Eksisting)

Berdasarkan hasil wawancara dan observasi, kondisi saat ini di Disdukcapil Kabupaten Garut adalah sebagai berikut:

#### a. Alur Kerja Pelaporan

| No | Aktivitas | Metode Saat Ini | Waktu |
|----|-----------|-----------------|-------|
| 1 | Verifikasi dokumen KK & Akta Kelahiran | Manual (cek fisik) | - |
| 2 | Perekaman biometric | Aplikasi Biometric Enrollment | - |
| 3 | Input data ke SIAK | Aplikasi SIAK | - |
| 4 | Rekapitulasi jumlah perekaman | Excel/Notepad | 30 menit/hari |
| 5 | Pelaporan ke pimpinan | File Excel/Notepad | - |
| 6 | Pengajuan bulanan | Google Drive folder bulanan | - |

#### b. Penanganan Anomali Data

**Duplicate Operator:**
- **Definisi:** Ketika biometric iris mata dan/atau sidik jari pemohon identik dengan petugas perekaman
- **Deteksi:** Muncul status "Duplicate_Record" di aplikasi dengan sandingan petugas rekam
- **Kendala:** Kelalaian petugas dalam menangkap biometric pemohon

**Salah Rekam:**
- **Jenis:** Iris mata pemohon dan petugas rekam identik
- **Frekuensi:** 3-4 kasus per bulan
- **Proses Koreksi:** Manual dengan disposisi kepada pimpinan

#### c. Evaluasi Kinerja

| Aspek | Kondisi Saat Ini |
|-------|------------------|
| **Metode Penilaian** | Mengukur realisasi vs target bulanan |
| **Standar Penilaian** | Tidak ada standar baku |
| **Monitoring** | Dilakukan oleh pimpinan |
| **Kendala Utama** | Missing link antara pemohon dan administrator database |

#### d. Tantangan dan Masalah

1. **Pelaporan Manual:** Masih menggunakan Excel/Notepad, rekapitulasi terpisah dengan format beragam
2. **Missing Link:** Petugas perekaman sering lupa follow up perbaikan data ke administrator
3. **Dokumen Tidak Lengkap:** Sering melampirkan fotokopi ijazah yang tidak dilegalisir
4. **Perlambatan:** Proses manual menyebabkan perlambatan penanganan anomali data

---

## 3.3 ~~Teknik Analisis Data~~ → DIPINDAHKAN KE BAB II

> **CATATAN:** Bagian ini sebaiknya dipindahkan ke BAB II (Landasan Teori) sebagai subbab tentang metodologi analisis data. Di Bab III, yang dibutuhkan adalah analisis kondisi eksisting (3.2.4), bukan teori analisis data.

**Rekomendasi:**
- Pindahkan "Teknik Analisis Data" ke BAB II sebagai subbab 2.X tentang "Metodologi Analisis Data Penelitian"
- Ganti dengan "Analisis Kebutuhan Sistem" yang lebih fokus pada kebutuhan Disdukcapil

---

## 3.4 Perancangan dan Teknologi Sistem

### 3.4.1 Model Perancangan Sistem

Sistem yang dikembangkan menggunakan pendekatan **Unified Modeling Language (UML)** dengan diagram:
- **Use Case Diagram:** Interaksi aktor dengan sistem
- **Activity Diagram:** Alur proses bisnis
- **Class Diagram:** Struktur data dan relasi
- **Sequence Diagram:** Interaksi antar komponen

### 3.4.2 Deskripsi Teknologi yang Digunakan

| Komponen | Teknologi | Alasan |
|----------|-----------|--------|
| **Frontend** | Next.js 15, Tailwind CSS | Performa tinggi, responsive |
| **Backend** | Go (Golang) + Gin | Performa concurrent, ringan |
| **Database** | Supabase (PostgreSQL) | Real-time, mudah diintegrasikan |
| **Hosting** | Vercel | Deployment Next.js optimal |

### 3.4.3 Rencana Uji Coba Sistem

| No | Jenis Pengujian | Metode | Target |
|----|-----------------|--------|--------|
| 1 | Fungsionalitas | Black-box Testing | 100% spesifikasi terpenuhi |
| 2 | Usabilitas | System Usability Scale (SUS) | Skor ≥ 68 (Good) |
| 3 | Performa | Load Testing | Response time < 200ms |

---

## REKOMENDASI PERUBAAN STRUKTUR BAB III

### Struktur Baru yang Disarankan:

```
BAB III - METODOLOGI PENELITIAN
├── 3.1 Objek Penelitian
│   ├── 3.1.1 Profil Perusahaan/Instansi
│   └── 3.1.2 Struktur Organisasi
├── 3.2 Metode dan Desain Penelitian
│   ├── 3.2.1 Teknik Pengumpulan Data
│   ├── 3.2.2 Kerangka Berpikir
│   ├── 3.2.3 Metode Penelitian (Scrum)
│   └── 3.2.4 Analisis Kondisi Saat Ini (SISTEM EKSISTING)
├── 3.3 Analisis Kebutuhan Sistem (BARU - ganti Teknik Analisis Data)
│   ├── 3.3.1 Kebutuhan Fungsional
│   └── 3.3.2 Kebutuhan Non-Fungsional
└── 3.4 Perancangan dan Teknologi Sistem
    ├── 3.4.1 Model Perancangan Sistem (UML)
    ├── 3.4.2 Deskripsi Teknologi yang Digunakan
    └── 3.4.3 Rencana Uji Coba Sistem
```

---

*Draf ini disusun berdasarkan data wawancara tanggal 16 Juli 2026*
*Referensi: Panduan Skripsi SI IPI Garut 2025*
