import random
import time

MESSAGES = [
    "System check complete.",
    "No problems detected.",
    "All services operational.",
    "Waiting for input...",
    "Task completed successfully."
]


def show_status():
    print("-" * 32)
    print("       SYSTEM STATUS")
    print("-" * 32)

    for _ in range(3):
        print(random.choice(MESSAGES))
        time.sleep(0.4)

    print("-" * 32)


def generate_id(length=8):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return "".join(random.choice(characters) for _ in range(length))


def main():
    print("Utility Manager v1.4")
    print()
    show_status()

    identifier = generate_id()
    print(f"Session ID: {identifier}")
    print("Session finished.")


if __name__ == "__main__":
    main()
