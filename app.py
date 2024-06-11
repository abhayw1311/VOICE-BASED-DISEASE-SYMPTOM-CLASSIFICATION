import speech_recognition as sr
from collections import Counter
from flask_mysqldb import MySQL
import MySQLdb.cursors
from flask import Flask, render_template,request,session,url_for,redirect,flash, send_file
from nltk.corpus import stopwords
import nltk
import pickle
nltk.download('stopwords')

app = Flask(__name__)
app.secret_key = "project"



app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='diseases_db'

mysql = MySQL(app)

#List of the symptoms is listed here in list l1.

l1=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
    'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
    'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
    'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
    'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
    'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
    'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
    'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
    'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
    'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
    'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
    'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
    'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
    'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
    'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
    'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
    'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
    'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
    'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
    'yellow_crust_ooze']

#List of Diseases is listed in list disease.

disease=['Fungal infection', 'Allergy', 'GERD', 'Chronic cholestasis',
       'Drug Reaction', 'Peptic ulcer diseae', 'AIDS', 'Diabetes ',
       'Gastroenteritis', 'Bronchial Asthma', 'Hypertension ', 'Migraine',
       'Cervical spondylosis', 'Paralysis (brain hemorrhage)', 'Jaundice',
       'Malaria', 'Chicken pox', 'Dengue', 'Typhoid', 'hepatitis A',
       'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E',
       'Alcoholic hepatitis', 'Tuberculosis', 'Common Cold', 'Pneumonia',
       'Dimorphic hemmorhoids(piles)', 'Heart attack', 'Varicose veins',
       'Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia',
       'Osteoarthristis', 'Arthritis',
       '(vertigo) Paroymsal  Positional Vertigo', 'Acne',
       'Urinary tract infection', 'Psoriasis', 'Impetigo']

#disease = [df['prognosis'].unique()]
#print(disease)

with open('models/decision_tree.pkl','rb') as f:
    decision_tree=pickle.load(f)


