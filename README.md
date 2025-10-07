PWS : https://antonius-daniel-footballshop.pbp.cs.ui.ac.id/

1. perbedaan antara synchronous request dan asynchronous request adalah untuk synchronous request, browser harus menunggu dari server lain ketika mau melakukan hal lain. Biasanya halaman aka di refresh ketika ada request. Sedangkan asynchronous request browser bisa lanjut aktivitas sambil memproses server, tidak refresh halaman dan hanya memperbarui sebagian data.
2. Cara bekerja AJAX di django adalah user melakukan sebuah aksi di halaman,javascript mengirim request ke URL django menggunakan fetch,view akan return jsonrespone, javascript menerima json dan menampilkan hasilnya di halaman.
3. keuntungan menggunakan AJAX dibandingkan render biasa di Django adlaah tidak perlu refresh halaman lagi, lebih ringan karena hanya data yang dikirim melalui jsonrespone,lebih interaktif dan lebih cepat.
4. cara memastikan keamanan AJAX adalah menggunakan csrf token, menggunakann decorator require_post agar hanya menerima post pada form sensitif, jangan mengirim data sensitif menggunakan jsonrespone.
5. AJAX akan memnbuat pengguna lebih nyaman karena jika melakukan aksi sesuatu akan terasa lebih cepat dna tanpa hambatan.
