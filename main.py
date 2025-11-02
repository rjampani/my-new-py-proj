from api_client import get


def main():
    print("Hello from my-new-py-proj!")
    response = get("https://www.github.com")
    print(response.status_code)


if __name__ == "__main__":
    main()
