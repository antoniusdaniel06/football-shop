PWS : https://pbp.cs.ui.ac.id/web/project/antonius.daniel/footballshop
1 Saya mengimplementasikan checklist di atas dengan langkah-langkah berikut : 
  - Mmebuat direktori terlebih dahulu, lalu membuat file requirements yang akan didownload menggunakan pip isntall.
  - Membuat dan mengaktifkan environment
  - menjalankan django-admin startproject LBM_SHOP .
  - mencoba menjalan terlebih dahalu dengan cara python manage.py runvsere untuk mengetahui apakah ada ada error atau tidak.
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
3. Peran settings.py di django :
  - menngatur database apa yang akan digunakan oleh project tersebut
  - mengatur lokasi file hmtl pada templates
  - mengatur aplikasi apa saja yang aktif dalam project tersebut
  - mengatur domain apa saja yang diizinkan untuk mengakses project
