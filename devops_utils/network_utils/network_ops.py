print(f"Importing {__name__} module...\n")

import sys
import subprocess

from ..file_utils import parse_yaml_or_json_file # Relative import
# from devops_utils.file_utils.file_ops import parse_yaml_or_json_file # Absolute import

def is_host_up(hostname: str) -> bool:
    """Pings a host to check if it's reachable"""
    print(f"\t- {__name__}.{sys._getframe().f_code.co_name} called for {hostname} by {__name__}.{sys._getframe(1).f_code.co_name}\n")

    try:
        result: subprocess.CompletedProcess = subprocess.run([
                "ping",
                "-n", # -c in Linux / MacOS
                "1",
                hostname
            ],
            timeout = 3,
            check = True,
            capture_output = True,
            text = True
        )

        return result.returncode == 0
    
    except (
        subprocess.CalledProcessError,
        subprocess.TimeoutExpired
    ):
        return False

def check_hosts_from_config_file(config_file_path: str) -> bool:
    """Cheks if all hosts in config file are reachable"""
    print(f"\t- {__name__}.{sys._getframe().f_code.co_name} called for {config_file_path}\n")

    config_data: dict[str, list[str]] = parse_yaml_or_json_file(config_file_path)
    
    hosts: list[str] = config_data.get("hosts", [])

    if not hosts:
        print(f"There are no host configured in config file\n")
        return False

    return all(is_host_up(host) for host in hosts)
