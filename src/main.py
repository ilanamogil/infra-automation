from machine import Machine, get_user_input, store_machines_into_config_json


def main():
    machines: list[Machine] = get_user_input()
    store_machines_into_config_json("configs/instances.json", machines)

main()