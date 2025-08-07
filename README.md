# mr-project-carmen-2
Kode Sumber untuk Artikel Medium saya yang berjudul "Optimasi Portofolio Sederhana pada Pasar Saham Indonesia". Kode sumber ini dapat Anda gunakan untuk melakukan replikasi pada hasil pada artikel tersebut maupun untuk melakukan optimasi secara mandiri.

## Cara Menggunakan

Jika Anda berencana untuk mereplikasi hasil yang ada pada artikel "Optimasi Portofolio Sederhana pada Pasar Saham Indonesia", maka anda dapat menjalankan/run `playground.py` saja, tanpa harus mengubah variabel lainnya.

Jika Anda ingin melakukan optimasi portofolio secara mandiri, ubah variabel berikut pada `playground.py`:

* `to_download` : berisi saham apa saja yang ingin dipertimbangkan untuk masuk dalam portofolio. Meskipun Anda bisa menggunakan data saham apa saja yang tersedia di yahoo finance, perhatikan bahwa Anda hanya bisa membandingkannya dengan IHSG.
* `start_str` : tanggal awal dari data yang akan didownload.
* `end_str` : tanggal akhir dari data yang akan didownload.

Perhatikan bahwa data yang didownload mulai dari tanggal pada `start_str` hingga 1 hari sebelum `end_str`. Untuk menentukan periode data yang diunduh, disarankan agar ...
1. banyak harinya minimal 10 * (banyak saham yang dipertimbangkan)
2. banyak bulannya minimal 2 kali dari input month_out

* `download_path` : nama folder tempat menyimpan data yang didownload.
* `month_out` : banyak bulan untuk dijadikan data outsample. Harus bilangan bulat (integer) lebih dari 0

Anda wajib menjalankan fungsi `download_data` jika baru pertama kali menjalankan program ini. Fungsi `plot_bobot` bersifat fungsional. Anda mungkin perlu meg-close beberapa plot yang muncul agar program berjalan/berhenti dengan sempurna.
