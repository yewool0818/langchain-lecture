import csv
import json

def csv_to_jsonl(csv_file_path, jsonl_file_path):
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        with open(jsonl_file_path, mode='w', encoding='utf-8') as jsonl_file:
            for row in csv_reader:
                jsonl_file.write(json.dumps(row) + '\n')

# 사용 예시
csv_file_path = './data/reviews.csv'  # 변환할 CSV 파일 경로
jsonl_file_path = 'reviews.jsonl'  # 생성할 JSONL 파일 경로
csv_to_jsonl(csv_file_path, jsonl_file_path)
