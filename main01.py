import speech_recognition as sr
from flask import Flask, render_template, request, flash
from collections import Counter
from flask import jsonify

app = Flask(__name__)
app.secret_key = "project"

def detect_disease(symptoms):
    # Here you would implement the logic to detect diseases based on symptoms
    # For demonstration purposes, let's return a dummy list of diseases
    # This is a simplistic mapping and would typically be more complex in a real-world scenario
    disease_mapping = {
        "cold": ["Common cold", "Flu"],
        "cough": ["Flu", "Bronchitis"],
        "poor appetite": ["Typhoid"],
        "vomiting": ["Typhoid", "Malaria", "Diarrhea"],
        "Generalized aches and pains": ["Typhoid"],
        "Fever as high as 104 degrees": ["Typhoid", "Malaria"],
        "Lethargy": ["Typhoid"],
        "Diarrhea": ["Typhoid", "Malaria", "Diarrhea", "Abortion"],
        "nausea": ["Malaria", "Diarrhea", "Hepatitis C", "Abdominal migraines in children and adults", "Anxiety",
                   "Allergies", "Jaundice"],
        "muscle pain": ["Malaria"],
        "profuse sweating": ["Malaria"],
        "Hungary": ["Diabetes"],
        "Drymouth": ["Diabetes"],
        "Blurred": ["Diabetes"],
        "thirst": ["Diabetes"],
        "Wheezing": ["Asthma"],
        "Shortness Of Breath": ["Asthma"],
        "Cough": ["Asthma", "Allergy", "Sneezing", "Cough", "TB"],
        "Abdominal Cramps": ["Abdominal Pain"],
        "Bloating": ["Abdominal Pain", "Weight Gain"],
        "Stomach Cramps": ["Abdominal Pain"],
        "ankle swelling": ["Ankle Pain"],
        "numbness or tingling": ["Ankle Pain"],
        "instability": ["Ankle Pain"],
        "burning pain": ["Ankle Pain"],
        "inability to bear weight on the affected ankle": ["Ankle Pain"],
        "stiffness": ["Ankle Pain"],
        "Runny Nose": ["Allergy", "Cold", "Watery Eye"],
        "Watery Eye": ["Allergy", "Watery Eye", "Sneezing"],
        "Tunnel Vision": ["Vision Loss"],
        "Double Vision": ["Vision Loss"],
        "Blur Vision": ["Brain Tumor"],
        "Seizures": ["Brain Tumor", "Encephalitis"],
        "dizzyness": ["Brain Tumor"],
        "watery stool": ["Diarrhea"],
        "blood in the stool": ["Diarrhea"],
        "urgency of bowel movements": ["Diarrhea"],
        "belly pain": ["Diarrhea", "Abdominal Pain"],
        "Chills": ["Fever", "Sneezing", "TB"],
        "Weakness": ["Fever", "Weight Loss", "Tremors", "Abdominal Pain"],
        "Drainage Of Pus": ["Fever"],
        "Body Shivring": ["Fever"],
        "Sweating": ["Fever"],
        "loss of appetite": ["Hepatitis C", "Weight Loss", "Jaundice"],
        "Increased Appetite": ["Weight Gain"],
        "Fatigue": ["Weight Gain", "Weight Loss", "Allergies", "Malnutrition", "Jaundice"],
        "Loss Of Appetite": ["Weight Loss"],
        "eye pain": ["Watery Eye"],
        "eye inflammation or eye infection": ["Watery Eye"],
        "vision impairment": ["Watery Eye"],
        "Tremors": ["Tremors"],
        "Seizure": ["Tremors", "Encephalitis"],
        "Muscle Cramps": ["Tremors"],
        "snoring": ["Sleep Apnea"],
        "gasping for breath": ["Sleep Apnea"],
        "restlessness": ["Sleep Apnea"],
        "poor quality sleep": ["Sleep Apnea"],
        "burning itchy or watery eyes": ["Sneezing"],
        "nasal congestion or runny nose": ["Sneezing", "Cold", "Allergy"],
        "sore throat": ["Sneezing", "Cold", "Allergy"],
        "pain": ["Toe Pain", "Joint Pain"],
        "Nervousness and tremor": ["Thyroid"],
        "Mental fogginess and poor concentration": ["Thyroid"],
        "infection": ["Common cold"],
        "most people can feel buldge where an inguinal hernia develops in the groin": ["Abdominal hernia"],
        "pain in the center of abdomen": ["Abdominal migraines in children and adults"],
        "veginal bleeding and pelvic pain.blood clots may also be present in veginal bleeding": ["Abortion"],
        "commonly appears on the face and shoulders": ["Acne"],
        "body itching": ["Allergies"],
        "fear of lossing control": ["Anxiety"],
        "low oxygen level": ["Anemia"],
        "develop palpitations": ["Anemia"],
        "water eyes": ["Common cold", "Watery Eye"],
        "low grade fever": ["Common cold"],
        "headache": ["Common cold", "Brain Tumor", "Typhoid", "TB"],
        "hair loss": ["Anemia"],
        "significant pain": ["Abdominal hernia"],
        "burning chest": ["Abdominal hernia"],
        "sour taste": ["Abdominal hernia"],
        "paleness of skin": ["Abdominal migraines in children and adults"],
        "cramping": ["Abdominal migraines in children and adults"],
        "frequent urination": ["Abdominal pain", "Urinary Tract Infection"],
        "bumps": ["Acne"],
        "whiteheads": ["Acne"],
        "blackheads": ["Acne"],
        "fatigue": ["Allergies", "Anemia", "Weight Loss", "Malnutrition", "Jaundice"],
        "sneezing": ["Allergies", "Cold", "Sneezing"],
        "scatchy throat": ["Allergies"],
        "itching on nose": ["Allergies"],
        "facial swelling": ["Allergies"],
        "tired": ["Anemia"],
        "trembling or shaking": ["Anxiety"],
        "hot blashes": ["Anxiety"],
        "stomach upset": ["Anxiety"],
        "sweating of palms": ["Anxiety"],
        "shortness of breath": ["Anxiety", "Chest Pain"],
        "sleep problem": ["Anxiety"],
        "musle tension": ["Anxiety"],
        "irritability": ["Anxiety"],
        "irritable mood": ["Bipolar disorder"],
        "racing thoughts": ["Bipolar disorder"],
        "pressured speech": ["Bipolar disorder"],
        "decrease need for sleep": ["Bipolar disorder"],
        "throught itching": ["Cough"],
        "chest pain": ["Cough", "TB"],
        "swollen lymph nodes": ["Dengue fever"],
        "swollen joints": ["Toe Pain"],
        "Jaw Pain": ["Toothache"],
        "Bleeding Gums": ["Toothache"],
        "Lump On Gums": ["Toothache"],
        "muscle pain": ["Dengue fever"],
        "Coughing, sometimes with mucus or blood": ["Tuberculosis"],
        "Loss of weight": ["Tuberculosis"],
        "Feeling very tired": ["Hepatitis E"],
        "Losing weight without trying": ["Hepatitis E"],
        "Yellow skin": ["Hepatitis E", "Jaundice"],
        "Feeling weak": ["Hepatitis E"],
        "fatigue": ["Swine Flu", "TB", "Allergies", "Weight Loss", "Malnutrition", "Jaundice"],
        "nasal secretions": ["Swine Flu"],
        "Loss of fat": ["Malnutrition"],
        "Breathing difficulties, a higher risk of respiratory failure": ["Malnutrition"],
        "Depression": ["Malnutrition"],
        "skin sores": ["Leprosy"],
        "lumps": ["Leprosy"],
        "strike the eyes and the thin tissue lining the inside of the nose": ["Leprosy"],
        "Abdominal pain": ["Filariasis", "TB", "Jaundice"],
        "Skin rashes": ["Filariasis"],
        "Arthritis": ["Filariasis"],
        "Hyper or hypo pigmented macules": ["Filariasis"],

        "stiff neck": ["Encephalitis"],
        "redness": ["Joint Pain"],
        "swelling": ["Joint Pain"],
        "tenderness": ["Joint Pain"],
        "warmth": ["Joint Pain"],
        "locking of the joint": ["Joint Pain"],
        "loss of range of motion of the joint": ["Joint Pain"],
        "Pressure, fullness or tightness in your chest": ["Chest Pain"],
        "Cold sweats": ["Chest Pain"],
        "Dizziness or weakness": ["Chest Pain"],
        "A feeling of liquid running down the back of your throat": ["Cough"],
        "Frequent throat clearing and sore throat": ["Cough"],
        "Hoarseness": ["Cough"],
        "Heartburn or a sour taste in your mouth": ["Cough"],
        "Cough(3 weeks lasts)": ["TB"],
        "Coughing up blood or mucus": ["TB"],
        "weight loss": ["TB", "Weight Loss", "Malnutrition"],
        "Chills": ["TB"],
        "Fever": ["TB", "Viral Infection", "Tuberculosis", "Hepatitis E", "Jaundice"],
        "pale stools": ["Jaundice"],
        "dark urine": ["Jaundice"],
        "itchiness": ["Jaundice"],
        "High Fever": ["Viral Infection"],
        "Diarrhea": ["Viral Infection"],
        "Skin rash": ["Viral Infection"],
        "Muscle ache": ["Viral Infection"],
        "Loss of sensation": ["Viral Infection"],
        "scratchy": ["Troat Infection"],
        "burning": ["Troat Infection"],
        "raw": ["Troat Infection"],
        "dry": ["Troat Infection"],
        "irritated": ["Troat Infection"],
    }

    diseases = set()
    for symptom in symptoms:
        if symptom in disease_mapping:
            diseases.update(disease_mapping[symptom])
    return list(diseases)

