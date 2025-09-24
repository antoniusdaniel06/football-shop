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
    SESSION_COOKIE_HTTPONLY = True,cookie tidak bisa diakses via JavaScript.
    SESSION_COOKIE_SECURE = True, cookie hanya dikirim lewat HTTPS.
    CSRF_COOKIE_SECURE = True, CSRF cookie juga hanya via HTTPS.
    CSRF_COOKIE_HTTPONLY = True,mengurangi risiko cookie dibaca script.
-Django punya proteksi CSRF token otomatis di form HTML

Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna mengakses aplikasi sebelumnya sesuai dengan status login/logoutnya :
 - Mengimport usercreationform,authenticationmform, authenticate,login,logout
 - Membuat fungsi register. membuat variabel form yang berisi usercreaionform. jika data pada form valid maka akan save dan akan redirect ke halaman loging , jika tidak valid akan meminta user register ulang
 - membuat fungsi login_user. jika method == "POST" maka form akan berisi authenticationform dengan paramter data yang di post. jika form valid , maka akan mengambil user dengan cara form.get_user() lalu memanggil fungsi login dengan parameter request dan user yang sudah diambil. Setelah login akan redirect ke fungsi show_main dan akan set_cookie dengan nama last login berdasarkan date login.
 - membuat fungsi logout_user . memanggil fungsi logout dan akan redirect ke login.setelah redirect last_login akan didelete cookienya.
 - mengimport login_required dan menambahkan @login_required sebelum fungsi show_name, product_detail,product_list dan create product.
 - menambahkan fungsi yang sudah dibuat kedalam urls.py .
Membuat dua (2) akun pengguna dengan masing-masing tiga (3) dummy data menggunakan model yang telah dibuat sebelumnya untuk setiap akun di lokal:
 - register dua akun dan menambahkan 3 product melalu add product.
Menghubungkan model Product dengan User:
- mengimport User didalam models.py dan menambahkan variabel baru di dalam product yaitu user. user didefinisikan sebagai one to many dan jika user dihapus maka semuanya yang berhubungan dengan user tersebut akan dihapus dengan cara on_delete = models.cascade.
- melakukan makemogrations dan migrate
Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last_login pada halaman utama aplikasi :
 - mengubah context dalam fungsi showname menjadi ada last_login yang berisi cookies.get(last_login,never) dan menambahkan username : user.username
 - menampilkan username dan last_login pada main.html.
   



