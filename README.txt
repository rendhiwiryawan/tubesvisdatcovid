VISUALISASI DATA DENGAN BOKEH

Anggota Kelompok :
- Fakhrana Kurnia (1301174344)
- Ghina Dwi Salsabila (1301174074)
- Jovita Nurvania (1301174215)
---------------------------------------------------------------------------------------------------------------------------
Deskripsi :
Bokeh adalah library yang ada di bahasa pemrograman python untuk memvisualisasikan sederetan data dengan plotting grafik 2D
yang memiliki environment yang menarik.
Visualisasi data dengan bokeh mempermudah masyarakat untuk melihat data yang memiliki banyak record. Data yang dimaksud salah
satunya adalah data jumlah kasus (yang terkonfirmasi), kasus kematian dan kasus yang sembuh pada penyakit yang disebabkan
oleh virus corona (covid-19) yang sedang terjadi di masa sekarang ini.
---------------------------------------------------------------------------------------------------------------------------
Kelebihan :
- Mudah digunakan
- Mudah dipahami
- Lebih enak dilihat
---------------------------------------------------------------------------------------------------------------------------
Fitur/widgets :
- Radiobutton
- Slider
- Select
- Button
- Tooltips
---------------------------------------------------------------------------------------------------------------------------
Data :
- Pada visualisasi data ini, digunakan 3 data global yaitu data jumlah penduduk yang positif terpapar virus (data 1), data
jumlah penduduk yang meninggal karena virus (data 2) dan data jumlah penduduk yang sembuh dari virus (data 3).
- Data yang digunakan merupakan data global yaitu data yang bersumber dari seluruh dunia dimana pada data terdapat keterangan
negara dan provinsinya masing-masing.
---------------------------------------------------------------------------------------------------------------------------
Cara penggunaan :
1. Install bokeh dengan menggunakan pip install bokeh
2. Unduh dataset yang akan digunakan (deaths, confirmed, recovered), pastikan file dataset (.csv) berada dalam direktori yang
   sama dengan file python (.py).
3. Running program python tersebut pada cmd menggunakan command line ‘bokeh serve --show (namafile).py’, lalu akan diarahkan ke
   localhost.
4. Lalu akan terlihat peta persebaran yang diperoleh berdasarkan titik koordinat yang ada pada dataset (longitude dan latitude).
   Untuk melihat persebaran data penduduk yang positif terkena virus dapat di klik radio button di pojok kiri atas dengan label
   ‘Data 1’ maka akan terlihat persebarannya dengan titik berwarna merah, sedangkan jika ingin melihat persebaran penduduk yang
   meninggal karena virus dapat di klik radio button dengan label ‘Data 2’ maka akan terlihat persebarannya dengan titik berwarna
   biru dan jika ingin melihat persebaran penduduk yang telah sembuh dari virus dapat di klik radio button dengan label ‘Data 3’
   maka akan terlihat persebarannya dengan titik berwarna hijau.
5. Untuk lebih spesifiknya, dapat dilihat sesuai dengan negara yang diinginkan dengan memilih menu dropdown/select di bagian atas
   dengan judul ‘Region’. Peta akan berubah sesuai region yang dipilih.
6. Karena jumlah data yang sangat banyak, pengguna diberi kemudahan untuk memilih akan melihat persebaran data dengan jumlah data
   minimalnya sesuai keinginan pengguna. Jika pengguna ingin melihat data dengan jumlah tertentu, pengguna dapat menggeser slider
   yang ada di bawah region ke kanan untuk angka lebih besar dan ke kiri untuk angka yang lebih kecil. Jika slider digeser persebaran
   data akan berubah sesuai dengan jumlahnya.
7. Jumlah kasus dari setiap daerah dapat dilihat dengan mengarahkan kursor pada sebuah titik tertentu. Akan muncul nama negara dan
   jumlah kasus pada negara tersebut.
--------------------------------------------------------------------------------
Link video youtube : https://youtu.be/Q6Zj1yUSVNI