def detect_disease(symptoms):
    # Here you would implement the logic to detect diseases based on symptoms
    # For demonstration purposes, let's return a dummy list of diseases
    # This is a simplistic mapping and would typically be more complex in a real-world scenario
     #sample array of symptoms, take this as a input from the user but ensure that symptoms is present in the given dataset
    print([decision_tree.predict(symptoms)[0]])
    return [decision_tree.predict(symptoms)[0]]
    disease_mapping = {
        "cold": ["Flu"],
        "cough": ["Flu"],
        "vomiting": ["Typhoid"],

        "high": ["Typhoid", "Malaria"],
        "fever": ["Flu"],

        "Lethargy": ["Typhoid"],
        "Diarrhea": ["Typhoid", "Diarrhea"],
        "nausea": ["Malaria", "Diarrhea", "Jaundice"],
        "Hungry": ["Diabetes"],
        "drymouth": ["Diabetes"],
        "Blurred": ["Diabetes"],
        "thirst": ["Diabetes"],
        "Wheezing": ["Asthma"],
        "Shortness": ["Asthma"],
        "Cough": ["Asthma", "Allergy","Cold", "TB"],
        #"Abdominal": ["Abdominal Pain"],
        "Bloating": ["Abdominal Pain", "Weight Gain"],
        "Stomach": ["Abdominal Pain"],
        "ankle": ["Ankle Pain"],
        "tingling": ["Ankle Pain"],
        "instability": ["Ankle Pain"],
        "stiffness": ["Ankle Pain"],
        "Runny": ["Allergy", "Cold", "Watery Eye"],
        "Watery Eye": ["Allergy", "Watery Eye", "Sneezing"],
        "Eye": ["Allergy", "Watery Eye", "Sneezing"],
        "Tunnel": ["Vision Loss"],
        "Double": ["Vision Loss"],
        "blur": ["Vision Loss"],
        "seizures": ["Brain Tumor", "Encephalitis"],
        "dizziness": ["Low Blood Pressure"],
        "stool": ["Diarrhea"],
        "belly": ["Diarrhea", "Abdominal Pain"],
        "chills": ["Fever"],
        "weakness": ["Fever"],
        "shivring": ["Fever"],
        "sweating": ["Fever"],
        "appetite": ["Hepatitis C", "Weight Loss", "Jaundice"],
        "eye": ["Watery Eye"],
        "vision": ["Watery Eye"],
        "Tremors": ["Tremors"],
        "Seizure": ["Tremors", "Encephalitis"],
        "snoring": ["Sleep Apnea"],
        "gasping for breath": ["Sleep Apnea"],
        "restlessness": ["Sleep Apnea"],
        "burning itchy or watery eyes": ["Sneezing"],

        "runny": ["Sneezing", "Cold", "Allergy"],
        "nose": ["Sneezing", "Cold", "Allergy"],

        "sore": ["Cold", "Allergy"],
        "throat": ["Cold", "Allergy"],

        "joint": ["Toe Pain", "Joint Pain"],
        "infection": ["Common cold"],
        "itching": ["Allergies"],
        "fear": ["Anxity"],
        "water eyes": ["Watery Eyes"],
        "headache": ["Common cold", "Migrane", "Typhoid", "TB"],


        "burning": ["Abdominal hernia"],
        "chest": ["Abdominal hernia"],

        "frequent": ["Abdominal pain", "Urinary Tract Infection"],
        "urination": ["Abdominal pain", "Urinary Tract Infection"],

        "bumps": ["Acne"],
        "whiteheads": ["Acne"],
        "blackheads": ["Acne"],
        "fatigue": ["Allergies", "Anemia", "Weight Loss", "Malnutrition", "Jaundice"],
        "sneezing": ["Allergies", "Cold", "Sneezing"],

        "scatchy": ["Allergies"],
        "throat": ["Allergies"],

        "itchy": ["Allergies"],
        "nose": ["Allergies"],

        "facial": ["Allergies"],
        "swelling": ["Allergies"],

        "tired": ["Anemia"],

        "trembling": ["Anxiety"],
        "shaking": ["Anxiety"],

        "sweating": ["Anxiety"],
        "palms": ["Anxiety"],

        "shortness": ["Anxiety", "Chest Pain"],
        "breath": ["Anxiety", "Chest Pain"],

        "sleep": ["Anxiety"],

        "irritability": ["Anxiety"],
        "irritable mood": ["Bipolar disorder"],
        "racing thoughts": ["Bipolar disorder"],
        "pressured speech": ["Bipolar disorder"],
        #"decrease need for sleep": ["Bipolar disorder"],

        "chest": ["Cough", "TB"],

        "swollen lymph nodes": ["Dengue fever"],
        #"swollen joints": ["Toe Pain"],
        "teeth": ["Toothache"],
        "bleeding gums": ["Toothache"],

        "yellow": ["Hepatitis E", "Jaundice"],
        "skin": ["Hepatitis E", "Jaundice"],

        "weakness": ["Viral Infection"],

        "fatigue": ["Swine Flu", "TB", "Allergies", "Weight Loss", "Malnutrition", "Jaundice"],

        "nasal": ["Swine Flu"],
        "secretions": ["Swine Flu"],

        "loss ": ["Malnutrition"],
        " fat": ["Malnutrition"],

        "depression": ["Malnutrition"],
        "skin sores": ["Leprosy"],
        "lumps": ["Leprosy"],
        #"strike the eyes and the thin tissue lining the inside of the nose": ["Leprosy"],
        "Abdominal pain": ["Filariasis", "TB", "Jaundice"],
        #"pain": ["Filariasis", "TB", "Jaundice"],
        
        "rashes": ["Allergies"],
        
        "arthritis": ["Filariasis"],
        #"Hyper or hypo pigmented macules": ["Filariasis"],
        "stiff neck": ["Encephalitis"],
        "neck": ["Encephalitis"],
        "redness": ["Allergies"],
        "swelling": ["Joint Pain","Hair Fracture"],
        "swollen": ["Joint Pain","Hair Fracture"],
        "tenderness": ["Joint Pain"],
        "warmth": ["Joint Pain"],
        "locking of the joint": ["Joint Pain"],
        "loss of range of motion of the joint": ["Joint Pain"],
        "pressure, fullness or tightness in your chest": ["Chest Pain"],
        "cold sweats": ["Anxiety"],

        #"dizziness": ["Chest Pain"],

        "hoarseness": ["Cough"],
        "heartburn": ["Acidity"],
        "coughing up blood or mucus": ["TB"],
        "weight loss": ["TB", "Weight Loss", "Malnutrition"],
        "chills": ["TB"],
        "pale stools": ["Jaundice"],

        "dark": ["Jaundice"],
        "urine": ["Jaundice"],

        "back":["Muscle Sprain"],
        
        "itchiness": ["Jaundice"],
        "Fever": ["Viral Infection"],
        "Diarrhea": ["Viral Infection"],
        "Muscle ache": ["Viral Infection"],
        "ache": ["Viral Infection"],
        "Loss of sensation": ["Viral Infection"],
        "scratchy": ["Throat Infection"],
        "burning": ["Throat Infection"],
        "raw": ["Throat Infection"],
        "dry": ["Throat Infection"],
        "irritated": ["Throat Infection"],
    }

    diseases = set()
    for symptom in symptoms:
        if symptom in disease_mapping:
            diseases.update(disease_mapping[symptom])
    return list(diseases)

