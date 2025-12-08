from enum import StrEnum
import json
from pydantic import BaseModel, Field
import logging

logging.basicConfig(level=logging.INFO)


class OS(StrEnum):
    UBUNTU = "Ubuntu"
    CENTOS = "CentOS"

class Machine(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    os: OS
    cpu: str = Field(..., min_length=1, max_length=20)
    ram: str = Field(..., min_length=1, max_length=20)


def get_user_input() -> list[Machine]:
    machines:list[Machine] = []
    while True:
        name = input(f"Enter machine number {len(machines) + 1} name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        os = input("Enter OS (Ubuntu/CentOS): ")
        cpu = input("Enter CPU (e.g., 2vCPU): ")
        ram = input("Enter RAM (e.g., 4GB): ")
        try:
            machine = Machine(name=name,os=os,cpu=cpu,ram=ram)
            machines.append(machine)
            logging.info(f"{machine} created successfully")
        except ValueError as e:
            logging.error(f"Error: {e}.\nBad input, Rejected")
    return machines

def store_machines_into_config_json(file_path: str, machines: list[Machine]):
    machines_data = [machine.model_dump() for machine in machines]
    with open(file_path, "w") as f:
        json.dump(machines_data, f, indent=4)
