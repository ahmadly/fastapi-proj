import uuid

from pydantic import BaseModel


class Item(BaseModel):
    id: int | None
    dbn: str | None
    school_name: str | None
    category: str | None
    year: str | None
    total_enrollment: int | None
    grade_k: int | None
    grade_1: int | None
    grade_2: int | None
    grade_3: int | None
    grade_4: int | None
    grade_5: int | None
    grade_6: int | None
    grade_7: int | None
    grade_8: int | None
    female_1: int | None
    female_2: float | None
    male_1: int | None
    male_2: float | None
    asian_1: int | None
    asian_2: float | None
    black_1: int | None
    black_2: float | None
    hispanic_1: int | None
    hispanic_2: float | None
    other_1: int | None
    other_2: float | None
    white_1: int | None
    white_2: float | None
    ell_spanish_1: int | None
    ell_spanish_2: float | None
    ell_chinese_1: int | None
    ell_chinese_2: float | None
    ell_bengali_1: int | None
    ell_bengali_2: float | None
    ell_arabic_1: int | None
    ell_arabic_2: float | None
    ell_haitian_creole_1: int | None
    ell_haitian_creole_2: float | None
    ell_french_1: int | None
    ell_french_2: float | None
    ell_russian_1: int | None
    ell_russian_2: float | None
    ell_korean_1: int | None
    ell_korean_2: float | None
    ell_urdu_1: int | None
    ell_urdu_2: float | None
    ell_other_1: int | None
    ell_other_2: float | None
    ela_test_takers: int | None
    ela_level_1_1: int | None
    ela_level_1_2: float | None
    ela_level_2_1: int | None
    ela_level_2_2: float | None
    ela_level_3_1: int | None
    ela_level_3_2: float | None
    ela_level_4_1: int | None
    ela_level_4_2: float | None
    ela_l3_l4_1: int | None
    ela_l3_l4_2: float | None
    math_test_takers: int | None
    math_level_1_1: int | None
    math_level_1_2: float | None
    math_level_2_1: int | None
    math_level_2_2: float | None
    math_level_3_1: int | None
    math_level_3_2: float | None
    math_level_4_1: int | None
    math_level_4_2: float | None
    math_l3_l4_1: int | None
    math_l3_l4_2: float | None
    chart_id: str | None

    class Config:
        orm_mode = True


class Chart(BaseModel):
    id: uuid.UUID | None
    file: str | None
