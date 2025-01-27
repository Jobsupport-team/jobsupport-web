< !DOCTYPE
html >
< html
lang = "id" >
< head >
< meta
charset = "UTF-8" >
< meta
name = "viewport"
content = "width=device-width, initial-scale=1.0" >
< title > Formulir
Pembuatan
CV < / title >
< style >
body
{
    font - family: Arial, sans - serif;
background - color:  # f4f4f4;
margin: 0;
padding: 20
px;
}
h1
{
    text - align: center;
font - weight: bold;
color:  # 333;
}
p
{
    text - align: left;
font - size: small;
color:  # 555;
}
form
{
    background - color:  # fff;
        padding: 20
px;
border - radius: 5
px;
box - shadow: 0
0
10
px
rgba(0, 0, 0, 0.1);
max - width: 600
px;
margin: auto;
}
label
{
    font - weight: bold;
display: block;
margin - top: 15
px;
}
input[type = "text"],
input[type = "email"],
input[type = "url"],
input[type = "number"],
textarea,
select,
input[type = "password"] {
    width: 100 %;
padding: 10
px;
margin: 5
px
0
20
px;
border: 1
px
solid  # ccc;
border - radius: 4
px;
}
input[type = "submit"] {
    background - color:  # 28a745;
        color: white;
border: none;
padding: 10
px;
border - radius: 5
px;
cursor: pointer;
font - weight: bold;
}
input[type = "submit"]:hover
{
    background - color:  # 218838;
}
< / style >
< / head >
< body >
< h1 > Formulir
Pembuatan
CV < / h1 >
< p > Isi
sesuai
data
diri
kamu
ya. < / p >

< form
method = "POST" >
< label
for ="user_email" > Email Pengirim:< / label >
< input
type = "email"
id = "user_email"
name = "user_email"
required >

< label
for ="user_password" > Password Pengirim:< / label >
< input
type = "password"
id = "user_password"
name = "user_password"
required >

< label
for ="name" > Nama Lengkap:< / label >
< input
type = "text"
id = "name"
name = "name"
required >

< label
for ="phone" > Nomor Handphone:< / label >
< input
type = "text"
id = "phone"
name = "phone"
required >

< label
for ="address" > Alamat:< / label >
< textarea
id = "address"
name = "address"
required > < / textarea >

< label
for ="linkedin" > Media Sosial (LinkedIn):< / label >
< input
type = "url"
id = "linkedin"
name = "linkedin"
required >

< h3 > Pendidikan
Terakhir < / h3 >
< label
for ="school" > Nama Sekolah / Universitas:< / label >
< input
type = "text"
id = "school"
name = "school"
required >

< label
for ="major" > Jurusan:< / label >
< input
type = "text"
id = "major"
name = "major"
required >

< label
for ="start_year" > Tahun Masuk:< / label >
< input
type = "number"
id = "start_year"
name = "start_year"
required >

< label
for ="end_year" > Tahun Lulus:< / label >
< input
type = "number"
id = "end_year"
name = "end_year"
required >

< label
for ="city" > Kota:< / label >
< input
type = "text"
id = "city"
name = "city"
required >

< h3 > Pengalaman
Kerja < / h3 >
< label
for ="position" > Posisi:< / label >
< input
type = "text"
id = "position"
name = "position"
required >

< label
for ="responsibilities" > Tanggung Jawab:< / label >
< textarea
id = "responsibilities"
name = "responsibilities"
required > < / textarea >

< label
for ="achievements" > Prestasi atau Pencapaian (jika ada):< / label >
< textarea
id = "achievements"
name = "achievements" > < / textarea >

< h3 > Bahasa
Asing
yang
Dikuasai < / h3 >
< label
for ="language" > Bahasa:< / label >
< input
type = "text"
id = "language"
name = "language"
required >

< label
for ="language_level" > Tingkat Pemahaman:< / label >
< select
id = "language_level"
name = "language_level"
required >
< option
value = "pemula" > Pemula < / option >
< option
value = "menengah" > Menengah < / option >
< option
value = "mahir" > Mahir < / option >
< / select >

< label
for ="skills" > Keterampilan Lain yang Dikuasai:< / label >
< textarea
id = "skills"
name = "skills"
required > < / textarea >

< label
for ="job_plan" > Rencana Pekerjaan yang Diinginkan:< / label >
< textarea
id = "job_plan"
name = "job_plan"
required > < / textarea >

< input
type = "submit"
value = "Kirim" >
< / form >
< / body >
< / html >
