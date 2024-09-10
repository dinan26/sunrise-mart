- Nama : Dinda Dinanti
- NPM : 2306245440
- Kelas : PBP C

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   1. Membuat suatu repository Github yang baru terserah kita, saya pribadi bernama sunrisemart
   2. Melakukan clone pada repository tersebut ke komputer
   3. Membuat virtual environment dengan menjalankan command berikut :
        python3 -m venv env
   4. Mengaktifkan virtual environment dengan command :
        source env/bin/activate
   5. Mempersiapkan requirements dengan menambahkan isi dari berkas :
         django
         gunicorn
         whitenoise
         psycopg2-binary
         requests
         urllib3
   6. Meng-install requirements dengan pip :
        Python3 -m pip install -r requirements.txt
   7. Membuat proyek Django baru dengan command:
     django-admin startproject sunrisemart 
   8. Menambahkan string pada ALLOWED_HOSTS di settings.py :
        ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
   9. Membuat aplikasi baru main dengan menggunakan command :
        python3 manage.py startapp main
   10. Menambahkan aplikasi ke INSTALLED_APPS pada file settings.py
   11. Membuat direktori baru dengan nama templates pada direktori aplikasi main
   12. Membuat file baru pada direktori templates tadi dengan berkas main.html yang nanti nya akan berguna untuk menampilkan data dari program sunrisemart :
         <h1>{{ app_name }} Page</h1>
   
         <h5>Name: </h5>
         <p>{{ name }}<p>
         <h5>Class: </h5>
         <p>{{ class }}<p>
   13. Mengubah berkas models.py :
         from django.db import models
   
         class Product(models.Model):
            name = models.CharField(max_length = 255)
            price = models.IntegerField()
            description = models.TextField()
            stock = models.IntegerField()
            rating = models.DecimalField(max_digits= 3, decimal_places=2, null= True, blank= True)
   14. Menambahkan fungsi untuk me-render main pada file views.py:
         from django.shortcuts import render
   
         def show_main(request):
            context = {
               'npm' : '2306245440',
               'name': 'Dinda Dinanti',
               'class': 'PBP C'
            }
            return render(request, "main.html", context)
   15. Melakukan routing di file urls.py yang terdapat pada direktori sunrisemart, dengan isi file urls.py menjadi :
         from django.contrib import admin
         from django.urls import path, include
   
         urlpatterns = [
            path('admin/', admin.site.urls),
            path('', include('main.urls')),
         ]
   16. Melakukan test dengan command :
         python3 manage.py runserver
         kemudian membuka http://localhost:8000/ di safari
   17. Deployment ke PWS

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
   ![image](https://github.com/user-attachments/assets/6bc71c44-23ec-438f-97f3-3d4da52cad0f)


3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
   Git adalah sebuah sistem kontrol versi yang terdistribusi dan tentunya sangat penting dalam pengembangan perangkat lunak.
   Fungsi utama dari git itu sendiri adalah memungkinkan para pengembang untuk bekerja bersama-sama pada proyek yang sama tanpa khawatir
   akan merusak kode atau mencampurnya, sehingga dapat memfasilitasi kerja tim dan memungkinkan pengembang untuk berkolaborasi secara efisien.
   Selain itu, Git juga memungkinkan penyimpanan proyek dalam folder berurutan seperti V1, V2, V3, dengan satu proyek yang menggunakan database
   khusus berisi semua versi file, sehingga membantu mengorganisir kode sumber dan memudahkan pengembang untuk melacak perubahan. Dengan demikian,
   Git menjadi platform fleksibilitas yang dapat digunakan sebagai platform hosting seperti GitHub, memungkinkan pengembang untuk menghosting berbagai
   proyek dengan mudah. Selain itu, Git juga berfungsi sebagai salinan cadangan, sehingga jika terjadi masalah saat mengembangkan versi terbaru, Git dapat
   dengan mudah mengembalikan ke versi sebelumnya. Dengan optimalitas kinerja, keamanan, dan fleksibilitas, Git menjadi sistem kontrol yang paling populer
   dan banyak digunakan dalam pengembangan perangkat lunak.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
   Django dijadikan sebagai pilihan awal dalam pembelajaran pengembangan perangkat lunak karena beberapa alasan yang signifikan.
   Pertama, Django adalah framework berbasis Python yang terkenal dengan kemudahan penggunaan dan sintaks yang sederhana.
   Dengan arsitektur Model-View-Template (MVT), Django memisahkan logika aplikasi dari tampilan dan data, yang membantu pengembang
   memahami struktur aplikasi dengan lebih baik. Selain itu, Django dilengkapi dengan banyak fitur bawaan seperti sistem autentikasi,
   manajemen sesi, dan Object-Relational Mapping (ORM), yang memungkinkan pengembang untuk fokus pada logika bisnis tanpa harus menulis
   kode dari awal. Dengan semua keunggulan ini, Django menjadi pilihan yang ideal.

7. Mengapa model pada Django disebut sebagai ORM?
   Model pada Django disebut sebagai ORM (Object Relational Mapping) karena fungsinya yang menghubungkan antara objek dalam kode Python
   dan tabel dalam basis data relasional. Dengan ORM, developer bisa ngelola database pake objek dan atribut Python tanpa harus nulis
   query SQL langsung. Setiap model di Django didefinisiin sebagai kelas Python, di mana atribut-atributnya ngegambarin kolom di tabel database.
   Jadi, lebih gampang buat ngelola data, karena operasi kayak bikin, baca, update, atau hapus data bisa dilakukan dengan metode yang berbasis objek,
   bikin proses pengembangan lebih cepat dan minim error. Django ORM juga secara otomatis bikin perintah SQL yang diperlukan, jadi developer bisa lebih
   fokus ke logika aplikasi daripada detail implementasi database. 
   
