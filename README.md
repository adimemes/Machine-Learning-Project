# Laporan Proyek Machine Learning - I Kadek Adi Memes Subagia

# Domain Proyek
 <h1>Analisa Pergerakan Harga Bitcoin</h1>

 <p>Bitcoin atau yang biasa kita kenal dengan BTC adalah salah satu mata uang digital atau yang kita kenal dengan cryptocurrency, hal ini menjadi sangat trend dan banyak sekali orang -orang yang mulai menaruh sebagian penghasilannya kedalam cryptocurrency. terutama pada Bitcoin ini karena Bitcoin menduduki Top 1 cryptocurrency dengan harga market tertinggi. bisa dilihat pada website <a href ="https://coinmarketcap.com/id/">Coinmarketcap</a></p> <br>
 Permasalahan ini menjadi topik yang sedang hangat diperbincangkan di Indonesia. Banyak konten kreator yang mengedukasi masyarakat mengenai investasi dalam mata uang kripto, khususnya Bitcoin. Namun, penting untuk tidak langsung mengikuti ajakan investasi tanpa memahami terlebih dahulu apa itu Bitcoin serta faktor-faktor yang mempengaruhi fluktuasi nilainya. 
 <br> <br>
Karena Bitcoin merupakan mata uang digital dengan harga yang tidak dapat diprediksi hanya berdasarkan insting, pemahaman yang mendalam mengenai cryptocurrency menjadi hal yang penting. Dalam hal ini, Bitcoin dipilih sebagai contoh untuk dianalisis lebih lanjut.



 Nahhh karena ini adalah uang digital yang harganya tidak bisa di prediksi dengan hanya insting kita hehehehe, kita perlu adanya pemahaman mengenai cryptocurrency dan pada kesempatan ini saya mencoba mengambil contoh di Bitcoin.

## Business Understanding

Dari Latar belakang di atas dapat diambil dua problem yaitu:

### Problem
* Apa Saja Faktor yang mempengaruhi Kenaikan dan penurunan Harga Bitcoin ?
* Bagaimana model machine learning dapat digunakan untuk memprediksi harga Bitcoin dalam periode tertentu ( harian, mingguan, atau bulanan) dengan tingkat akurasi yang optimal?

### Goals
* Menganalisis faktor-faktor yang memiliki korelasi erat dengan harga Bitcoin.
* Membangun model prediksi harga Bitcoin berdasarkan data historis dengan mempertimbangkan faktor-faktor utama yang mempengaruhi harga serta mengevaluasi kinerjanya menggunakan metrik tertentu

### Solution statements

*   Untuk Permasalahan pertama, akan menggunakan visualisasi data berupa heatmap yang menunjukan korelasi antar fitur bitcoin, sehingga dapat didentifikasi faktor - faktor yang mempengaruhi kenaikan dan penurunan harga bitcoin.
*   Permasalahan kedua, akan dikembangkan menggunakan model prediksi menggunakan algoritma random forest dan dievaluasi dengan Mean Absolute Error (MEA), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), dan R-squared (R²)

# Data Understanding

