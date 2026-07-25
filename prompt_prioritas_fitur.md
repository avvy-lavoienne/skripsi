# Prompt UML — Tabel 4.2 Prioritas Fitur MoSCoW

Paste ke kroki.io/plantuml:

```plantuml
@startuml
skinparam backgroundColor white
skinparam defaultFontName Arial
skinparam defaultFontSize 11
skinparam shadowing false

title Tabel 4.2 Prioritas Fitur — MoSCoW Method

together {
  card "**Must Have** 🔴" as must #FFCDD2 {
    --Form Input Laporan Digital
    --Deteksi Duplicate Operator
    --Rules-Based Scoring Engine
    --Dashboard Monitoring
    --Deteksi Salah Rekam
  }
  card "**Should Have** 🟡" as should #FFF9C4 {
    --Notifikasi Email Otomatis
    --Export Laporan (Excel/PDF)
    --Manajemen User & Role
    --Autentikasi JWT
  }
}

together {
  card "**Could Have** 🟢" as could #C8E6C9 {
    --Visualisasi Grafik Tren
    --Pencarian Lanjutan
    --Filter Tersimpan
    --Glossary Istilah
  }
  card "**Won't Have** ⚪" as wont #E0E0E0 {
    --Integrasi Real-time SIAK
    --Mobile Native App
    --Bulk Action Anomali
    --Selly AI Chat
  }
}

must -[hidden]right-> should
could -[hidden]right-> wont

@enduml
```
