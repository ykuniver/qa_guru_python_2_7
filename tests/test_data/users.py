from dataclasses import dataclass
from enum import Enum
from typing import Tuple


class Subject(Enum):
    History = 'History'
    Maths = 'Maths'
    Physics = 'Pysics'


class Hobby(Enum):
    Sports = 'Sports'
    Reading = 'Reading'
    Music = 'Music'


class Gender(Enum):
    Male = 'Male'
    Female = 'Female'
    Other = 'Other'


@dataclass
class User:
    gender: Gender
    name: str
    last_name: str = 'YouMeanIt'
    email: str = 'abc@efg.com'
    user_number: str = '0123456789'
    birth_day: str = '21'
    birth_month: str = 'October'
    birth_year: str = '1972'
    subjects: Tuple[Subject] = (Subject.History, Subject.Maths)
    current_address: str = 'The Earth'
    hobbies: Tuple[Hobby] = (Hobby.Sports, Hobby.Reading)
    picture_file: str = 'photo.jpg'
    state: str = 'Haryana'
    city: str = 'Karnal'


student = User(name='yuri', gender=Gender.Male)
