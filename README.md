PWS : https://pbp.cs.ui.ac.id/web/project/antonius.daniel/footballshop

1. fungsi data delivery dalam sebuah platform :
    - untuk bertukar informasi antara frontend dan backend
    - data delivery memungkinkan untuk integrasi dengan sistem lain seperti pembayaran,autentikasi dll.
    - data delivery bisa dijadikan sebagai informasi yang ditampilkan kepada user

2. menurut saya json lebih baik dan lebih populer dibandingkan dengan xml karena lebih ringkas sehingga lebih mudah dibaca oleh manusia, lebih mudah diintegrasikan denga  REST API, lebih didukung oleh banyak framework/

3.fungsi is_valid dalam form django adalah untuk melihat apakah user sudah mengisi semua field yang ada dan memastikan data yang diisi sudah valid. Jika is_valid sudah return True maka kita bisa melakukan simpan data dengan save.

4. kita membutuhkan csrf_token pada django karena saat server menerima request , token ini akan dijadikan sebagai patokan, jika token tidak cocok maka django akan menolak request. Jika kita tidak menggunakan csrf_token maka server bisa menerima request yang merupakan halaman palsu yang dibuat oleh penyerang. penyerang memanfaatkan tersebut karena server tidak akan mengetahui mana yang merupakan request  yang valid.

5. -Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID :
        - improt httpresponse untuk return dan serializers untuk mengubah format data.
        - mengimport product dari .models
        - membuat fungsi show_xml dan show_json 
        -mengambil semua data dari product dan masukan ke varibael products
        - membuat variabel yang serialize product ke xml dan json lalu return variabel tersebut dengan httpresponse
        -membuat fungsi show_xml_by_id dan show_json_by_id dengan parameter request dan id 
        -prosesnya sama seperti yang show_json atau show_xml tetapi menggunakan try except karena dengan id tertentu data belum tentu ada
    -Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 1
        -membuat path dengan nama xml,json,xml/<int:id>, json/<int:id> dengan memanggil fungsi yang sudah saya buat tadi.
    -Membuat halaman yang menampilkan data objek model yang memiliki tombol "Add" yang akan redirect ke halaman form, serta tombol "Detail" pada setiap data objek model yang akan menampilkan halaman detail objek.
        - membuat product_list di template yang berfungsi untuk menampilkan semua product
        - menamnbahkan button pada main.html degan nama products dan jika ditekan dia akan direct ke halam product list.
    -Membuat halaman form untuk menambahkan objek model pada app sebelumnya.
        -menambahkan form.html didalam templates
        -membuat form method = "post"
        - memasukan csrf_token agar hanya menerima request yang valid
        = menambahkan form.as_table 
    -  Membuat halaman product_detail.html yang menampilkan detail dari setiap data objek model.
        - didalam product_list.html saya menambahkan href yang akan direct ke url prodct_detail dengan p.pk yang akan di pass. jadi di route products<int:pk> pk akan dipass sesuai p.pk sesuai href yang tadi. Halaman product_detail akan menampilkan semua detail yang dimiliki oleh barang tersebut.

Postman xml seleuruh product
<img width="1905" height="875" alt="image" src="https://github.com/user-attachments/assets/4e77514f-9ea2-404c-b4b9-d4e7946dc08f" />
Postman xml dengan id 4
<img width="1913" height="810" alt="image" src="https://github.com/user-attachments/assets/56ea86e8-5114-4fbd-99a3-c4af7d65e386" />
Postman json seluruh product 
<img width="1447" height="828" alt="image" src="https://github.com/user-attachments/assets/acf43f8a-9732-4fd8-9902-af5c829d202b" />
Postman json dengan id 3
<img width="1432" height="821" alt="image" src="https://github.com/user-attachments/assets/da3180d6-eff4-42ea-a702-dd327f14c632" />



