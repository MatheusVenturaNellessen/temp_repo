print(f"{__name__} started\n")

from dotenv import load_dotenv
import os

from devops_utils import check_hosts

load_dotenv()

CONFIG_FILE_PATH: str = os.environ["CONFIG_FILE_PATH"]

def main() -> None:
    print(f"All hosts in config file are available? {check_hosts(CONFIG_FILE_PATH)}\n")

if __name__ == "__main__":
    main()
