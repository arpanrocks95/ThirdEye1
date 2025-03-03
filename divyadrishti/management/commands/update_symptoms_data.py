from django.core.management import BaseCommand
import pandas as pd

from django.conf import settings
from divyadrishti.models import Symptoms

listofsymptoms = ['back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine',
                  'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach',
                  'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation',
                  'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
                  'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool',
                  'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs',
                  'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails',
                  'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips',
                  'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints',
                  'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness',
                  'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine',
                  'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)',
                  'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain',
                  'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite',
                  'polyuria', 'family_history', 'mucoid_sputum',
                  'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion',
                  'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen',
                  'history_of_alcohol_consumption', 'fluid_overload', 'blood_in_sputum', 'prominent_veins_on_calf',
                  'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling',
                  'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister',
                  'red_sore_around_nose',
                  'yellow_crust_ooze']
                  
def startup():
    print("---------------------Update Symptoms Command Started----------------------")

    for symptom in listofsymptoms:
        if not Symptoms.objects.filter(symptom_name=symptom
                                       ).count():
            print(f"added : {symptom}")
            Symptoms.objects.create(symptom_name=symptom
                                    )
        else:
            print(f"already present : {symptom}")
    print("---------------------Update Symptoms Command Ended----------------------")


class Command(BaseCommand):
    def handle(self, *args, **options):
        startup()
