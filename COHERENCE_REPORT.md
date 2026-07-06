# SKRIPSI COHERENCE CHECK REPORT
## Document: /root/skripsi/Prototype.docx
## Date: 2026-07-06
## Method: XML parsing (unzip + ElementTree), 456 paragraphs extracted

---

## DIMENSION 1: CITATION-REFERENCE MATCH — ⚠️ PARTIAL FAIL

**Daftar Pustaka entries:** 20 (paragraphs [430]–[449])
**Citations found in body text:** 16 unique (Author, Year) pairs

### (a) Citations in text NOT in Daftar Pustaka: 1 false positive

| Citation | Status | Details |
|----------|--------|---------|
| (Lisjak, 2021) | FALSE POSITIVE | Caused by regex picking up "Lisjak" from "Mikulić dan Lisjak (2021)". The actual reference is Mikulić, Lisjak, & Štefanić (2021) which IS in Daftar Pustaka. |

**Verdict:** No genuinely missing references. All in-text citations have matching Daftar Pustaka entries.

### (b) Entries in Daftar Pustaka NOT cited in text: 2 entries

| Reference | Year | Status | Details |
|-----------|------|--------|---------|
| Donovan, A. A., & Kernighan, B. W. | 2015 | **UNCITED** | Never appears in body text at all |
| Supabase | 2024 | **UNCITED AS FORMAL REF** | "Supabase" mentioned 15+ times by name but never with "(2024)" year citation |
| Vercel | 2024 | **UNCITED AS FORMAL REF** | "Vercel" mentioned once (para [182]) but without "(2024)" year citation |
| Laudon, K. C., & Laudon, J. P. | 2020 | CITED | Cited at para [163] as "(Laudon & Laudon, 2020)" — regex missed due to `&` separator |
| Mikulić, I., Lisjak, D., & Štefanić, N. | 2021 | CITED | Cited multiple times as "Mikulić dan Lisjak (2021)" — regex missed due to "dan" connector |

**Corrected genuine uncited count:** 3 (Donovan 2015, Supabase 2024, Vercel 2024)

**OVERALL: FAIL** — 3 Daftar Pustaka entries have no corresponding formal in-text citation.

---

## DIMENSION 2: RUMUSAN MASALAH → KESIMPULAN ALIGNMENT — ✅ PASS

### Rumusan Masalah (BAB I, §1.2):
- **RM1:** "Bagaimana merancang dan membangun platform sistem evaluasi pelaporan yang mencakup fitur pelaporan aktivitas harian pegawai, deteksi data duplikat (duplicate operator), pelaporan salah rekam, serta pengajuan bulanan secara terintegrasi di Disdukcapil Kabupaten Garut?"
- **RM2:** "Bagaimana mengimplementasikan fitur evaluasi pelaporan secara otomatis dan terukur menggunakan pendekatan rules-based scoring engine?"
- **RM3:** "Bagaimana tingkat penerimaan pengguna terhadap platform yang dikembangkan berdasarkan pengujian fungsionalitas (Black-box Testing) dan usability (System Usability Scale)?"

### Kesimpulan (BAB V, §5.1) — 4 paragraphs:
- **K2** addresses RM1: "Sistem yang dikembangkan berhasil dirancang dan dibangun menggunakan arsitektur modern Next.js dan Go dengan metode Scrum, yang terbukti adaptif dalam menerjemahkan kebutuhan operasional birokrasi ke dalam fitur fungsional seperti Rule-Based Scoring dan Duplicate Operator."
- **K3** addresses RM2: "Implementasi platform ini menjawab Rumusan Masalah kedua dengan menunjukkan dampak signifikan terhadap efisiensi operasional internal, di antaranya: peningkatan kecepatan pemrosesan laporan bulanan sebesar 95% (dari 240 menit menjadi 12 menit)..."
- **K4** addresses RM3: "Pengujian yang dilakukan menjawab Rumusan Masalah ketiga, di mana performa sistem terbukti sangat stabil dengan waktu respons rata-rata 125–180 ms, sedangkan tingkat usabilitas mencapai skor SUS sebesar 82,5 (kategori Excellent)..."

