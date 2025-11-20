import argparse
import sys
from pathlib import Path

def file_exists_or_exit(filepath):
    path = Path(filepath)
    if not path.exists():
        print(f"File not found: {filepath}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных: JSON, CSV, XLSX")
    subparsers = parser.add_subparsers(dest='cmd', required=True)

    p1 = subparsers.add_parser('json2csv', help='Конвертация JSON в CSV')
    p1.add_argument('--in', dest='input', required=True, help='Входной JSON файл')
    p1.add_argument('--out', dest='output', required=True, help='Выходной CSV файл')

    p2 = subparsers.add_parser('csv2json', help='Конвертация CSV в JSON')
    p2.add_argument('--in', dest='input', required=True, help='Входной CSV файл')
    p2.add_argument('--out', dest='output', required=True, help='Выходной JSON файл')

    p3 = subparsers.add_parser('csv2xlsx', help='Конвертация CSV в XLSX')
    p3.add_argument('--in', dest='input', required=True, help='Входной CSV файл')
    p3.add_argument('--out', dest='output', required=True, help='Выходной XLSX файл')

    args = parser.parse_args()

    try:
        # Проверяем существование входного файла
        file_exists_or_exit(args.input)
        
        # Создаем директорию для выходного файла если нужно
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        if args.cmd == 'json2csv':
            from src.lab05.json_csv import json_to_csv
            json_to_csv(args.input, args.output)
            print(f"Successfully converted JSON to CSV: {args.output}")
        elif args.cmd == 'csv2json':
            from src.lab05.json_csv import csv_to_json
            csv_to_json(args.input, args.output)
            print(f"Successfully converted CSV to JSON: {args.output}")
        elif args.cmd == 'csv2xlsx':
            from src.lab05.csv_xlsx import csv_to_xlsx
            csv_to_xlsx(args.input, args.output)
            print(f"Successfully converted CSV to XLSX: {args.output}")
    except Exception as e:
        print(f"Error during conversion: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()