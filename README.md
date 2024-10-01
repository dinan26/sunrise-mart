- Nama : Dinda Dinanti
- NPM : 2306245440
- Kelas : PBP C

Berikut link pws yang sudah berhasil di deploy https://pbp.cs.ui.ac.id/web/project/dinda.dinanti/sunrisemart

<details>
  <summary>TUGAS 2</summary>
   
**TUGAS INDIVIDU 2**

**1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
   - Membuat suatu repository Github yang baru terserah kita, saya pribadi bernama sunrisemart
   - Melakukan clone pada repository tersebut ke komputer
   - Membuat virtual environment dengan menjalankan command berikut :
         python3 -m venv env
   - Mengaktifkan virtual environment dengan command :
         source env/bin/activate
   - Mempersiapkan requirements dengan menambahkan isi dari berkas :
         django
         gunicorn
         whitenoise
         psycopg2-binary
         requests
         urllib3
   - Meng-install requirements dengan pip :
         Python3 -m pip install -r requirements.txt
   - Membuat proyek Django baru dengan command:
         django-admin startproject sunrisemart 
   - Menambahkan string pada ALLOWED_HOSTS di settings.py :
         ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
   - Membuat aplikasi baru main dengan menggunakan command :
         python3 manage.py startapp main
   - Menambahkan aplikasi ke INSTALLED_APPS pada file settings.py
   - Membuat direktori baru dengan nama templates pada direktori aplikasi main
   - Membuat file baru pada direktori templates tadi dengan berkas main.html yang nanti nya akan berguna untuk menampilkan data dari program sunrisemart :
         <h1>{{ app_name }} Page</h1>
   
         <h5>Name: </h5>
         <p>{{ name }}<p>
         <h5>Class: </h5>
         <p>{{ class }}<p>
   - Mengubah berkas models.py :
         from django.db import models
   
         class Product(models.Model):
            name = models.CharField(max_length = 255)
            price = models.IntegerField()
            description = models.TextField()
            stock = models.IntegerField()
            rating = models.DecimalField(max_digits= 3, decimal_places=2, null= True, blank= True)
   - Menambahkan fungsi untuk me-render main pada file views.py:
         from django.shortcuts import render
   
         def show_main(request):
            context = {
               'npm' : '2306245440',
               'name': 'Dinda Dinanti',
               'class': 'PBP C'
            }
            return render(request, "main.html", context)
   - Melakukan routing di file urls.py yang terdapat pada direktori sunrisemart, dengan isi file urls.py menjadi :
         from django.contrib import admin
         from django.urls import path, include
   
         urlpatterns = [
            path('admin/', admin.site.urls),
            path('', include('main.urls')),
         ]
   - Melakukan test dengan command :
         python3 manage.py runserver
         kemudian membuka http://localhost:8000/ di safari
   - Deployment ke PWS