def get_specialist(disease):

        specialist_mapping = {
            "Low Blood Pressure": "Cardiologist",
            "Migrane": "Neurologist",
            "Hair Fracture" : "Orthopedic",
            "Common cold": "General Physician",
            "Flu": "General Physician",
            "Bronchitis": "Pulmonologist",
            "Joint Pain": ["Orthopedic", "Rheumatologist"],
            "Chest Pain": ["Pulmonologist", "Cardiologist"],
            "Cough": ["Pulmonologist", "General Physician"],
            "Diabetes": ["Diabetologist", "Endocrinologist"],
            "Asthma": "Pulmonologist",
            "Diarrhea": ["General Physician", "Gastroenterologist"],
            "Hepatitis C": ["Gastroenterologist", "Hepatologist"],
            "Abdominal Pain": "Gastroenterologist",
            "Allergy": ["Otolaryngologist", "Dermatologist"],
            "Tb": "Pulmonologist",
            "Swine Flu": "General Physician",
            "Typhoid": "General Physician",
            "Encephalitis": "Neurologist",
            "Ankle Pain": "Orthopedic",
            "Brain Tumor": "Neurologist",
            "Fever": "General Physician",
            "Watery Eye": "Ophthalmologist",
            "Vision Loss": "Ophthalmologist",
            "Urinary Tract Infection": "Urologist",
            "Toe Pain": "Orthopedic",
            "Toothache": "Dentist",
            "Tremors": "Neurologist",
            "Sleep Apnea": "Neurologist",
            "Sneezing": "General Physician",
            "Abdominal hernia": "Gastroenterologist",
            "Acne": "Dermatologist",
            "Anxiety": "Neurologist",
            "Bipolar disorder": "Psychiatrist",
            "Hepatitis E": "General Physician",
            "Dengue fever": "General Physician",
            "Malnutrition": "General Physician",
            "Leprosy": "Dermatologist",
            "Filariasis": "General Physician",
            "Muscle Pain": "Chiropractor",
        }

        # Check if the disease is in the mapping
        if disease in specialist_mapping:
            # If the specialist is a list, join them into a string
            return specialist_mapping[disease]
        else:
            return "General Physician"  # Default to General Physician if not found


@app.route('/')
def index():
    # flash("Welcome to web application")
    l2=[]
    for i in range(0,len(l1)):
        l2.append(0)
    psymptoms = ['obesity', 'swollen_legs','malaise',]
    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    #disease prediction
    inputtest = [l2]
    print(detect_disease(inputtest))
    return render_template('index.html')


@app.route('/audio_to_text/')
def audio_to_text():
    if 'username' not in session:
        return redirect(url_for('user_login'))  # Assuming you have a login route
    username = session['username']

    flash("Press Start to start recording audio and press Stop to end recording audio")
    return render_template('audio_to_text.html')


@app.route('/audio', methods=['POST'])
def audio():
    r = sr.Recognizer()

    # Save the audio file
    with open('upload/audio.wav', 'wb') as f:
        f.write(request.data)

    # Load the audio file
    with sr.AudioFile('upload/audio.wav') as source:
        audio_data = r.record(source)

        try:
            # Recognize speech
            tokenizedWords = r.recognize_google(audio_data, language='en-IN').lower().split()
            symptoms=[]
            for word in tokenizedWords:
                if word  not in stopwords.words('english'):
                    symptoms.append(word)
            flash("Symptoms recognized: " + ', '.join(symptoms))


            # Detect disease based on symptoms
            CD = detect_disease(symptoms)
            diseases = list(set(CD))
            unique_specialists = set() 
            if diseases:
                session['diseases'] = diseases
                return_text = "Possible diseases based on the described symptoms:<br>"
                for disease in diseases:
                    return_text+=f"{disease},"
                    specialist = get_specialist(disease)
                    if isinstance(specialist, list):
                        unique_specialists.update(specialist)
                    else:
                        unique_specialists.add(specialist)
                return_text += f"<br><br> Please Visit to Doctors :<br>"
                for specialist in unique_specialists:
                    session['specialist'] = specialist
                    return_text += f"{specialist} <br>"
            else:
                return_text = "No diseases found for the described symptoms."

        except sr.UnknownValueError:
            return_text = "Sorry! Voice not Detected"
        except sr.RequestError as e:
            return_text = f"Sorry! Could not request results from Google Speech Recognition service; {e}"

        # Insert user's fry into the database
        if request.method == 'POST':
            user_id = session.get('userid')
            diseases = session.get('diseases')

            if not user_id or not diseases:
                flash("User not logged in or no symptoms detected")
            else:
                try:
                    # Convert the list of symptoms into a comma-separated string
                    symptoms_str = ', '.join(diseases)

                    cur = mysql.connection.cursor()
                    # Execute the SQL query to insert data into the history table
                    cur.execute("INSERT INTO history (user_id, sym) VALUES (%s, %s)", (user_id, symptoms_str,))
                    mysql.connection.commit()
                    cur.close()
                    #flash("User's history saved successfully")
                except Exception as e:
                    flash(f"Error occurred while saving user's history: {str(e)}")
    return return_text


