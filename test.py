import os

def get_path():
    print("This is a test function.")

    var = "PATH"
    a = os.environ.get(var, "default_value")
    print(f"Environment variable {var}: {a}")

if __name__ == "__main__":
    get_path()