### Keyword verification:
- RM1 → Kesimpulan: matched ['platform', 'rancang', 'bangun', 'duplicate operator'] ✅
- RM2 → Kesimpulan: matched ['scoring', 'efisiensi', '95%'] — note: "rules-based" and "otomatis" not explicitly mentioned ⚠️
- RM3 → Kesimpulan: matched ['pengguna', 'sus', 'usabilitas', '82,5', 'excellent'] ✅

**OVERALL: PASS** (all 3 RMs explicitly answered, though RM2 answer could be more specific about "rules-based scoring engine")

---

## DIMENSION 3: TUJUAN → KETERCAPAIAN ALIGNMENT — ✅ PASS

### Tujuan (BAB I, §1.4):
- **T1:** "Merancang dan membangun platform sistem evaluasi pelaporan yang mencakup fitur pelaporan aktivitas harian pegawai, deteksi data duplikat, pelaporan salah rekam, serta pengajuan bulanan secara terintegrasi di Disdukcapil Kabupaten Garut."
- **T2:** "Mengimplementasikan fitur evaluasi pelaporan secara otomatis dan terukur menggunakan pendekatan rules-based scoring engine."
- **T3:** "Melakukan pengujian fungsionalitas sistem menggunakan Black-box Testing dan mengukur tingkat penerimaan pengguna melalui System Usability Scale (SUS)."

### Ketercapaian (BAB IV, §4.3.1) — 12 paragraphs:
- **T1:** ✅ Fully addressed — "Tujuan 1: Merancang dan membangun platform sistem evaluasi pelaporan pegawai berbasis web menggunakan arsitektur Next.js dan Go dengan menerapkan tahapan metode Scrum. Ketercapaian: Tujuan ini berhasil dicapai..."
- **T2:** ✅ Addressed — "Tujuan 2: Mengukur dan menguji tingkat performa serta fungsionalitas platform..." with validation via Black-Box, SUS, and Load Testing
- **T3:** ✅ Fully addressed — Black-Box 100% spec compliance, SUS 82.5 (Excellent), response time 125-180ms

### Keyword verification:
- T1 → Ketercapaian: matched ['rancang', 'bangun', 'platform', 'scrum', 'next.js', 'go', 'sprint'] ✅
- T2 → Ketercapaian: matched ['scoring', 'evaluasi', 'rule-based'] ✅
- T3 → Ketercapaian: matched ['black-box', 'sus', 'fungsionalitas', '82,5'] ✅

### Issue noted:
- §4.3.1 labels "Tujuan 2" as "Mengukur dan menguji tingkat performa serta fungsionalitas platform..." which is NOT the same text as the actual T2 from §1.4 ("Mengimplementasikan fitur evaluasi pelaporan secara otomatis dan terukur menggunakan pendekatan rules-based scoring engine"). **Content mismatch between §1.4 and §4.3.1 for Tujuan 2.**

**OVERALL: PASS** (all 3 Tujuan addressed, but T2 has a content mismatch between §1.4 and §4.3.1)

---

## DIMENSION 4: TEXT ANOMALIES — ✅ PASS (minor issues)

### 4a. Duplicate Paragraphs: 6 instances
All are title page repetitions (front matter cover pages for LEMBAR PENGESAHAN and LEMBAR PENGUJIAN):
- Para [0]==[27]==[45]: "RANCANG BANGUN PLATFORM SISTEM EVALUASI"
- Para [1]==[28]==[46]: "PELAPORAN MENGGUNAKAN NEXT.JS DAN GO"
- Para [2]==[29]==[47]: "GUNA OPTIMALISASI LAYANAN PUBLIK"

**Status:** Expected and acceptable for Word document structure (cover, approval, testing pages).

### 4b. Broken Sentences: Acceptable
Most flagged items are keywords lines, table/figure captions, reference URLs, and list introductions ending with colon — standard academic formatting.

