from prometheus_client import start_http_server, Gauge, Counter
import random
import time

# Metrik: Akurasi model
model_accuracy = Gauge('model_accuracy', 'Akurasi model ML')

# Metrik: Jumlah request inferensi berhasil/gagal
success_counter = Counter('inference_success_total', 'Total inferensi berhasil')
fail_counter = Counter('inference_fail_total', 'Total inferensi gagal')

# Metrik: Jumlah inferensi per detik (throughput)
inference_throughput = Counter('inference_throughput_total', 'Jumlah total inferensi per detik')

def mock_monitoring_loop():
    while True:
        # Simulasikan akurasi model
        acc = random.uniform(0.7, 0.9)
        model_accuracy.set(acc)

        # Simulasikan inferensi berhasil/gagal
        success = random.randint(1, 3)
        fail = random.randint(0, 1)
        success_counter.inc(success)
        fail_counter.inc(fail)

        # Total inferensi dalam periode ini
        inference_throughput.inc(success + fail)

        time.sleep(5)  # Update metrik setiap 5 detik

if __name__ == '__main__':
    print("[INFO] Exporter running at http://localhost:9000/metrics")
    start_http_server(9000)  # Endpoint yang akan dibaca oleh Prometheus
    mock_monitoring_loop()
