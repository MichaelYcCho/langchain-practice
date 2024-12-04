from dotenv import load_dotenv
import os



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f"Hi, {name}")  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    load_dotenv()
    print(os.getenv("DB_HOST"))
    print_hi("PyCharm")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
