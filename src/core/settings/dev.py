import os

CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'redis://localhost:6379/1')
CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND', 'redis://localhost:6379/1')
DATABASE_URI = os.getenv('DATABASE_URI', 'postgresql://db:db@localhost/db')
DEBUG = True
DATASET_ENDPOINT = 'https://data.cityofnewyork.us/api/views/7yc5-fec2/rows.json?accessType=DOWNLOAD'
DATASET_FIELDS = [
    'dbn', 'school_name', 'category', 'year', 'total_enrollment', 'grade_k', 'grade_1', 'grade_2', 'grade_3',
    'grade_4', 'grade_5', 'grade_6', 'grade_7', 'grade_8', 'female_1', 'female_2', 'male_1', 'male_2', 'asian_1',
    'asian_2', 'black_1', 'black_2', 'hispanic_1', 'hispanic_2', 'other_1', 'other_2', 'white_1', 'white_2',
    'ell_spanish_1', 'ell_spanish_2', 'ell_chinese_1', 'ell_chinese_2', 'ell_bengali_1', 'ell_bengali_2',
    'ell_arabic_1', 'ell_arabic_2', 'ell_haitian_creole_1', 'ell_haitian_creole_2', 'ell_french_1',
    'ell_french_2', 'ell_russian_1', 'ell_russian_2', 'ell_korean_1', 'ell_korean_2', 'ell_urdu_1', 'ell_urdu_2',
    'ell_other_1', 'ell_other_2', 'ela_test_takers', 'ela_level_1_1', 'ela_level_1_2', 'ela_level_2_1',
    'ela_level_2_2', 'ela_level_3_1', 'ela_level_3_2', 'ela_level_4_1', 'ela_level_4_2', 'ela_l3_l4_1',
    'ela_l3_l4_2', 'math_test_takers', 'math_level_1_1', 'math_level_1_2', 'math_level_2_1', 'math_level_2_2',
    'math_level_3_1', 'math_level_3_2', 'math_level_4_1', 'math_level_4_2', 'math_l3_l4_1', 'math_l3_l4_2'
]

try:
    from .local import *
except ImportError:
    pass