### 4c. Naming Consistency: ACCEPTABLE
| Reference Pattern | Count |
|-------------------|-------|
| "sistem evaluasi pelaporan" | 24 |
| "sistem yang dikembangkan" | 21 |
| "platform sistem" | 18 |
| "platform yang dikembangkan" | 8 |
| "platform ini" | 4 |
| "sistem ini" | 3 |

Minor variations are normal for Indonesian academic prose.

### 4d. SELLICA Mentions: 0 found ✅

### 4e. Mikulić Author Name: NO DUPLICATION ✅
Initial `read_file` auto-extraction suggested "Mikulić dan Mikulić dan Lisjak" duplication, but XML parsing confirms the text correctly reads "Mikulić dan Lisjak (2021)" — no duplication exists in the actual document XML.

**OVERALL: PASS** — No critical text anomalies found.

---

## DIMENSION 5: HEADING NUMBERING — ❌ FAIL

### Missing Parent Headings: 4 instances

| Missing Heading | Required By | Severity |
|----------------|-------------|----------|
| **4.2** (Heading2) | 4.2.1, 4.2.2, 4.2.3 | **HIGH** |
| **4.3** (Heading2) | 4.3.1 | **HIGH** |

**Details:**
- "4.2 Hasil Pengujian Fungsionalitas dan Performa" exists as **plain body text** (paragraph [386]), not as a Heading2 style. Its children 4.2.1, 4.2.2, 4.2.3 are properly styled as Heading3.
- "4.3" has no heading at all — 4.3.1 appears as Heading3 without a parent.

### BAB IV Heading Structure (problematic):
```
4.1   [Heading2]  Implementasi Sistem
  4.1.1 [Heading3]  Hasil Pengembangan Sprint
  4.1.2 [Heading3]  Implementasi Antarmuka Pengguna
  4.1.3 [Heading3]  Implementasi Logika Bisnis
  (4.2) [PLAIN TEXT] Hasil Pengujian Fungsionalitas dan Performa  ← NOT A HEADING!
    4.2.1 [Heading3]  Uji Fungsionalitas
    4.2.2 [Heading3]  Uji Usabilitas
    4.2.3 [Heading3]  Uji Performa
  (4.3) [MISSING]                                            ← COMPLETELY MISSING!
    4.3.1 [Heading3]  Ketercapaian Tujuan Penelitian
```

### Numbering Sequence: No gaps found ✅
Within each level, numbering is sequential (1.1→1.6, 2.1→2.12, 3.1→3.4, 4.1→4.1.3, 5.1→5.2).

### Other observations:
- Heading [241] and [325] are empty Heading2 styles (likely formatting artifacts)
- Heading [364] is an empty Heading3 style

**OVERALL: FAIL** — 2 missing parent headings (4.2 and 4.3) break the hierarchical structure in BAB IV.

---

## SUMMARY TABLE

| Dimension | Result | Issues |
|-----------|--------|--------|
| 1. Citation-Reference Match | ❌ **FAIL** | 3 uncited refs: Donovan (2015), Supabase (2024), Vercel (2024) |
| 2. RM → Kesimpulan Alignment | ✅ **PASS** | All 3 RMs answered; RM2 could be more explicit |
| 3. Tujuan → Ketercapaian Alignment | ✅ **PASS** | All addressed; T2 content mismatch between §1.4 and §4.3.1 |
| 4. Text Anomalies | ✅ **PASS** | No critical anomalies (duplicates are front matter only) |
| 5. Heading Numbering | ❌ **FAIL** | Missing parent headings 4.2 and 4.3 in BAB IV |

### PRIORITY FIXES:
1. **HIGH:** Convert "4.2 Hasil Pengujian Fungsionalitas dan Performa" from plain text (para [386]) to Heading2 style
2. **HIGH:** Add "4.3 Pembahasan" or similar Heading2 before section 4.3.1
3. **MEDIUM:** Add in-text citations for Donovan & Kernighan (2015), Supabase (2024), and Vercel (2024), OR remove from Daftar Pustaka
4. **LOW:** Consider making Kesimpulan K3 more explicitly mention "rules-based scoring engine"
5. **LOW:** Fix empty Heading2 at [241] and [325], empty Heading3 at [364]
