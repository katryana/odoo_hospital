{
    'name' : 'Hospital',
    'depends' : [
        'base'
    ],
    'data': [
        'security/ir.model.access.csv',

        'views/hr_hospital_patient_views.xml',
        'views/hr_hospital_doctor_views.xml',
        'views/hr_hospital_doctor_schedule_views.xml',
        'views/hr_hospital_disease_views.xml',
        'views/hr_hospital_diagnosis_views.xml',
        'views/hr_hospital_disease_type_views.xml',
        'views/hr_hospital_appointment_views.xml',
        'views/hr_hospital_personal_doctor_history_views.xml',
        'views/hr_hospital_research_views.xml',
        'views/hr_hospital_sample_views.xml',
        'views/hr_hospital_research_type_views.xml',
        'views/hr_hospital_menus.xml',
    ],
    'application': True,
}
