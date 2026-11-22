"""Print basic local system details."""

import os
import platform


def main():
    print("System:", platform.system())
    print("CPU cores:", os.cpu_count())


if __name__ == "__main__":
    main()
