from logger import setup_logging
from machine import Machine, get_user_input, store_machines_into_config_json

logger = setup_logging()

def main():
    machines: list[Machine] = get_user_input()
    store_machines_into_config_json("configs/instances.json", machines)

    for machine in machines:
        machine.run_bash_script()

    logger.info("Provision finnished successfully")


main()