**2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.**
   ![image](https://github.com/user-attachments/assets/6bc71c44-23ec-438f-97f3-3d4da52cad0f)
Diagram yang saya buat menjelaskan alur penanganan request dari client hingga menghasilkan output yang sesuai dengan keinginan client.
Proses ini dimulai ketika user mengirimkan request melalui internet,saat mereka mengakses website dan mengirimkan permintaan HTTP ke server. Setelah permintaan diterima, web server memprosesnya dan meneruskannya ke aplikasi Django. Selanjutnya, Django memulai proses request-response dengan memeriksa file ⁠urls.py untuk mencocokkan URL yang diminta dengan pola URL yang telah terdaftar. Jika URL tersebut cocok, Django meneruskan permintaan view di views.py, dimana argumen-argumen dari request diekstraksi dan diteruskan ke view. View dilanjutkan dengan proses pada models.py untuk mengambil data yang relevan dari database. Setelah data berhasil diambil, data tersebut dikirim kembali ke view dan kemudian diteruskan ke template HTML untuk ditampilkan kepada user. Akhirnya, setelah template diisi dengan data yang sesuai, Django mengirimkan respons HTTP yang berisi HTML kembali ke user, sehingga hasil permintaan dapat dilihat di browser mereka.

**3. Jelaskan fungsi git dalam pengembangan perangkat lunak!**
   Git adalah sebuah sistem kontrol versi yang terdistribusi dan tentunya sangat penting dalam pengembangan perangkat lunak.
   Fungsi utama dari git itu sendiri adalah memungkinkan para pengembang untuk bekerja bersama-sama pada proyek yang sama tanpa khawatir
   akan merusak kode atau mencampurnya, sehingga dapat memfasilitasi kerja tim dan memungkinkan pengembang untuk berkolaborasi secara efisien.
   Selain itu, Git juga memungkinkan penyimpanan proyek dalam folder berurutan seperti V1, V2, V3, dengan satu proyek yang menggunakan database
   khusus berisi semua versi file, sehingga membantu mengorganisir kode sumber dan memudahkan pengembang untuk melacak perubahan. Dengan demikian,
   Git menjadi platform fleksibilitas yang dapat digunakan sebagai platform hosting seperti GitHub, memungkinkan pengembang untuk menghosting berbagai
   proyek dengan mudah. Selain itu, Git juga berfungsi sebagai salinan cadangan, sehingga jika terjadi masalah saat mengembangkan versi terbaru, Git dapat
   dengan mudah mengembalikan ke versi sebelumnya. Dengan optimalitas kinerja, keamanan, dan fleksibilitas, Git menjadi sistem kontrol yang paling populer
   dan banyak digunakan dalam pengembangan perangkat lunak.

**4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?**
   Django dijadikan sebagai pilihan awal dalam pembelajaran pengembangan perangkat lunak karena beberapa alasan yang signifikan.
   Pertama, Django adalah framework berbasis Python yang terkenal dengan kemudahan penggunaan dan sintaks yang sederhana.
   Dengan arsitektur Model-View-Template (MVT), Django memisahkan logika aplikasi dari tampilan dan data, yang membantu pengembang
   memahami struktur aplikasi dengan lebih baik. Selain itu, Django dilengkapi dengan banyak fitur bawaan seperti sistem autentikasi,
   manajemen sesi, dan Object-Relational Mapping (ORM), yang memungkinkan pengembang untuk fokus pada logika bisnis tanpa harus menulis
   kode dari awal. Dengan semua keunggulan ini, Django menjadi pilihan yang ideal.

**5. Mengapa model pada Django disebut sebagai ORM?**
   Model pada Django disebut sebagai ORM (Object Relational Mapping) karena fungsinya yang menghubungkan antara objek dalam kode Python
   dan tabel dalam basis data relasional. Dengan ORM, developer bisa ngelola database pake objek dan atribut Python tanpa harus nulis
   query SQL langsung. Setiap model di Django didefinisiin sebagai kelas Python, di mana atribut-atributnya ngegambarin kolom di tabel database.
   Jadi, lebih gampang buat ngelola data, karena operasi kayak bikin, baca, update, atau hapus data bisa dilakukan dengan metode yang berbasis objek,
   bikin proses pengembangan lebih cepat dan minim error. Django ORM juga secara otomatis bikin perintah SQL yang diperlukan, jadi developer bisa lebih
   fokus ke logika aplikasi daripada detail implementasi database. 

</details>


<details>
  <summary>TUGAS 3</summary>

**TUGAS INDIVIDU 3**

**1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**
   Data delivery sangat penting untuk pengoperasian sebuah platform karena bertanggung jawab untuk memastikan bahwa data dapat dikirimkan dengan cepat, aman, dan efisien antara      berbagai bagian atau layanan yang ada. Alasan pertama adalah untuk memastikan informasi yang diperlukan tepat waktu; ini sangat penting untuk platform e-commerce seperti itu,     di mana gudang, sistem pengiriman, dan pembayaran perlu segera menghubungi pelanggan dengan data pesanan mereka. Penyebaran data adalah bagian penting dari integrasi antar        komponen platform. Sebagian besar platform terdiri dari banyak komponen yang harus berkomunikasi satu sama lain, seperti layanan API, frontend, dan backend. Jika komponen-        komponen ini tidak dapat berbagi data dengan baik, hal itu dapat menyebabkan kesalahan atau kegagalan sistem.

   Data delivery juga meningkatkan kinerja platform dan meningkatkan efisiensi. Platform dapat menghindari penggunaan bandwidth dan sumber daya yang berlebihan dengan sistem         pengiriman data yang baik. Untuk meningkatkan efisiensi, data dikirim hanya dalam jumlah yang diperlukan dan pada waktu yang tepat. Penyebaran data sangat penting karena          keamanan. Sangat penting untuk memastikan bahwa data dilindungi saat ditransfer dari satu platform ke platform lainnya, terutama ketika melibatkan informasi sensitif seperti      data pribadi atau keuangan. Pengiriman data yang aman memastikan bahwa pihak yang tidak berwenang tidak dapat mengaksesnya.
         
**2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?**
   JSON menjadi lebih populer dibandingkan XML karena sejumlah alasan penting. Pertama, JSON memiliki sintaks yang lebih sederhana dan mudah dipahami, membuatnya lebih fleksibel     dan cepat dalam proses parsing.XML menggunakan elemen dan tag, seperti <element></element>, membuatnya lebih sulit dibaca dan dipahami secara visual. Kecepatan dan efisiensi      JSON juga menjadi alasan utamanya. XML memerlukan parser yang lebih rumit, sehingga prosesnya lebih lambat dan mengonsumsi lebih banyak sumber daya. Akibatnya, JSON menawarkan    penggunaan sumber daya komputasi yang lebih efisien dan lebih cocok untuk aplikasi yang membutuhkan respons cepat. Keamanan juga menjadi faktor yang mendukung popularitas         JSON. Dengan sintaks yang lebih sederhana dan kurang kompleks, JSON mengurangi risiko kesalahan keamanan. Oleh karena itu, JSON lebih aman untuk digunakan dalam pengiriman        data yang bersifat sensitif.
   
   Secara keseluruhan, JSON lebih populer karena keunggulannya dalam hal kesederhanaan, kecepatan, efisiensi, kompatibilitas, dan keamanan. Meskipun XML masih memiliki manfaat       dalam beberapa aplikasi tertentu, JSON lebih sesuai untuk sebagian besar penggunaan modern.

**3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?**
   Metode "is_valid()" pada form Django berfungsi untuk memvalidasi data yang dikirimkan melalui form. Metode ini digunakan untuk memastikan bahwa data yang dikirimkan sesuai        dengan aturan dan konfigurasi yang telah ditentukan dalam form. Setelah dari diisi dan dikirimkan, Django memproses data dan mengecek apakah semua kolom yang perlu diisi telah    diisi dengan benar, jadi method `is_valid()` akan mengembalikan nilai `True`, menunjukkan bahwa data tersebut valid. Sebaliknya, jika ada field yang tidak diisi atau tidak        sesuai dengan aturan, maka method ini akan mengembalikan nilai `False`, menunjukkan bahwa data tersebut tidak valid.

   Jadi, Metode "is_valid()" diperlukan karena memungkinkan pengawasan dan pengendalian yang efektif atas kesalahan validasi. Metode "is_valid()" adalah bagian penting dari          pengembangan aplikasi karena memungkinkan untuk menampilkan pesan kesalahan yang spesifik kepada pengguna sehingga mereka dapat memperbaiki kesalahan tersebut.

**4. Mengapa kita membutuhkan csrf_token saat membuat form di Django?Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?**
   Untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF), kita menggunakan "csrf_token" saat membuat form Django. CSRF adalah jenis serangan yang memungkinkan    penyerang mengirimkan permintaan ke server Anda tanpa izin pengguna yang terautentikasi. Dengan menggunakan "csrf_token", Django dapat memastikan bahwa permintaan yang            diterima berasal dari pengguna yang terautentikasi dan bukan dari sumber lain yang tidak sah.

   Serangan CSRF dapat terjadi pada aplikasi kita jika kita tidak memasukkan "csrf_token" ke dalam format Django. Penyerang dapat mengirimkan permintaan ke server Anda dengan        menggunakan token yang diperoleh dari cookie pengguna yang terautentikasi. Hal ini dapat memungkinkan pencuri untuk melakukan hal-hal yang tidak diinginkan, seperti mulai         mengirimkan dana, mengubah email, atau hal lainnya yang dapat mengancam keamanan pengguna.

   Saat membuat form Django, kita membutuhkan "csrf_token". Penyerang dapat memanfaatkan kekurangan ini dengan mengirimkan permintaan ke server Anda menggunakan token yang          diperoleh dari cookie pengguna. Misalnya, mereka dapat mengirimkan permintaan untuk mengubah email pengguna atau melakukan transfer dana tanpa izin pengguna yang       terautentikasi. Oleh karena itu, pengguna tidak akan mengetahui bahwa penyerang melakukan tindakan tersebut.

