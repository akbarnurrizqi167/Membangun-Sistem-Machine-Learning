# 🚀 Membangun Sistem Machine Learning - Submission Proyek Akhir Dicoding

Ini adalah proyek akhir dari kelas Membangun Sistem Machine Learning yang diselenggarakan oleh Dicoding. Proyek ini mengimplementasikan prinsip dan praktik **MLOps** untuk membangun sistem machine learning yang terstruktur, terukur, dan dapat dimonitor secara menyeluruh menggunakan **MLflow**, **GitHub Actions**, **Prometheus**, **Grafana**, dan **Telegram Alerting**.

## 🏅 Sertifikat

🔗 Verifikasi Sertifikat Dicoding (https://www.dicoding.com/certificates/GRX5JN4VYX0M)

## 🎯 Tujuan Proyek

Tujuan dari proyek ini adalah membangun sistem machine learning yang lengkap dan terotomatisasi, mencakup proses:

- Eksperimen model dan pelacakan metrik
- Manajemen artefak dan model
- CI/CD pipeline dengan GitHub Actions
- Model serving lokal menggunakan MLflow
- Monitoring metrik sistem dan model secara real-time
- Alerting otomatis menggunakan **Grafana** dan **Telegram Bot**

## 🧪 Fitur yang Diimplementasikan

### ✅ Kriteria 1: Eksperimen Dataset Pelatihan

- Eksperimen dilakukan dengan berbagai hyperparameter
- Pelacakan menggunakan **MLflow Tracking**
- Evaluasi model berdasarkan akurasi
- Disimpan di direktori `mlruns`

### ✅ Kriteria 2: Membangun Model Machine Learning

- Model menggunakan **RandomForestClassifier**
- Proses pelatihan, evaluasi, dan pendaftaran model ke MLflow
- Artefak model terstruktur dan siap digunakan untuk serving

### ✅ Kriteria 3: Workflow CI/CD

- CI pipeline menggunakan **GitHub Actions**
- Workflow otomatis:
  - Menjalankan eksperimen
  - Logging MLflow
  - Upload artefak ke GitHub
- Belum menerapkan Docker push ke DockerHub (skor *Skilled*)

### ✅ Kriteria 4: Monitoring & Logging

- Exporter metrik menggunakan `prometheus_client` (Python)
- Metrik yang dimonitor:
  - `model_accuracy`
  - `inference_success_total`
  - `inference_fail_total`
  - `python_info`
  - `python_gc_objects_collected_total`
- Visualisasi metrik menggunakan **Grafana**
- **Alerting dengan Telegram Bot**:
  - Menggunakan konfigurasi Alertmanager yang terhubung ke Telegram
  - Tersedia rules alert berbasis akurasi dan jumlah inferensi gagal
- Screenshot dan konfigurasi alert tersedia dalam folder `Monitoring dan Logging/6.bukti alerting Grafana`

## 📊 Tools yang Digunakan

| Tool           | Deskripsi                                           |
| -------------- | --------------------------------------------------- |
| MLflow         | Tracking dan registry model                         |
| GitHub Actions | Otomasi CI/CD                                       |
| Prometheus     | Monitoring metrik model & sistem                    |
| Grafana        | Visualisasi metrik dan alerting                     |
| Telegram Bot   | Channel alert untuk kondisi kritis model/sistem     |
| Docker         | Containerization (opsional, belum push ke registry) |

## 📌 Catatan Reviewer

> "Proyek ini sangat baik. Untuk mencapai skor *Advanced*, dapat ditingkatkan pada aspek integrasi dengan DagsHub dan menambahkan lebih banyak alerting serta metrik."

## 🔮 Potensi Pengembangan Selanjutnya

- Menyimpan artefak eksperimen ke DagsHub
- Deploy model sebagai Docker image dan push ke DockerHub
- Tambahkan lebih banyak metrik sistem seperti latensi, memory usage
- Otomatiskan inference pipeline dan notifikasi ke Slack/Telegram
- Buat dashboard publik untuk real-time inference status

