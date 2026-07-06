# SKRIPSI COHERENCE CHECK REPORT
## Document: /root/skripsi/Prototype.docx
## Date: 2026-07-06

---

## DIMENSION 1: CITATION-REFERENCE MATCH — ⚠️ PARTIAL FAIL

**Daftar Pustaka entries:** 20
**Citations found in body text:** 16 unique (Author, Year) pairs

### (a) Citations in text NOT in Daftar Pustaka: 1 issue

| Citation | Status | Details |
|----------|--------|---------|
| (Lisjak, 2021) | FALSE POSITIVE | Not a real separate citation. Caused by text error "Mikulić dan Mikulić dan Lisjak (2021)" which duplicates "Mikulić dan". The correct reference is Mikulić, Lisjak, & Štefanić (2021) which IS in Daftar Pustaka. |

**Verdict:** No genuine missing references. The (Lisjak, 2021) detection is a symptom of the duplicate-author-name text anomaly (see Dim 4).

### (b) Entries in Daftar Pustaka NOT cited in text: 5 entries

| Reference | Year | Issue |
|-----------|------|-------|
| Donovan, A. A., & Kernighan, B. W. | 2015 | Never cited in body text — dead reference |
| Laudon, K. C., & Laudon, J. P. | 2020 | Cited at para 166 as "(Laudon & Laudon, 2020)" — MISSED by extraction due to `&` separator. **Actually cited — false alarm.** |
| Mikulić, I., Lisjak, D., & Štefanić, N. | 2021 | Cited multiple times as "Mikulić dan Lisjak (2021)" — MISSED by extraction due to "dan" connector. **Actually cited — false alarm.** |
| Supabase | 2024 | "Supabase" is mentioned 15+ times in body but never with "(2024)" year citation — **GENUINELY uncited as formal reference** |
| Vercel | 2024 | "Vercel" mentioned once (para 185) but without "(2024)" year — **GENUINELY uncited as formal reference** |

**Corrected count:**
- **2 genuinely uncited references:** Donovan & Kernighan (2015), Supabase (2024), Vercel (2024)
- **0 genuinely missing references from text**

**OVERALL: FAIL** — 3 Daftar Pustaka entries have no corresponding in-text citation.

---

## DIMENSION 2: RUMUSAN MASALAH → KESIMPULAN ALIGNMENT — ✅ PASS

### Rumusan Masalah (BAB I, §1.2):
- **RM1:** "Bagaimana merancang dan membangun platform sistem evaluasi pelaporan yang mencakup fitur pelaporan aktivitas harian pegawai, deteksi data duplikat (duplicate operator), pelaporan salah rekam, serta pengajuan bulanan secara terintegrasi di Disdukcapil Kabupaten Garut?"
- **RM2:** "Bagaimana mengimplementasikan fitur evaluasi pelaporan secara otomatis dan terukur menggunakan pendekatan rules-based scoring engine?"
- **RM3:** "Bagaimana tingkat penerimaan pengguna terhadap platform yang dikembangkan berdasarkan pengujian fungsionalitas (Black-box Testing) dan usability (System Usability Scale)?"

### Kesimpulan (BAB V, §5.1):
- **K2** explicitly addresses RM1: "Sistem yang dikembangkan berhasil dirancang dan dibangun menggunakan arsitektur modern Next.js dan Go dengan metode Scrum, yang terbukti adaptif dalam menerjemahkan kebutuhan operasional birokrasi ke dalam fitur fungsional seperti Rule-Based Scoring dan Duplicate Operator."
- **K3** explicitly addresses RM2: "Implementasi platform ini menjawab Rumusan Masalah kedua dengan menunjukkan dampak signifikan terhadap efisiensi operasional internal, di antaranya: peningkatan kecepatan pemrosesan laporan bulanan sebesar 95% (dari 240 menit menjadi 12 menit)..."
- **K4** explicitly addresses RM3: "Pengujian yang dilakukan menjawab Rumusan Masalah ketiga, di mana performa sistem terbukti sangat stabil dengan waktu respons rata-rata 125–180 ms, sedangkan tingkat usabilitas mencapai skor SUS sebesar 82,5 (kategori Excellent)..."