@app.route('/user-login', methods=['GET', 'POST'])
def user_login():
    error = None

    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        # Retrieve user information from the database
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM registration WHERE username = %s AND password = %s", (username, password))
        user = cur.fetchone()  # Fetch the first row
        cur.close()

        if user:
            session['username'] = username
            session['userid'] = user[0]


            user_dict = {'id':user[0],'username': user[0], 'photo': user[1]}

            cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("SELECT username, photo FROM registration WHERE username=%s", (username,))
            ulist = cur.fetchall()
            cur.close()

            return redirect(url_for('user_dashboard', username=username))

        else:
            flash("Invalid username or password")

    return render_template('user_login.html', error=error)


@app.route('/user-signup', methods=['GET', 'POST'])
def usersignup():
    error = None

    if request.method == "POST":
        fullname = request.form['fullname']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        file = request.files['file']
        mobile = request.form['mobile']

        if not username or not email or not password or not mobile or not file:
            flash("Please fill in all required fields.")
        else:

            # Check if the username is already taken
            cur = mysql.connection.cursor()
            cur.execute("SELECT COUNT(*) FROM registration WHERE username = %s", (username,))
            count = cur.fetchone()[0]
            cur.close()

            if count > 0:
                flash("Username is already taken. Please choose a different one.")
            else:
                cur = mysql.connection.cursor()
                cur.execute(
                    "INSERT INTO registration (name, username, email, password, photo, mobile) VALUES (%s,%s, %s, %s, %s, %s)",
                    (fullname, username, email, password, file.filename, mobile))
                mysql.connection.commit()
                cur.close()

                file.save('static/upload_img/' + file.filename)

                flash("Signup successful!!")  # You can redirect to another page or show a success message.

    return render_template('user_signup.html')


@app.route('/user_dashboard')
def user_dashboard():
    if 'username' not in session:
        return redirect(url_for('user_login'))  # Assuming you have a login route

    username = session['username']
    return render_template('user_start.html', username=username)

@app.route('/history_list')
def history_list():

    username = session['username']
    user_id = session.get('userid')

    # Retrieve list of history records
    cur = mysql.connection.cursor()
    query = "SELECT * FROM history WHERE user_id ="+str(user_id)
    print(query)
    cur.execute(query)
    history_records = cur.fetchall()
    print(history_records)
    cur.close()

    return render_template('user_history.html', history_records=history_records, username=username)

