PWS : https://antonius-daniel-footballshop.pbp.cs.ui.ac.id/

1. Django AuthenticationForm adalah form yang disediakan django yang berfungsi untuk memvalidasi username dan password yang dimasukan oleh pengguna, mengecek apakah ada di database atau tidak dan memastikan passowrdnya sudah sesuai.
   Kelebihan : mudah digunakan tinggal mengimort saja , sudah otomatis melakukan validasi , password langsung di hashing.
   Kekurangan : Hanya bisa autentikasi username dan password, tampilan yang sederhana , harus kustomisasi jika ingin login dengan email dll.
2. Autentikasi adalah proses memeriksa identitas pengguna contohnya pada login apakah username dan password yang dimasukan pengguna sudah sesuai dengan database. Otorisi adalah menentukan apa saja yang bisa dilakukan oleh pengguna misal jika dia teridentifikasi sebagai admin maka dia bisa CRUD database dll. Django mengimplementasikan autentikasi dengan menyediakan login , logout, authenticationform dll. Otorosiasi yang diimplementasikan di Django adalah seperti decorator login_required, properti seperti user.is_staff,user.is_superuser dll.
3. Kelebihan cookies : mudah diakses, bisa diimplementasikan untuk fitur remember me, tidak terlalu berat untuk server
   Kekurangan cookies : terdapat batas ukuran, mungkin untuk dicuri oleh orang lain , tidak aman untuk data yang berisfat sensitif.
   Kelebihan sessions :Data yang disimpan aman karena berada disimpan di browser, Data yang disimpan bisa lebih banyak
   Kekurangan sessions : membutuhkan penyimpanan tambahan seperti database, dibutuhkan pembersihan sessions lama.
4.Penggunaan cookies tidak selalu aman karena data bisa dicuri dengan cara XXS dan user langsung diambil alih. Django menangani hal tersebut dengan cara :
- Cookie session hanya menyimpan ID (data ada di server).
- Opsi keamanan di settings.py:
    SESSION_COOKIE_HTTPONLY = True → cookie tidak bisa diakses via JavaScript.
    SESSION_COOKIE_SECURE = True → cookie hanya dikirim lewat HTTPS.
    CSRF_COOKIE_SECURE = True → CSRF cookie juga hanya via HTTPS.
    CSRF_COOKIE_HTTPONLY = True → mengurangi risiko cookie dibaca script.
-Django punya proteksi CSRF token otomatis di form HTML
   



