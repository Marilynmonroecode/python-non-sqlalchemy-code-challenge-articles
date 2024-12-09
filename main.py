from lib.classes.db import DatabaseConnection
import sys

def main():
    DatabaseConnection().create_tables()

if __name__ == '__main__':
    sys.exit(main())