### Issues:
- **RM2 answer is incomplete:** Kesimpulan K3 mentions "efisiensi" and "scoring" but does NOT explicitly mention "rules-based scoring engine", "otomatis", or "terukur" — the specific technical terms from RM2. The answer focuses on efficiency metrics rather than the rules-based scoring mechanism itself.
- All 3 RMs are addressed, but with varying specificity.

**OVERALL: PASS** (all 3 RMs answered, though RM2 answer could be more explicit)

---

## DIMENSION 3: TUJUAN → KETERCAPAIAN ALIGNMENT — ✅ PASS

### Tujuan (BAB I, §1.4):
- **T1:** "Merancang dan membangun platform sistem evaluasi pelaporan yang mencakup fitur pelaporan aktivitas harian pegawai, deteksi data duplikat, pelaporan salah rekam, serta pengajuan bulanan secara terintegrasi di Disdukcapil Kabupaten Garut."
- **T2:** "Mengimplementasikan fitur evaluasi pelaporan secara otomatis dan terukur menggunakan pendekatan rules-based scoring engine."
- **T3:** "Melakukan pengujian fungsionalitas sistem menggunakan Black-box Testing dan mengukur tingkat penerimaan pengguna melalui System Usability Scale (SUS)."

### Ketercapaian (BAB IV, §4.3.1):
- **T1:** ✅ Fully addressed — KC1 explicitly states "Tujuan 1: Merancang dan membangun platform sistem evaluasi pelaporan pegawai berbasis web menggunakan arsitektur Next.js dan Go dengan menerapkan tahapan metode Scrum. Ketercapaian: Tujuan ini berhasil dicapai..."
- **T2:** ✅ Addressed — KC5 mentions "Rule-Based Scoring" and "Duplicate Operator" as validated modules, and the broader Ketercapaian section discusses evaluasi and scoring engine.
- **T3:** ✅ Fully addressed — KC5 (Black-Box), KC7 (SUS 82.5 Excellent), and explicit validation numbers.

### Issues:
- **T2 Ketercapaian lacks a dedicated paragraph** — unlike T1 and T3, there is no explicit "Tujuan 2: [text]" followed by "Ketercapaian:" paragraph in §4.3.1. T2 is addressed indirectly through Tujuan 2 in the Ketercapaian section which focuses on performance/testing rather than the rules-based scoring engine specifically.
- **Structural mismatch:** §4.3.1 labels "Tujuan 2" as "Mengukur dan menguji tingkat performa serta fungsionalitas platform..." which is NOT the same as the actual T2 from §1.4 ("Mengimplementasikan fitur evaluasi pelaporan secara otomatis dan terukur menggunakan pendekatan rules-based scoring engine"). The Ketercapaian section redefines Tujuan 2.

**OVERALL: PASS** (all addressed, but T2 has a content mismatch between §1.4 and §4.3.1)

---

## DIMENSION 4: TEXT ANOMALIES — ⚠️ ISSUES FOUND

### 4a. Duplicate Paragraphs: 8 instances
All are in front matter (title pages, approval pages) — **expected and acceptable** for Word document structure.

### 4b. Broken Sentences: 24 instances
Most are keywords lines, table/figure captions, reference URLs, and list introductions ending with colon — **acceptable** for academic formatting. No genuinely broken sentences found in body text.

### 4c. Naming Consistency: ACCEPTABLE
- "sistem evaluasi pelaporan": 24 occurrences (consistent primary name)
- "sistem yang dikembangkan": 21 occurrences (consistent generic reference)
- "platform sistem": 18 occurrences
- "platform yang dikembangkan": 8 occurrences
- Minor variations ("sistem ini", "sistem tersebut") are normal for Indonesian academic prose.

### 4d. SELLICA Mentions: 0 found ✅
No inappropriate SELLICA references detected.

