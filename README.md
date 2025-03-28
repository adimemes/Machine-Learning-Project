# Laporan Proyek Machine Learning - I Kadek Adi Memes Subagia

## Domain Proyek
 <h1>Analisa Pergerakan Harga Bitcoin</h1>

 <p>Bitcoin atau yang biasa kita kenal dengan BTC adalah salah satu mata uang digital atau yang kita kenal dengan cryptocurrency, hal ini menjadi sangat tren dan banyak sekali orang -orang yang mulai menaruh sebagian penghasilannya kedalam cryptocurrency. terutama pada Bitcoin ini karena Bitcoin menduduki Top 1 cryptocurrency dengan harga market tertinggi. bisa dilihat pada website <a href ="https://coinmarketcap.com/id/">Coinmarketcap</a></p> <br>
 Kenapa saya mengambil permasalahan ini adalah karena ini sedang panas - panasnya di indonesia, dimana banyak konten kreator yang sudah mengedukasi kita untuk mulai investasi pada coin inii, tapii kita sebagai individu tidak boleh asal percaya dengan ajakan konten kreator yang mengajak menaruh uang kita pada Bitcoin sebelum kita tahu apa itu Bitcoin?? dan apa aja sihh yang mempengaruhi Bitcoin itu bisa naik atau turun. <br>

 Nahhh karena ini adalah uang digital yang harganya tidak bisa di prediksi dengan hanya insting kita hehehehe, kita perlu adanya pemahaman mengenai cryptocurrency dan pada kesempatan ini saya mencoba mengambil contoh di Bitcoin.

## Business Understanding

Dari Latar belakang di atas mengenai kenapa saya mengambil contoh ini pada proyek saya, saya mendapati dua problem yaitu:

### Problem
*   Apa Saja Faktor yang mempengaruhi Kenaikan dan penurunan Harga Bitcoin ?
*   Apakah Bitcoin Layak di Investasikan Jangka Panjang ?

### Goals

*   Memeriksa faktor yang memiliki Hubungan erat dengan Harga Bitcoin
*   Membuat sebuah Model yang bisa memberikan prediksi harga Bitcoin satu tahun kedepan, dengan data yang ada.

### Solution statements

*   Untuk Permasalahan pertama saya akan membuat sebuah visualisasi data berupa heatmap yang menunjukan korelasi antar setiap fitur dari Bitcoin untuk melihat fitur apa saja yang memiliki korelasi dari harga bitcoin
*   Permasalahan kedua saya akan membuat sebuah model prediksi menggunakan algoritma Random Forest untuk memprediksi harga dengan menggunakan data yang saya miliki.

## Data Understanding

Untuk menyelesaikan masalah yang sudah saya sampaikan di atas, disini saya akan menggunakan dataset yang disediakan secara grartis pada Kaggle <br>
[Dataset](https://www.kaggle.com/datasets/sudalairajkumar/cryptocurrencypricehistory/data) <br>
data yang saya ambil adalah data historical dari Cryptocurrency dalam dataset ini terdapat 23 historical dari Cryptocurrency yang ada, namun karena latar belakang ini mengenai Bitcoin jadi saya hanya mengambil data untuk coin BTC saja.

Dataset Memiliki beberapa Variabel Colom yaitu: 

*   SNo : yang menunjukan nomor dari data
*   Name : adalah menunjukan nama coin dari Cryptocurrency yaitu Bitcoin
*   Symbol : yaitu symbol dari nama Bitcoin yaitu BTC
*   Date : menunjukan tanggal data yang diambil yaitu mulai dari 2013 - 2021
*   High : kolom ini menunjukan harga tertinggi yang dicapai oleh Bitcoin berdasarkan tanggalnya
*   Low : ini adalah kebalikan dari Kolom HIgh, pada kolom ini menunjukan harga terendah dari Bitcoin pada Tanggal tersebut
*   Open : kolom ini merupakan harga pembuka dari koin Bitcoin
*   CLose : yang merupakan harga penutup dari Bitcoin di tanggal tersebut
*   Marketcap : kolom ini menunjukan berapa total aset Bitcoin yang berada dalam pasar Crypto

Dan pada Notebook saya juga melakukan beberapa visualisasi data yaitu melihat nilai dari Bitcoin pertahunnya membandingkan beberapa Colom dan menunjukan kenaikan pada data tahun,bulan dan minggu.

## Data Preparation
### Feature Engginering
Pada tahap ini, dilakukan pemilihan fitur yang akan digunakan dalam model dengan menyaring kolom-kolom yang relevan dari dataset Bitcoin, yaitu:
**feature**: Kolom-kolom yang memiliki korelasi dengan harga Bitcoin.
 <br>
**Target** : Kolom harga penutupan Bitcoin yang dijadikan acuan dalam prediksi.

### Split Dataset
Pada tahap ini, dilakukan pembagian data menjadi dua bagian yaitu pagian train data dan test data, split data ini dilakukan dengan data pada feature engginering di atas yaitu **feature** dan **target**, <br>
pada tahap ini data dibagi menjadi 80% data train dan 20% data test dengan kode test_size = 0.2 yang mengartikan data test mengambil 20% saja.

## Modeling
menggunakan Random Forest karena menurut saya algoritma ini cocok untuk menangani data yang lumayan kompleks, walaupun pada permaslahaan ini memiliki kekurangan juga yaitu kurang akurat untuk memprediksi jangka panjang dan ada alternatifnya yaitu menggunakan LSTM (Long Short-Term Memory) <br> namun karen saya belum mengetahui mengenai LSTM (Long Short-Term Memory) saya akan menggunakan Random Forest Untuk kasus ini.
<br> 
dan pada proses modeling adalah fase yang berulang bagi saya karena saya ada merubah beberapa parameter untuk mendapatkan hasil yang baik secara manual terus menerus atau menggunakan teknik Optimasi Hyperparameter manual

## Evaluation
pada Tahap ini saya menggunakan 4 metrik regresi yaitu:
* Mean Absolute Error (MAE): MAE adalah rata-rata dari selisih absolut antara nilai aktual dan nilai prediksi dengan Rumus. <br>
![image](https://github.com/user-attachments/assets/d522d2ab-d206-4e19-a4f6-319a58c1c111)
* Mean Squared Error (MSE): MSE adalah rata-rata dari kuadrat selisih antara nilai aktual dan prediksi sangat sensitif pada outlier jadi nilainya besar dan di kuadratkan <br>
![image](https://github.com/user-attachments/assets/fc210183-d9b3-4004-856f-e1aa1d45636c)
* Root Mean Squared Error (RMSE): adalah nilai akar dari MSE guna Mengembalikan kesalahan dalam satuan yang sama dengan data asli <br>
![image](https://github.com/user-attachments/assets/d80d0e25-494f-495c-b009-fa0285567d2c)
* R-squared (R²) Score: R² mengukur seberapa baik model regresi menjelaskan variabilitas data <br>
![image](https://github.com/user-attachments/assets/6aaae5d7-9089-4561-86d8-50cc41fb6058)
<br>
dimana jika nilai R² mendekati nilai 1 itu artinya model berjalan dengan baik.

