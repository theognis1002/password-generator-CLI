import argparse
import random
import string
from typing import List

from colorama import Fore

CHAR_MAPPINGS = {
    "digits": string.digits,
    "upper": string.ascii_uppercase,
    "lower": string.ascii_lowercase,
    "symbol": string.punctuation,
}


def generate_password(length: int, exclude: List[str] = []) -> str:
    chars = "".join([v for k, v in CHAR_MAPPINGS.items() if k not in exclude])
    return "".join(random.choice(chars) for _ in range(length))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="password generator")
    parser.add_argument(
        "-l",
        "--length",
        type=int,
        default=24,
        help="Length of password",
    )
    parser.add_argument(
        "-x",
        "--exclude",
        nargs="*",
        default=[],
        choices=CHAR_MAPPINGS.keys(),
        help="Exclude symbol characters",
    )

    args = parser.parse_args()
    new_password = generate_password(args.length, args.exclude)
    print(Fore.GREEN + f"Newly generated password: {Fore.RESET}{new_password}")
