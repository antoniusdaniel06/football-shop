PWS : https://pbp.cs.ui.ac.id/web/project/antonius.daniel/footballshop

1 Saya mengimplementasikan checklist di atas dengan langkah-langkah berikut : 
  - Membuat direktori terlebih dahulu, lalu membuat file requirements yang akan didownload menggunakan pip isntall.
  - Membuat dan mengaktifkan environment
  - menjalankan django-admin startproject LBM_SHOP .
  - mencoba menjalankan terlebih dahalu dengan cara python manage.py runvserer untuk mengetahui apakah ada ada error atau tidak.
  - membuat app baru dengan cara python manage.py startapp main
  - menambahakn app ke dalam installed apps
  - membuat env prod yang berisi username dan password database dan mengubah bagian database di settings.py.
  - membuat file baru urls.py di main
  - menambahkan method include didalam urls pada LBM_SHOP dan menambahkan path('', include("main.urls")) didalam urlpatterns.
  - membuat function pada views dan membuat dict bernama person berisi nama, npm dan kelas dan function ini akan render main.html dengen context = person
  - membuat folder baru didalam main bernama templates dan menambahkan file main.html
  - mengisi main.html agar bisa menampilkan nama,npm dan kelas berdasarkan person yang sudah saya buat di views.py
  - membuat class baru bernama product berisi name,price,description,thumbnail, category,dan is featured di model.py
  - melakukan migrasi model dengan cara python manage.py makemigrations dan python manage.py migrate.
  - mengimport views didalam urls.py pada main agar bisa memanggil function yang sudah dibuat dengan cara path('',views.show_name, name='show_name').
  - melakukan push ke git hub dan mengkonfigurasi allowed_host berisi link pws.
  - melakukan push ke master pws.
  - membuat file readme.md yang berisi link pws saya dan jawaban dari pertanyaan yang lain.
2. ![IMG_2449](https://github.com/user-attachments/assets/04832a45-e1f3-4de4-84da-e096fb833a76)

3. Peran settings.py di django :
  - menngatur database apa yang akan digunakan oleh project tersebut
  - mengatur lokasi file hmtl pada templates
  - mengatur aplikasi apa saja yang aktif dalam project tersebut
  - mengatur domain apa saja yang diizinkan untuk mengakses project
4. Cara kerja migrasi dalam django adalah pertama kita bisa mengubah models.py lalu menjalankan perintah makemigrations, perintah tersebut akan membandingkan model saat ini dengan migrasi terakhir dan jika ada perubahan akan membuat file baru di folder migrations yang berisi perubahan database. Setelah itu kita harus menjalankan migrate untuk mengubah struktur database sesuai migrasi yang terakhir.
5. Django dijadikan permulaan pembelajaran pengembangan perangkat lunak karena django sudah menyediakan banyak fitur yang mudah digunakan oleh karena itu pengunanya dapat mengembangkan dengan cepat. Django juga menggunakan arsitektur MVT(model view template) yang bisa membantu pengguna untuk mengatur data di dalam model, function untuk merespon apa ketika request dan template untuk mengatur file-file html.[

