{
    'name' : 'Hospital',
    'depends' : [
        'base'
    ],
    'data': [
        'security/ir.model.access.csv',

        'views/hr_hospital_patient_views.xml',
        'views/hr_hospital_menus.xml',
    ],
    'application': True,
}
