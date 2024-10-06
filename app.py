from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            user_email = request.form['user_email']
            user_password = request.form['user_password']
            name = request.form['name']
            phone = request.form['phone']
            address = request.form['address']
            linkedin = request.form['linkedin']
            school = request.form['school']
            major = request.form['major']
            start_year = request.form['start_year']
            end_year = request.form['end_year']
            city = request.form['city']
            position = request.form['position']
            responsibilities = request.form['responsibilities']
            achievements = request.form['achievements']
            language = request.form['language']
            language_level = request.form['language_level']
            skills = request.form['skills']
            job_plan = request.form['job_plan']

            # Format email
            subject = "Formulir Pembuatan CV"
            body = f"""
            Nama Lengkap: {name}
            Nomor Handphone: {phone}
            Alamat: {address}
            LinkedIn: {linkedin}
            Pendidikan Terakhir: {school}, {major}, {start_year} - {end_year}, {city}
            Pengalaman Kerja: {position}, {responsibilities}, {achievements}
            Bahasa: {language} ({language_level})
            Keterampilan: {skills}
            Rencana Pekerjaan: {job_plan}
            """
            msg = MIMEText(body)
            msg['Subject'] = subject
            msg['From'] = user_email
            msg['To'] = 'geniusmakerds@gmail.com'

            # Kirim email
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(user_email, user_password)
                server.send_message(msg)
            return "Formulir berhasil dikirim!"
        except Exception as e:
            return f"Gagal mengirim formulir: {e}"

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
