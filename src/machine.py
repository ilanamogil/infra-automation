from enum import StrEnum
from pydantic import BaseModel, Field

class OS(StrEnum):
    UBUNTU = "Ubuntu"
    CENTOS = "CentOS"

class Machine(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    os: OS
    cpu: str = Field(..., min_length=1, max_length=20)
    ram: str = Field(..., min_length=1, max_length=20)


def get_user_input():
    machines = []
    while True:
        name = input("Enter machine name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        os = input("Enter OS (Ubuntu/CentOS): ")
        cpu = input("Enter CPU (e.g., 2vCPU): ")
        ram = input("Enter RAM (e.g., 4GB): ")
        machine = Machine(name=name,os=os,cpu=cpu,ram=ram)
        # Validate input (to be implemented by the student)
        # Example: validate_instance_input(instance_data)

        machines.append(machine)
    return machines
    


get_user_input()
