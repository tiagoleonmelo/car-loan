from pydantic import BaseModel, ValidationError, root_validator, validator
from typing import Optional, Dict
from typing_extensions import Literal

# constants
VALUE_1 = "1-9"
VALUE_2 = "10-99"
VALUE_3 = "99+"
VALUE_4 = "unknown"
CONST = [VALUE_1, VALUE_2, VALUE_3, VALUE_4]


class Company(BaseModel):
    name: str
    employees: Optional[Literal[VALUE_1, VALUE_2, VALUE_3, VALUE_4]]

    @staticmethod
    def map(v):
        if v in CONST:
            return v
        if int(v) < 1:
            return VALUE_4
        elif int(v) < 10:
            return VALUE_1
        elif int(v) < 100:
            return VALUE_2
        else:
            return VALUE_3

    @validator("employees", pre=True)
    def employees_must_be_literal(cls, values):
        values = cls.map(values)
        if values == VALUE_4:
            raise ValueError("Employee number invalid")
        return values


if __name__ == "__main__":
    data_collection = [
        {"name": "Good Company B.V.", "employees": "1-9"},
        {"name": "Random company A", "employees": "1"},
        {"name": "Random company B", "employees": "67"},
        {"name": "Random company C", "employees": "101"},
        {
            "name": "Random company D",
            "employees": " 878",
        },  # the whitespace in the stringed number is deliberate !
        {"name": "Random company E", "employees": "0"},
        {"name": "Random company F", "employees": 6},
    ]

    for data in data_collection:
        try:
            company = Company(**data)
            print(f"{company.name} has {company.employees} number of employees")
        except ValidationError:
            print(f"Invalid data supplied")
            # raise
