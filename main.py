import extract as ex
import validate as val
import transform as trans
import load


def main():
    databases = ex.extract()
    val.validate_schemas(databases)
    trans.transform(databases)


if __name__ == "__main__":
    main()
