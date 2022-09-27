import os
import sys

from Cyan import __version__
from Cyan.interpreter import run


def shell(debug_mode=False):
    print(
        f"Cyan {__version__} shell on {sys.platform}"
        + (" (with debug mode enabled)" if debug_mode else "")
    )
    while True:
        try:
            text = input(">>> ")

        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit(0)

        if text.strip() == "":
            continue

        result, error = run("<stdin>", text, debug_mode=debug_mode)

        if error:
            print(error)
        else:
            print(result)


def run_file(filename, debug_mode):
    with open(filename) as file:
        text = file.read()

    result, error = run(filename, text, debug_mode=debug_mode)

    if error:
        print(error)


def main():
    """
    -d
    --version
    --help
    file
    """
    debug = False
    argv = sys.argv[1:]
    if "-d" in argv:
        debug = True
        argv.remove("-d")
    if not argv:
        shell(debug_mode=debug)
    if "--version" in argv:
        print(__version__)
        return
    if "--help" in argv:
        print(f"Cyan {__version__}")
        print(f"")
        print(f"    --version    See Cyan version")
        print(f"    --help       See this message")
        print(f"    -d           Enable debug mode")
        return

    for arg in argv:
        if os.path.exists(arg):
            run_file(arg, debug_mode=debug)


if __name__ == "__main__":
    main()