def get_specialist(disease):
        specialist_mapping = {
            "Common cold": "General Physician",
            "Flu": "General Physician",
            "Bronchitis": "Pulmonologist",
            "Joint Pain": ["Orthopedician", "Rheumatologist"],
            "Chest Pain": ["Pulmonologist", "Cardiologist"],
            "Cough": ["Pulmonologist", "General Physician"],
            "Diabetes": ["Diabetologist", "Endocrinologist"],
            "Asthma": "Pulmonologist",
            "Diarrhea": ["General Physician", "Gastroenterologist"],
            "Hepatitis C": ["Gastroenterologist", "Hepatologist"],
            "Abdominal Pain": "Gastroenterologist",
            "Allergy": ["Otolaryngologist", "Dermatologist"],
            "Tuberculosis": "Pulmonologist",
            "Swine Flu": "General Physician",
            "Typhoid": "General Physician",
            "Encephalitis": "Neurologist",
            "Ankle Pain": "Orthopedician",
            "Brain Tumor": "Neurologist",
            "Fever": "General Physician",
            "Watery Eye": "Ophthalmologist",
            "Vision Loss": "Ophthalmologist",
            "Urinary Tract Infection": "Urologist",
            "Toe Pain": "Orthopedician",
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
        }

        # Check if the disease is in the mapping
        if disease in specialist_mapping:
            # If the specialist is a list, join them into a string
            if isinstance(specialist_mapping[disease], list):
                return ', '.join(specialist_mapping[disease])
            else:
                return specialist_mapping[disease]
        else:
            return "General Physician"  # Default to General Physician if not found