Untuk menyelesaikan permasalahan yang telah disampaikan sebelumnya, dataset yang digunakan diperoleh secara gratis dari Kaggle. Dataset dapat diakses melalui tautan berikut:<br>
[Dataset](https://www.kaggle.com/datasets/sudalairajkumar/cryptocurrencypricehistory/data) <br>
Dataset ini berisi data historis dari 23 jenis cryptocurrency. Namun, karena fokus proyek ini adalah Bitcoin (BTC), hanya data terkait BTC yang digunakan untuk analisis.

### Jumlah Data
Dataset ini terdiri dari 2.991 baris dan 10 kolom, dengan rincian sebagai berikut:

* SNo: Nomor urut data.
* Name: Nama cryptocurrency, dalam hal ini Bitcoin.
* Symbol: Simbol mata uang Bitcoin, yaitu BTC.
* Date: Tanggal pengambilan data, mencakup rentang waktu dari 2013 hingga 2021.
* High: Harga tertinggi Bitcoin pada tanggal tertentu.
* Low: Harga terendah Bitcoin pada tanggal tertentu.
* Open: Harga pembukaan Bitcoin pada tanggal tersebut.
* Close: Harga penutupan Bitcoin pada tanggal tersebut.
* Volume : Jumlah total Bitcoin yang diperdagangkan dalam satu hari
* Marketcap: Total nilai pasar Bitcoin dalam ekosistem cryptocurrency.

### Kondisi Data
Pada Pemeriksaan Dataset tidak terdapat dataset yang mengalami missing Value. <br>
![image](https://github.com/user-attachments/assets/16958b1a-da09-415c-9a81-04ed23c6fd7f)
<br>
Namun Pada Dataset terdapat salah satu column yang memiliki keliruan type data <br>
![image](https://github.com/user-attachments/assets/07ce7161-5d39-44ad-8772-8ec2f09778a7)



# Data Preparation
Dalam Data Preparation dilakukan beberapa tahapan seperti Feature Engginering dan Split Data, Namun sesuai dengan Kondisi data di atas, sebelum kita melakukan feature engginering dan split data kita melakukan perbaikan type data pada column Date. <br>
![image](https://github.com/user-attachments/assets/3b2b22f2-9576-45b8-96ba-80c4ff203d43)

### Feature Engginering
Pada tahap ini, dilakukan pemilihan fitur yang akan digunakan dalam model dengan menyaring kolom-kolom yang relevan dari dataset Bitcoin, yaitu:
**feature**: Kolom-kolom yang memiliki korelasi dengan harga Bitcoin.
 <br>
**Target** : Kolom harga penutupan Bitcoin yang dijadikan acuan dalam prediksi.

### Split Dataset
Pada tahap ini, dilakukan pembagian data menjadi dua bagian yaitu pagian train data dan test data, split data ini dilakukan dengan data pada feature engginering di atas yaitu **feature** dan **target**, <br>
pada tahap ini data dibagi menjadi 80% data train dan 20% data test dengan kode test_size = 0.2 yang mengartikan data test mengambil 20% saja.

# Modeling dan Evaluasi
Untuk menjawab pertanyaan nomor dua, saya menggunakan **algoritma Random Forest.**
## Random Forest
Random Forest dipilih karena algoritma ini cocok untuk menangani data yang cukup kompleks.
### Cara Kerja Random Forest
Algoritma ini adalah algoritma ensemble learning berbasis decision tree,  Algoritma ini bekerja dengan cara membangun banyak pohon keputusan (decision trees) dan menggabungkan hasilnya untuk meningkatkan akurasi serta mengurangi risiko overfitting.<br>
karena Random Forest menerapkan metode bagging (agregasi bootstrap) untuk menghasilkan prediksi yang akurat dan stabil. yang dimana dalam algoritma ini mengambil sampel acak dari dataset maka dari itu disebut dengan Random Forest.
### Kelebihan 
Kelebihan Dari Algoritma ini adalah cocok untuk dataset yang cukup kompleks karena mampu mengurangi overfiting dengan mengatur Hyperparameter yang ada dalam algoritma ini.
### Kekurangan 
Kekurangan Dari Algoritma ini adalah kurang akurat untuk memprediksi jangka panjang dan ada alternatifnya yaitu menggunakan LSTM (Long Short-Term Memory)
<br> 
### Parameter
Pada File Notebook parameter yang digunakan pada algoritma Random Forest yaitu :
*   n_estimators dengan value default yaitu 100<br>
parameter ini merupakan berapa banyak pohon yang akan digunakan, semakin banyak pohon semakin meningkatkan akurasi namun lama saat eksekusi
*   random_state dengan value none yaitu value bisa diisi berapa saja <br>
untuk mengatur Memilih subset fitur acak di setiap percabangan pohon agar hasil konsisten


## Evaluation
Pada Proyek ini menggunakan empat Metrik evaluasi yaitu:
* Mean Absolute Error (MAE): MAE adalah rata-rata dari selisih absolut antara nilai aktual dan nilai prediksi dengan Rumus. <br>
![image](https://github.com/user-attachments/assets/d522d2ab-d206-4e19-a4f6-319a58c1c111)
* Mean Squared Error (MSE): MSE adalah rata-rata dari kuadrat selisih antara nilai aktual dan prediksi sangat sensitif pada outlier jadi nilainya besar dan di kuadratkan <br>
![image](https://github.com/user-attachments/assets/fc210183-d9b3-4004-856f-e1aa1d45636c)
* Root Mean Squared Error (RMSE): adalah nilai akar dari MSE guna Mengembalikan kesalahan dalam satuan yang sama dengan data asli <br>
![image](https://github.com/user-attachments/assets/d80d0e25-494f-495c-b009-fa0285567d2c)
* R-squared (R²) Score: R² mengukur seberapa baik model regresi menjelaskan variabilitas data <br>
![image](https://github.com/user-attachments/assets/6aaae5d7-9089-4561-86d8-50cc41fb6058)
<br>

Metrik ini digunakan karena metrik ini cocok untuk menjadi evaluasi dalam proyek regresion.
Dalam pelatihan model, didapatkan hasil seperti dibawah ini: 
<br>
* Mean Absolute Error (MAE): 53.16653051038279
* Mean Squared Error (MSE): 14860.572896414964
* Root Mean Squared Error (RMSE): 121.90394947012571
* R-squared (R²) Score: 0.9998845303025761 <br>

Untuk metrik
* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)

jika nilai mendekati Nol berarti hasil dari model baik. <br>
sedangkan untuk nilai R-squared (R²) jika nilai mendekati satu berarti model berjalan dengan baik