@app.route('/user_delete_his/<int:id>', methods=['GET', 'POST'])
def user_delete_his(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM history WHERE id = %s", (id,))
        mysql.connection.commit()
        cur.close()
        flash("User Diseases History deleted successfully")
        return redirect("/history_list")
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/doctor_list')
def doctor_list():
    if 'username' not in session:
        return redirect(url_for('user_login'))  # Assuming you have a login route

    username = session['username']

    diseases = session.get('diseases')
    specialist_name = session.get('specialist')
    # specialist_name = "General Physician"
    print("01010101")
    print(diseases)

    if specialist_name:
        # Retrieve list of doctors based on specialist
        cur = mysql.connection.cursor()
        # cur.execute("SELECT * FROM doctor WHERE specialist = %s", (specialist_name,))
        cur.execute("SELECT * FROM doctor")
        doc_list = cur.fetchall()
        cur.close()

        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT * FROM doctor WHERE specialist = %s", (specialist_name,))
        profilelist = cur.fetchall()
        cur.close()

        print(doc_list)
        return render_template('doctor_list.html', specialist_name=specialist_name, doc_list=doc_list,profilelist=profilelist)
    else:
        return "No diseases or specialist found in session."

@app.route('/slider/')
def slider():
    return render_template('demo1.html')


#-----------------------------------------------------------------


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    error = None

    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']


        if username=="admin" and password=="admin":
            flash("Admin are logged in successfully!")

            return redirect(url_for('admin_dashboard'))

        else:
            flash("Invalid username or password")

    return render_template('admin_login.html', error=error)


@app.route('/admin_dashboard')
def admin_dashboard():
    # Retrieve road requests with user IDs
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM doctor")
    profilelist = cur.fetchall()
    total_student = len(profilelist)
    cur.close()

    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM registration")
    h = cur.fetchall()
    total_his = len(h)
    cur.close()

    return render_template('admin_dashboard.html', total_student=total_student, total_his=total_his)


@app.route('/admin-view-user')
def adminviewemp():
    try:
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT * FROM registration")
        profilelist = cur.fetchall()
        cur.close()

        return render_template('admin_userlist.html', profilelist=profilelist, )
    except Exception as e:
        return f"Error: {str(e)}"


@app.route('/admin-view-history')
def adminviewhis():
    try:
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT * FROM doctor")
        profilelist = cur.fetchall()
        cur.close()

        return render_template('admin_history.html', profilelist=profilelist, )
    except Exception as e:
        return f"Error: {str(e)}"


import os
import uuid
from werkzeug.utils import secure_filename

@app.route('/user-update-profile', methods=['GET', 'POST'])
def user_update_profile():
    user_id = request.args.get('id')

    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM registration WHERE id = %s", (user_id,))
    user_data = cur.fetchone()
    cur.close()
    print(user_data)

    if request.method == 'POST':
        name = request.form['fullname']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        mobile = request.form['mobile']
        file = request.files['file']

        try:
            cur = mysql.connection.cursor()

            if file:
                # Generate a unique filename to prevent overwriting
                cur.execute(
                    "UPDATE registration SET name=%s, email=%s, mobile=%s, photo=%s, username=%s, password=%s WHERE id=%s",
                    (name, email, mobile, file.filename, username, password, user_id))
                file.save('static/upload_img/' + file.filename)
            else:
                cur.execute(
                    "UPDATE registration SET name=%s, email=%s, mobile=%s, username=%s, password=%s WHERE id=%s",
                    (name, email, mobile, username, password, user_id))

            mysql.connection.commit()
            flash("Profile Update successfully")
            cur.close()

            return redirect("/admin-view-user")
        except Exception as e:
            flash(f"Error: {str(e)}")

    return render_template('admin_update_user.html', user_data=user_data)

@app.route('/user-delete-profile/<int:id>', methods=['GET', 'POST'])
def user_delete_profile(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM registration WHERE id = %s", (id,))
        mysql.connection.commit()
        cur.close()
        flash("User deleted successfully")
        return redirect("/admin-view-user")
    except Exception as e:
        return f"Error: {str(e)}"


@app.route('/user_update', methods=['GET', 'POST'])
def user_update():
    if 'username' not in session:
        return redirect(url_for('user_login'))  # Assuming you have a login route

    username = session['username']

    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM registration WHERE username = %s", (username,))
    user_data = cur.fetchone()
    cur.close()

    if request.method == 'POST':
        name = request.form['fullname']
        email = request.form['email']
        new_username = request.form['username']
        password = request.form['password']
        mobile = request.form['mobile']
        # imgpro = request.files['file']

        try:

            cur = mysql.connection.cursor()
            cur.execute(
                "UPDATE registration SET name=%s, email=%s, mobile=%s, username=%s, password=%s WHERE username=%s",
                (name, email, mobile, new_username, password, username))
            mysql.connection.commit()
            cur.close()

            flash("Profile updated successfully")
            return redirect(url_for('user_update'))  # Redirect to the same page after update
        except Exception as e:
            flash(f"Error: {str(e)}")


    return render_template('user_update.html', user_data=user_data)

@app.route('/diseases_list')
def diseases_list():
    try:
        # Retrieve list of doctors
        cur = mysql.connection.cursor()
        # cur.execute("SELECT * FROM history")
        cur.execute("Select sym, date, username FROM history INNER JOIN registration ON history.user_id = registration.id;")
        doc_list = cur.fetchall()
        cur.close()

        return render_template('admin_dise_history.html', doc_list=doc_list)
    except Exception as e:
        # Handle any exceptions that might occur during database access
        flash(f"Error occurred while fetching doctor list: {str(e)}")
        return render_template('error.html', error_message=str(e))






if __name__ == "__main__":
    app.run(debug=True)