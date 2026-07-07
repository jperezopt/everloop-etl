import extract as ex


def main():
    databases = ex.extract()
    print(databases["Users"])


if __name__ == "__main__":
    main()