def get_doctors_by_specialist(specialist):
    doctor_details = {
        "General Physician": [
            {
                "name": "Dr. John Smith",
                "address": "123 Main Street, City, Country",
                "contact": "1234567890",
                "type": "Private",
                "specialist": "General Physician"
            },
            {
                "name": "Amit Achliya",
                "address": "1St Floor Faida Building, Amravati 444601, Near Savkar Bhavan Jaystambh squre",
                "contact": "9422265961",
                "type": "Private",
                "specialist": "General Physician"
            },
            # Add more General Physicians if needed
        ],
        # Add other specialist categories here
    }

    # Check if the specialist is in the mapping
    if specialist in doctor_details:
        return doctor_details[specialist]
    else:
        return "Doctor Not Found"

# Example usage:
specialist = "General Physician"
doctors = get_doctors_by_specialist(specialist)
for doctor in doctors:
    print(doctor)


@app.route('/')
def index():
    flash("Welcome to Vatsal's site")
    return render_template('index.html')


@app.route('/audio_to_text/')
def audio_to_text():
    flash("Press Start to start recording audio and press Stop to end recording audio")
    return render_template('audio_to_text.html')




# @app.route('/audio', methods=['POST'])
# def audio():
#     r = sr.Recognizer()
#
#     # Save the audio file
#     with open('upload/audio.wav', 'wb') as f:
#         f.write(request.data)
#
#     # Load the audio file
#     with sr.AudioFile('upload/audio.wav') as source:
#         audio_data = r.record(source)
#
#         try:
#             # Recognize speech
#             symptoms = r.recognize_google(audio_data, language='en-IN').lower().split()
#             flash("Symptoms recognized: " + ', '.join(symptoms))
#
#             # Detect disease based on symptoms
#             diseases = detect_disease(symptoms)
#
#             if diseases:
#                 return_text = "Possible diseases based on the described symptoms:<br>"
#                 for disease in diseases:
#                     specialist = get_specialist(disease)
#                     doctors = get_doctors_by_specialist(specialist)
#                     return_text += f"- {disease}: {specialist}<br>"
#                     if doctors:
#                         return_text += "Possible diseases based on the described symptoms:<br>"
#                         for disease in diseases:
#                             specialist = get_specialist(disease)
#                             return_text += f"- {disease}: {specialist}<br>"
#                             if isinstance(doctors, list):
#                                 return_text += "Recommended doctors:<br>"
#                                 for doctor in doctors:
#                                     if isinstance(doctor, dict):  # Check if the doctor is a dictionary
#                                         return_text += f"Specialist: {specialist}<br>"
#                                         return_text += f"Name: {doctor['name']}<br>"
#                                         return_text += f"Address: {doctor['address']}<br>"
#                                         # Add other attributes as needed
#                                     else:
#                                         return_text += "Invalid doctor details.<br>"
#                             else:
#                                 return_text += "No recommended doctors found for this specialist.<br>"
#                     else:
#                         return_text = "No diseases found for the described symptoms."
#
#
#             else:
#                 return_text = "No diseases found for the described symptoms."
#         except sr.UnknownValueError:
#             return_text = "Sorry! Voice not Detected"
#         except sr.RequestError as e:
#             return_text = f"Sorry! Could not request results from Google Speech Recognition service; {e}"
#
#     return jsonify({'response': return_text})


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
            symptoms = r.recognize_google(audio_data, language='en-IN').lower().split()

            # Detect disease based on symptoms
            diseases = detect_disease(symptoms)

            return_text = ""

            if diseases:
                # Construct list of diseases
                diseases_info = []
                for disease in diseases:
                    specialist = get_specialist(disease)
                    doctors = get_doctors_by_specialist(specialist)
                    doctors_info = []
                    if doctors:
                        for doctor in doctors:
                            if isinstance(doctor, dict):
                                doctors_info.append(f"Name: {doctor['name']}, Specialist: {specialist}, Address: {doctor['address']}, Contact: {doctor['contact']}")
                    diseases_info.append((disease, specialist, doctors_info))

                # Construct return text
                for disease, specialist, doctors_info in diseases_info:
                    return_text += f"Disease: {disease}, Specialist: {specialist}<br>"
                    if doctors_info:
                        return_text += "Recommended doctors:<br>"
                        for info in doctors_info:
                            return_text += f"- {info}<br>"
                    else:
                        return_text += "No recommended doctors found.<br>"
            else:
                return_text = "No diseases found for the described symptoms."

        except sr.UnknownValueError:
            return_text = "Sorry! Voice not Detected"
        except sr.RequestError as e:
            return_text = f"Sorry! Could not request results from Google Speech Recognition service; {e}"

    # return jsonify({'response': return_text})
    return jsonify(return_text)


if __name__ == "__main__":
    app.run(debug=True)