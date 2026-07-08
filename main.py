import extract as ex
import validate as val


def main():
    databases = ex.extract()
    val.validate_schemas(databases)
    print(databases.keys())


if __name__ == "__main__":
    main()
