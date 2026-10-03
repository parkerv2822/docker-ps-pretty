"""Docker PS Pretty — Show local docker ps as a compact table of name, image, status, and ports."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='docker_ps_pretty',
        description='Show local docker ps as a compact table of name, image, status, and ports.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Docker PS Pretty')
    print('docker ps you can paste.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