**5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
   1. Buat direktori baru di direktori utama yang berisikan folder base.html
      
   2. Pada subdirektori settings.py, yang ada pada direktori sunrire_mart :
      ```
      'DIRS': [BASE_DIR / 'templates'], # Tambahkan konten baris ini
      ```
      
   3. Pada subdirektori templates yang ada pada direktori main, ubahlah kode berkas main.html:
       ```
       {% extends 'base.html' %}
       {% block content %}
       <h1>Mental Health Tracker</h1>
      
       <h5>NPM: </h5>
       <p>{{ npm }}<p>
      
       <h5>Name:</h5>
       <p>{{ name }}</p>
      
       <h5>Class:</h5>
       <p>{{ class }}</p>
       {% endblock content %}
       ```
       
   4. Tambahkan baris berikut pada berkas models.py di subdirektori main.
      ``` 
      import uuid  # tambahkan baris ini di paling atas
       id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
      ```
      
   5. Membuat Forms
      - Buat file forms.py di dalam direktori main.
      - Tambahkan fields dari forms yang berasal dari class Product yang telah dideklarasikan di models.py.
        ```
        from django.forms import ModelForm
        from main.models import Product

        class ProductForm(ModelForm):
           class Meta:
                 model = Product
                 fields = ["nama", "deskripsi", "stock", "harga" ]
        ```
        
   6. Membuat Fungsi create_page di views.py
      - Buat fungsi baru di views.py dengan nama create_product
        ```
        def create_page(request):
          form = ProductForm(request.POST or None)

          if form.is_valid() and request.method == "POST":
              form.save()
              return redirect('main:show_main')

          context = {'form': form}
          return render(request, "create_page.html", context)
        ```
        Nantinya fungsi ini akan me-render tampilan dari form pada template HTML.

   7. Membuat Template HTML untuk create_product
      - Buat file HTML sebagai template untuk form yang akan dirender oleh fungsi create_page.
        ``` {% extends 'base.html' %} 
         {% block content %}
         <h1>Add New Product</h1>
         
         <form method="POST">
           {% csrf_token %}
           <table>
             {{ form.as_table }}
             <tr>
               <td></td>
               <td>
                 <input type="submit" value="Add Product" />
               </td>
             </tr>
           </table>
         </form>
         {% endblock %}
         ```
   8. Menambahkan Button pada main.html
      - Tambahkan tombol pada halaman main.html yang akan mengarahkan pengguna ke halaman yang berisi form untuk menambahkan produk.
        ```
        <a href="{% url 'main:create_page' %}">
         <button>Add New Product</button>
       </a>
       

  9. Menambahkan Fungsi Tampilan dalam Format XML dan JSON
      - Buat 4 fungsi baru: show_xml, show_json, show_xml_by_id, dan show_json_by_id.
     ```
      def show_xml(request):
          data = Product.objects.all()
          return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
     ```
        - show_xml untuk menampilkan representasi seluruh products dalam format XML, dapat diakses pada (url)/xml
      ```
      def show_json(request):
          data = Product.objects.all()
          return HttpResponse(serializers.serialize("json", data), content_type="application/json")
      ```
      - show_json untuk menampilkan representasi seluruh products dalam format JSON, dapat diakses pada (url)/json
      ```
      def show_xml_by_id(request, id):
          data = Product.objects.filter(pk=id)
          return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
      ```
      - show_xml_by_id untuk menampilkan representasi product dengan id yang diinginkan dalam format XML, dapat diakses pada (url)/xml/(desired_id)
      ```
      def show_json_by_id(request, id):
          data = Product.objects.filter(pk=id)
          return HttpResponse(serializers.serialize("json", data), content_type="application/json")
      ```
      - show_json_by_id untuk menampilkan representasi product dengan id yang diinginkan dalam format JSON, dapat diakses pada (url)/json/(desired_id)
    
   10. Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
       ```
       path('create-page', create_page, name='create_page'),
       path('xml/', show_xml, name='show_xml'),
       path('json/', show_json, name='show_json'),
       path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
       path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
       ```

**Mengakses URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md**

**1. POSTMAN XML**
   <img width="1440" alt="Screenshot 2024-09-18 at 05 51 24" src="https://github.com/user-attachments/assets/5330f82b-9abd-4e36-b514-9ea96d4d5bb2">

**2. POSTMAN JSON**
   <img width="1440" alt="Screenshot 2024-09-18 at 05 51 41" src="https://github.com/user-attachments/assets/9882def2-32ec-4045-988a-56b9195f18ec">

**3. POSTMAN XML By ID**
   <img width="1440" alt="Screenshot 2024-09-18 at 05 51 47" src="https://github.com/user-attachments/assets/f1e10577-fe1a-4142-9aa3-f29fbafe6f44">

**4. POSTMAN JSON By ID**
   <img width="1440" alt="Screenshot 2024-09-18 at 05 52 01" src="https://github.com/user-attachments/assets/e9a09213-bb44-45ca-b128-82c426e6e491">
</details>


<details>
  <summary>TUGAS 4</summary>
  
**TUGAS INDIVIDU 4**

**1. Apa perbedaan antara HttpResponseRedirect() dan redirect() ?**

      HttpResponseRedirect dan redirect adalah dua alat dalam Django yang digunakan untuk melakukan pengalihan (redirect), namun keduanya memiliki perbedaan tertentu. 
      Dari segi fungsi dan penggunaan, **HttpResponseRedirect** merupakan kelas yang mengembalikan respons HTTP dengan status kode 302 (Found), yang menandakan bahwa halaman yang       diminta telah dipindahkan ke lokasi lain. Untuk menggunakannya, Anda perlu menginstansiasi kelas ini dan memasukkan URL tujuan ke dalam konstruktornya. Sementara itu,             **redirect** adalah sebuah fungsi yang merupakan jalan pintas (shortcut) dari HttpResponseRedirect. Fungsi ini lebih sederhana digunakan karena tidak memerlukan instansiasi       kelas secara manual, cukup dengan menyertakan URL tujuan di dalam fungsinya. 
      Dari segi sintaks, **HttpResponseRedirect** ditulis sebagai HttpResponseRedirect('/path/to/new/location'), sedangkan **redirect** lebih ringkas dengan penulisan         redirect('/path/to/new/location'). Dalam hal kemudahan, **redirect** lebih praktis karena sintaksnya lebih sederhana dan intuitif, sehingga lebih sesuai untuk penggunaan sehari-hari dalam pengembangan aplikasi Django.

**2. Jelaskan cara kerja penghubungan model Product dengan User!**

Menggunakan ForeignKey yang nantinya akan mengizinkan setiap produk terhubung dengan satu pengguna. Hal ini memungkinkan pengguna dapat memiliki banyak produk dan dapat dengan mudah mengakses produk-produk tersebut. Biasanya kita melakukan pada file berikut :

      from django.db import models
      from django.contrib.auth.models import User
      
      class Product(models.Model):
          name = models.CharField(max_length=100)
          description = models.TextField()
          price = models.DecimalField(max_digits=10, decimal_places=2)
          user = models.ForeignKey(User, on_delete=models.CASCADE)
      
          def __str__(self):
              return self.name


**3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? 
     Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.**

  **Authentication**: Proses verifikasi identitas pengguna. Ini biasanya dilakukan dengan memeriksa kredensial seperti username dan password.
  Dalam Django, authentication ditangani oleh sistem authentication bawaan yang memverifikasi kredensial pengguna melalui model User. Jika kredensial benar, Django membuat  pengguna yang valid, menyimpan informasi pengguna, dan memungkinkan mereka mengakses sistem.

**Authorization**: Proses menentukan apakah pengguna yang telah terautentikasi memiliki izin untuk mengakses sumber daya tertentu.
  Django menyediakan sistem otorisasi berbasis izin (permissions) yang melekat pada pengguna dan grup pengguna. Anda bisa mengatur aturan izin untuk model atau tampilan (views) tertentu.

**Proses Login :**
Ketika pengguna login, Django akan memverifikasi kredensial pengguna (authentication). Jika kredensial benar, sesi login dibuat dan pengguna diberi akses ke sistem. Setelah itu, untuk setiap tindakan atau halaman, Django akan memeriksa apakah pengguna memiliki izin yang sesuai (authorization) untuk melakukan tindakan atau mengakses halaman tersebut

**Implementasi Authentication dan Authorization di Django**

**Authentication**: Django menyediakan sistem autentikasi bawaan yang mencakup model ⁠ User ⁠, form login, dan middleware untuk mengelola sesi pengguna.

     
    from django.contrib.auth import authenticate, login
  
    def my_view(request):
        user = authenticate(username='john', password='secret')
        if user is not None:
            login(request, user)
     ⁠ 
**Authorization**: Django menggunakan izin (permissions) dan grup (groups) untuk mengelola akses pengguna.

    ⁠ 
    from django.contrib.auth.decorators import permission_required
  
    @permission_required('app_label.permission_code')
    def my_view(request):
        # View code here
   
Jadi karena adanya modul django.contrib.auth, Django menyediakan sistem authentication yang detail,
dan memungkinkan pengembang dengan mudah mengelola authentication.

**4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?**

Django menggunakan sesi (sessions) dan cookies untuk mengingat pengguna yang telah login. Saat pengguna login, 
Django membuat sesi baru dan menyimpan ID sesi di cookie pengguna. Setiap kali pengguna membuat permintaan baru, 
cookie ini dikirim kembali ke server, memungkinkan Django untuk mengidentifikasi pengguna.

Selain untuk melacak sesi pengguna yang login, cookies memiliki berbagai fungsi lain, seperti menyimpan preferensi pengguna 
(seperti bahasa), melacak aktivitas pengguna untuk keperluan analitik, serta menyimpan informasi otentikasi agar pengguna 
tetap login untuk jangka waktu yang lebih lama. Cookies juga sering digunakan untuk menampilkan iklan yang disesuaikan dengan perilaku
browsing pengguna. 

Namun, tidak semua cookies aman. Cookies dapat rentan jika menyimpan informasi sensitif dalam bentuk teks biasa,
atau jika digunakan di jaringan yang tidak aman, yang membuatnya rentan terhadap serangan.Untuk meningkatkan keamanan, 
Django dan aplikasi web lainnya biasanya menerapkan langkah-langkah seperti menambahkan flag **Secure**, sehingga cookies hanya
dikirim melalui koneksi HTTPS, menggunakan flag **HttpOnly** agar JavaScript tidak bisa mengakses cookies,Pengelolaan cookies yang
aman sangat penting untuk melindungi privasi dan keamanan data pengguna.

**5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

**1. Membuat Fungsi Register**

- Tambahkan import baru pada file views.py
    ```
   from django.contrib.auth.forms import UserCreationForm
   from django.contrib import messages
    ```
- Buat fungsi baru di views.py dengan nama register
    ```
   def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
    ```
- Buat file HTML baru dengan nama register.html
   
     ```{% extends 'base.html' %}
        {% block meta %}
        <title>Register</title>
        {% endblock meta %}
        
        {% block content %}
        
        <div class="login">
          <h1>Register</h1>
        
          <form method="POST">
            {% csrf_token %}
            <table>
              {{ form.as_table }}
              <tr>
                <td></td>
                <td><input type="submit" name="submit" value="Daftar" /></td>
              </tr>
            </table>
          </form>
        
          {% if messages %}
          <ul>
            {% for message in messages %}
            <li>{{ message }}</li>
            {% endfor %}
          </ul>
          {% endif %}
        </div>
        
        {% endblock content %}
     ```

- Lakukan import pada file urls.py yang ada pada subdirektori main
      ```
   from main.views import register
      ```

   Tambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi:
    ```
    urlpatterns = [
     ...
     path('register/', register, name='register'),
     ]
    ```

**2. Membuat Fungsi Login**

- Tambahkan import baru pada file views.py kembali
    ```
  from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
  from django.contrib.auth import authenticate, login
    ```
- Buat fungsi baru di views.py dengan nama register :
    ```
  def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:show_main')

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
    ```
- Buat file HTML baru dengan nama login.html
    ```{% extends 'base.html' %}
        
        {% block meta %}
        <title>Login</title>
        {% endblock meta %}
        
        {% block content %}
        <div class="login">
          <h1>Login</h1>
        
          <form method="POST" action="">
            {% csrf_token %}
            <table>
              {{ form.as_table }}
              <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login" /></td>
              </tr>
            </table>
          </form>
        
          {% if messages %}
          <ul>
            {% for message in messages %}
            <li>{{ message }}</li>
            {% endfor %}
          </ul>
          {% endif %} Don't have an account yet?
          <a href="{% url 'main:register' %}">Register Now</a>
        </div>
        
        {% endblock content %}
    ```

- Lakukan import pada file urls.py yang ada pada subdirektori main
    ```
   from main.views import login_user
    ```
   Tambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi:
      ```
    urlpatterns = [
     path('login/', login_user, name='login'),
 ]
      ```
  
**3. Membuat Fungsi Logout**
- Lakukan import pada views.py
- Tambahkan fungsi di bawah ini ke dalam fungsi views.py
    ```
  def logout_user(request):
    logout(request)
    return redirect('main:login')
    ```
- Tambahkan kode pada berkas main.html
    ```
  <a href="{% url 'main:logout' %}">
    <button>Logout</button>
  </a>
    ```
- Pada urls.py tambahkan kode:
  ```
  from main.views import logout_user
  ```
  dan
    ```
  urlpatterns = [
   path('logout/', logout_user, name='logout'),
  ]
    ```
    
**4. Merestriksi Akses Halaman Main**
- Lakukan import pada views.py
- Tambahkan potongan kode 
  ```
  @login_required(login_url='/login') di atas fungsi show_main
  ```
- Jalankan proyek Django-mu dengan perintah python manage.py runserver dan bukalah http://localhost:8000/

**5. Menggunakan Data Dari Cookies**
- Buka kembali views.py yang ada pada subdirektori main. Tambahkan import HttpResponseRedirect, reverse, dan datetime pada bagian paling atas.
- Pada fungsi login_user tambahkan cookie yang bernama last_login untuk melihat kapan terakhir kali pengguna melakukan login.
  Ganti kode yang ada pada blok if form.is_valid() menjadi potongan kode berikut:
    ```
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
    ```
- Pada fungsi show_main, tambahkan potongan kode
  ```
  'last_login': request.COOKIES['last_login']
  ```
- Ubah fungsi logout_user mennjadi :
  ```
  def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
  ```
- Tambahkan kode berikut pada main.html
   ```
    <h5>Sesi terakhir login: {{ last_login }}</h5>
   ```
- Silakan refresh halaman login (atau jalankan proyek Django-mu dengan perintah python manage.py runserver 

**6. Menghubungkan product dengan user**
- Tambahkan import baru pada models.py
    ```
    from django.contrib.auth.models import User
    ```
- Untuk menghubungkan model dengan user kita harus menambahkan model baru bernama user menggunakan foreign key
    ```
   user = models.ForeignKey(User, on_delete=models.CASCADE)
    ```
- Ubah potongan kode pada fungsi create_page dalam subdirektori views.py
    ```
  def create_page(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        page = form.save(commit=False)
        page.user = request.user
        form.save()
        # page.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_page.html", context)
    ```
- Ubah value pada fungsi show_main
    ```
  def show_main(request):
    products =  Product.objects.filter(user=request.user)
    ```
- Simpan semua perubahan, dan lakukan migrasi model dengan python manage.py makemigrations
- Lakukan python manage.py migrate
- tambahkan sebuah import baru pada settings.py yang ada pada subdirektori sunrise_mart
  import os
- Kemudian, ganti variabel DEBUG dari berkas settings.py menjadi :
  PRODUCTION = os.getenv("PRODUCTION", False)
  DEBUG = not PRODUCTION
- Jalankan proyek Django-mu dengan perintah python manage.py runserver dan bukalah http://localhost:8000/ 

</details>

<details>
  <summary>TUGAS 5</summary>

  **TUGAS INDIVIDU 5**

  **1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!**

  CSS menentukan prioritas penerapan gaya berdasarkan beberapa faktor. Urutan prioritas pertama adalah aturan dengan !important , 
  yang akan selalu diutamakan jika ada. Setelah itu, gaya inline yang ditulis langsung pada elemen HTML (misalnya, melalui atribut style="... )
  memiliki prioritas tertinggi. Di bawahnya, selektor ID (#id) diambil terlebih dahulu dibandingkan yang lain. Selektor kelas (.class), atribut ([attribute]),
  dan pseudo-class (:hover, :focus, dll.) memiliki prioritas berikutnya. Setelah itu, selektor elemen seperti div, p, atau h1, serta pseudo-elemen (::before, ::after) diprioritaskan. Universal selector (*) memiliki spesifisitas terendah. Jika terdapat dua atau lebih aturan dengan spesifisitas yang sama, aturan yang terakhir dideklarasikan akan diambil.

  **2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!**

  Responsive design menjadi konsep penting dalam pengembangan aplikasi web karena beberapa alasan utama yang berkaitan dengan pengalaman pengguna,
  aksesibilitas, dan SEO. Pertama, responsive design memastikan bahwa konten dapat diakses dengan nyaman di berbagai perangkat, baik itu desktop, 
  tablet, maupun smartphone. Ini mengurangi kebutuhan untuk menggulir atau memperbesar halaman, sehingga pengguna dapat menavigasi situs dengan mudah. 
  Selain itu, desain responsif juga meningkatkan aksesibilitas karena semakin banyak pengguna yang mengakses internet melalui perangkat mobile. Hal ini 
  penting untuk meningkatkan interaksi dan keterlibatan pengguna.
  
Selain itu, Google memberikan peringkat lebih tinggi kepada situs web yang responsif karena mereka menawarkan pengalaman pengguna yang lebih baik. Ini berarti 
bahwa penerapan responsive design dapat membantu meningkatkan visibilitas dan peringkat situs di hasil pencarian. Dengan demikian, situs web yang responsif 
tidak hanya lebih mudah digunakan oleh pengguna, tetapi juga lebih mudah ditemukan oleh mesin pencari.Mengembangkan satu versi situs web yang responsif juga 
lebih efisien dibandingkan dengan membuat versi terpisah untuk desktop dan mobile. Ini mengurangi biaya pemeliharaan dan waktu pengembangan. 

**3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!**

**Margin** adalah ruang yang berada di luar batas (border) elemen. Fungsinya adalah untuk memberikan jarak antara elemen tersebut dengan elemen lain di sekitarnya. 
Margin dapat diatur menggunakan properti seperti `margin-top`, `margin-right`, `margin-bottom`, dan `margin-left`. Untuk menerapkan margin, kita dapat menggunakan 
sintaks berikut:
```css
selector {
    margin: 20px; /* Margin di semua sisi */
    margin-top: 10px; /* Margin hanya di atas */
    margin: 10px 20px; /* Margin atas/bawah 10px, kiri/kanan 20px */
}
```

**Border** adalah garis yang mengelilingi elemen dan terletak di antara padding dan margin. Border dapat disesuaikan dalam hal ketebalan, jenis garis, dan warna. 
Implementasinya dilakukan dengan menggunakan properti seperti `border-width`, `border-style`, dan `border-color`. Contoh penerapan border adalah sebagai berikut:
```css
selector {
    border: 2px solid black; /* Border dengan ketebalan 2px, jenis solid, warna hitam */
}
```

**Padding** adalah ruang yang berada di dalam elemen, antara konten dan batas (border) elemen tersebut. Padding berfungsi untuk memberikan ruang tambahan di sekitar 
konten sehingga tidak menempel langsung pada batas elemen. Padding dapat diatur dengan cara yang mirip dengan margin, menggunakan properti seperti `padding-top`, 
`padding-right`, `padding-bottom`, dan `padding-left`. Berikut adalah contoh penerapan padding:
```css
selector {
    padding: 15px; /* Padding di semua sisi */
    padding-top: 10px; /* Padding hanya di atas */
    padding: 10px 20px; /* Padding atas/bawah 10px, kiri/kanan 20px */
}
```
Secara ringkas, margin mengatur jarak antar elemen, border memberikan batas visual pada elemen, dan padding menciptakan ruang di dalam elemen itu sendiri. Memahami 
perbedaan ini sangat penting untuk menciptakan tata letak yang rapi dan fungsional dalam desain web.

**4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!**

**- Flexbox**

**Konsep**: Flexbox, atau Flexible Box Layout, adalah model tata letak satu dimensi yang memungkinkan elemen dalam sebuah kontainer diatur dalam baris atau kolom.
Dengan menggunakan flexbox, elemen dapat secara otomatis menyesuaikan ukuran mereka untuk mengisi ruang yang tersedia, baik dengan memperluas maupun menyusut.
Ini sangat berguna untuk membuat tata letak responsif yang dapat beradaptasi dengan berbagai ukuran layar.

**Kegunaan**:
- Memudahkan penataan elemen dalam satu baris atau kolom.
- Memungkinkan untuk melakukan penyelarasan vertikal dan horizontal dengan mudah.
- Mengatasi masalah kolom dengan tinggi yang berbeda, sehingga semua kolom dapat memiliki tinggi yang sama.
- Sangat cocok untuk membuat menu navigasi, tombol, dan komponen UI lainnya yang memerlukan penataan sederhana.

**Implementasi**: Untuk menggunakan flexbox, kita perlu menetapkan properti `display` pada elemen kontainer menjadi `flex`. Contoh implementasi:
```css
.container {
    display: flex;
    justify-content: center; /* Menyelaraskan item secara horizontal */
    align-items: center; /* Menyelaraskan item secara vertikal */
}
```

**- Grid Layout**

**Konsep**: CSS Grid Layout adalah model tata letak dua dimensi yang memungkinkan pengaturan elemen dalam baris dan kolom secara bersamaan. Dengan grid, 
kita dapat membuat struktur kompleks dengan lebih mudah dibandingkan dengan teknik lain seperti float atau positioning.

**Kegunaan**:
- Memungkinkan desain tata letak yang lebih kompleks dengan kontrol penuh atas baris dan kolom.
- Sangat berguna untuk membuat layout halaman penuh, seperti grid foto, dashboard, atau layout berbasis kartu.
- Dapat mengatur ruang antar elemen dengan lebih efektif dan fleksibel.

**Implementasi**: Untuk menggunakan grid layout, kita juga perlu menetapkan properti `display` pada elemen kontainer menjadi `grid`. Contoh implementasi:
```css
.grid-container {
    display: grid;
    grid-template-columns: repeat(3, 1fr); /* Membuat 3 kolom dengan lebar yang sama */
    gap: 10px; /* Jarak antar item grid */
}
```
**5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!**


</details>
