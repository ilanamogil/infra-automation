# Infra Automation

## Project Overview

Infra Automation is a Python-based infrastructure provisioning simulator that allows users to define, configure, and manage virtual machines with different operating systems and hardware specifications. The tool provides a centralized way to input machine configurations, store them in JSON format, and execute setup scripts across the provisioned infrastructure.

## Objectives

- **Machine Configuration Management**: Define machines with custom names, operating systems (Ubuntu/CentOS), CPU, and RAM specifications
- **Configuration Persistence**: Store machine configurations in JSON format for reproducibility
- **Script Execution**: Execute bash scripts on configured machines for automated setup and provisioning
- **Logging**: Comprehensive logging to both file and console for tracking provisioning activities
- **Error Handling**: Robust error handling with proper exception reporting

## Setup Instructions

### Prerequisites

- Python 3.8+
- Virtual environment support
- Access to bash shell
- sudo access (for nginx installation scripts)

### Installation

1. **Clone the repository**:
   ```bash
   cd /home/mogilevsky/Src/infra-automation
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Execution

1. **Run the infrastructure simulator**:
   ```bash
   python src/infra_simulator.py
   ```

2. **Follow the interactive prompts**:
   - Enter machine name (or 'done' to finish)
   - Select OS (Ubuntu or CentOS)
   - Specify CPU (e.g., 2vCPU)
   - Specify RAM (e.g., 4GB)

3. **Configurations are saved to** `configs/instances.json`

4. **Logs are written to** `logs/provisioning.log` and displayed in console

## Example Expected Output

### Console Output:
```
Enter machine number 1 name (or 'done' to finish): web-server-1
Enter OS (Ubuntu/CentOS): Ubuntu
Enter CPU (e.g., 2vCPU): 2vCPU
Enter RAM (e.g., 4GB): 4GB

2025-12-08 10:15:23,456 - INFO - Provisioning web-server-1: Ubuntu, 2vCPU, 4GB
2025-12-08 10:15:24,123 - INFO - running script scripts/setup_nginx.sh on web-server-1
2025-12-08 10:15:26,789 - INFO - script scripts/setup_nginx.sh ran successfully on web-server-1

Enter machine number 2 name (or 'done' to finish): done
2025-12-08 10:15:27,901 - INFO - Configuration saved to configs/instances.json
```

### Generated Configuration File (`configs/instances.json`):
```json
[
    {
        "name": "web-server-1",
        "os": "Ubuntu",
        "cpu": "2vCPU",
        "ram": "4GB"
    },
    {
        "name": "db-server-1",
        "os": "CentOS",
        "cpu": "4vCPU",
        "ram": "8GB"
    }
]
```

### Log File (`logs/provisioning.log`):
```
2025-12-08 10:15:23,456 - INFO - Provisioning web-server-1: Ubuntu, 2vCPU, 4GB
2025-12-08 10:15:24,123 - INFO - running script scripts/setup_nginx.sh on web-server-1
2025-12-08 10:15:26,789 - INFO - script scripts/setup_nginx.sh ran successfully on web-server-1
2025-12-08 10:15:27,890 - INFO - Provisioning db-server-1: CentOS, 4vCPU, 8GB
2025-12-08 10:15:29,012 - INFO - Configuration saved to configs/instances.json
```

## Project Structure

```
infra-automation/
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── configs/
│   └── instances.json       # Machine configurations (generated)
├── logs/
│   └── provisioning.log     # Provisioning logs
├── scripts/
│   └── setup_nginx.sh       # Nginx installation script
└── src/
    ├── __init__.py
    ├── infra_simulator.py   # Main entry point
    ├── machine.py           # Machine class and utilities
    └── logger.py            # Logging configuration
```

## Key Features

- **Input Validation**: Machine configurations are validated using Pydantic models
- **Dual Logging**: Logs are written to both file and console simultaneously
- **Bash Script Execution**: Execute setup scripts with proper error handling
- **Interactive CLI**: User-friendly command-line interface for machine configuration

## Troubleshooting

- **Permission Denied**: Ensure you have sudo access for script execution
- **Script Not Found**: Verify script paths are correct relative to project root
- **Log File Issues**: Ensure `logs/` directory exists and has write permissions
- **Import Errors**: Verify all dependencies are installed via `pip install -r requirements.txt`