### 4e. CRITICAL — Duplicate Author Name "Mikulić dan Mikulić dan Lisjak": **3 instances**
| Paragraph | Text |
|-----------|------|
| [181] | "Penelitian **Mikulić dan Mikulić dan** Lisjak (2021) menunjukkan bahwa penerapan rules-based engine..." |
| [213] | "...**Mikulić dan Mikulić dan** Lisjak (2021) dalam studinya hanya menggunakan framework..." |
| [411] | "...konsisten dengan hasil penelitian **Mikulić dan Mikulić dan** Lisjak (2021) yang menunjukkan..." |

**This is a clear text error.** Should be "Mikulić dan Lisjak (2021)" or "Mikulić, Lisjak, dan Štefanić (2021)".

**OVERALL: FAIL** — 3 instances of duplicate author name "Mikulić dan Mikulić" must be fixed.

---

## DIMENSION 5: HEADING NUMBERING — ⚠️ ISSUES FOUND

### Missing Parent Headings: 4 issues

| Missing Heading | Required By | Severity |
|----------------|-------------|----------|
| **4.2** (Heading2) | 4.2.1, 4.2.2, 4.2.3 | HIGH — breaks §4.2 hierarchy |
| **4.3** (Heading2) | 4.3.1 | HIGH — breaks §4.3 hierarchy |

**Details:**
- Sections 4.2.1, 4.2.2, 4.2.3 exist as Heading3 but their parent "4.2 Hasil Pengujian Fungsionalitas dan Performa" exists only as **plain body text** (paragraph [391]), not as a Heading2.
- Section 4.3.1 exists as Heading3 but there is no "4.3" Heading2 parent at all.

### Numbering Sequence: No gaps found ✅
Within each level, numbering is sequential (1.1→1.2→...→1.6, 2.1→2.2→...→2.12, etc.).

### BAB IV Heading Structure (problematic):
```
4.1 [Heading2]  Implementasi Sistem
  4.1.1 [Heading3]  Hasil Pengembangan Sprint
  4.1.2 [Heading3]  Implementasi Antarmuka Pengguna
  4.1.3 [Heading3]  Implementasi Logika Bisnis
  4.2.1 [Heading3]  Uji Fungsionalitas  ← MISSING 4.2 parent!
  4.2.2 [Heading3]  Uji Usabilitas      ← MISSING 4.2 parent!
  4.2.3 [Heading3]  Uji Performa        ← MISSING 4.2 parent!
  4.3.1 [Heading3]  Ketercapaian        ← MISSING 4.3 parent!
```

**OVERALL: FAIL** — 2 missing parent headings (4.2 and 4.3) break the hierarchical structure.

---

## SUMMARY TABLE

| Dimension | Result | Critical Issues |
|-----------|--------|-----------------|
| 1. Citation-Reference Match | ❌ FAIL | 3 uncited references (Donovan 2015, Supabase 2024, Vercel 2024) |
| 2. RM → Kesimpulan Alignment | ✅ PASS | RM2 answer could be more explicit about "rules-based scoring" |
| 3. Tujuan → Ketercapaian Alignment | ✅ PASS | §4.3.1 redefines Tujuan 2 differently from §1.4 |
| 4. Text Anomalies | ❌ FAIL | 3× "Mikulić dan Mikulić dan Lisjak" duplicate author error |
| 5. Heading Numbering | ❌ FAIL | Missing parent headings 4.2 and 4.3 |

### PRIORITY FIXES:
1. **HIGH:** Fix "Mikulić dan Mikulić dan Lisjak" → "Mikulić dan Lisjak" in paragraphs 181, 213, 411
2. **HIGH:** Add Heading2 for "4.2 Hasil Pengujian Fungsionalitas dan Performa" and "4.3 Pembahasan/Ketercapaian"
3. **MEDIUM:** Add in-text citations for Donovan & Kernighan (2015), Supabase (2024), and Vercel (2024), OR remove them from Daftar Pustaka
4. **LOW:** Consider making Kesimpulan K3 more explicitly address "rules-based scoring engine" terminology
