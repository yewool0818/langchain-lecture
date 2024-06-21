import json

dataset = {
    "train": [
        {
            "prompt": "방콕의 현재 기온은 어떻게 되나요?",
            "completion": "방콕의 현재 기온은 약 28°C입니다."
        },
        {
            "prompt": "부에노스아이레스의 현재 기온은 어떻게 되나요?",
            "completion": "부에노스아이레스의 현재 기온은 약 28°C입니다."
        },
        {
            "prompt": "델리의 현재 기온은 어떻게 되나요?",
            "completion": "델리의 현재 기온은 약 10°C입니다."
        },
        {
            "prompt": "이스탄불의 현재 기온은 어떻게 되나요?",
            "completion": "이스탄불의 현재 기온은 약 13°C입니다."
        },
        {
            "prompt": "자카르타의 현재 기온은 어떻게 되나요?",
            "completion": "자카르타의 현재 기온은 약 30°C입니다."
        },
        {
            "prompt": "멕시코시티의 현재 기온은 어떻게 되나요?",
            "completion": "멕시코시티의 현재 기온은 약 15°C입니다."
        },
        {
            "prompt": "모스크바의 현재 기온은 어떻게 되나요?",
            "completion": "모스크바의 현재 기온은 약 -12°C입니다."
        },
        {
            "prompt": "상파울루의 현재 기온은 어떻게 되나요?",
            "completion": "상파울루의 현재 기온은 약 27°C입니다."
        },
        {
            "prompt": "상하이의 현재 기온은 어떻게 되나요?",
            "completion": "상하이의 현재 기온은 약 14°C입니다."
        },
        {
            "prompt": "토론토의 현재 기온은 어떻게 되나요?",
            "completion": "토론토의 현재 기온은 약 2°C입니다."
        },
        {
            "prompt": "방콕의 현재 기온은 어떻게 되나요?",
            "completion": "방콕의 현재 기온은 82°F입니다."
        },
        {
            "prompt": "부에노스아이레스의 현재 기온은 어떻게 되나요?",
            "completion": "부에노스아이레스의 현재 기온은 82°F입니다."
        },
        {
            "prompt": "델리의 현재 기온은 어떻게 되나요?",
            "completion": "델리의 현재 기온은 50°F입니다."
        },
        {
            "prompt": "이스탄불의 현재 기온은 어떻게 되나요?",
            "completion": "이스탄불의 현재 기온은 55°F입니다."
        },
        {
            "prompt": "자카르타의 현재 기온은 어떻게 되나요?",
            "completion": "자카르타의 현재 기온은 86°F입니다."
        },
        {
            "prompt": "멕시코시티의 현재 기온은 어떻게 되나요?",
            "completion": "멕시코시티의 현재 기온은 59°F입니다."
        },
        {
            "prompt": "모스크바의 현재 기온은 어떻게 되나요?",
            "completion": "모스크바의 현재 기온은 11°F입니다."
        },
        {
            "prompt": "상파울루의 현재 기온은 어떻게 되나요?",
            "completion": "상파울루의 현재 기온은 81°F입니다."
        },
        {
            "prompt": "상하이의 현재 기온은 어떻게 되나요?",
            "completion": "상하이의 현재 기온은 57°F입니다."
        },
        {
            "prompt": "토론토의 현재 기온은 어떻게 되나요?",
            "completion": "토론토의 현재 기온은 36°F입니다."
        },
        {
            "prompt": "시드니의 현재 기온은 어떻게 되나요?",
            "completion": "시드니의 현재 기온은 약 13°C입니다."
        },
        {
            "prompt": "카이로의 현재 기온은 어떻게 되나요?",
            "completion": "카이로의 현재 기온은 약 28°C입니다."
        },
        {
            "prompt": "케이프타운의 현재 기온은 어떻게 되나요?",
            "completion": "케이프타운의 현재 기온은 약 16°C입니다."
        },
        {
            "prompt": "마드리드의 현재 기온은 어떻게 되나요?",
            "completion": "마드리드의 현재 기온은 약 27°C입니다."
        },
        {
            "prompt": "로마의 현재 기온은 어떻게 되나요?",
            "completion": "로마의 현재 기온은 약 28°C입니다."
        },
        {
            "prompt": "베를린의 현재 기온은 어떻게 되나요?",
            "completion": "베를린의 현재 기온은 약 22°C입니다."
        },
        {
            "prompt": "도쿄의 현재 기온은 어떻게 되나요?",
            "completion": "도쿄의 현재 기온은 약 22°C입니다."
        },
        {
            "prompt": "서울의 현재 기온은 어떻게 되나요?",
            "completion": "서울의 현재 기온은 약 22°C입니다."
        },
        {
            "prompt": "리마의 현재 기온은 어떻게 되나요?",
            "completion": "리마의 현재 기온은 약 19°C입니다."
        },
        {
            "prompt": "리야드의 현재 기온은 어떻게 되나요?",
            "completion": "리야드의 현재 기온은 약 36°C입니다."
        },
        {
            "prompt": "싱가포르의 현재 기온은 어떻게 되나요?",
            "completion": "싱가포르의 현재 기온은 약 27°C입니다."
        },
        {
            "prompt": "뉴델리의 현재 기온은 어떻게 되나요?",
            "completion": "뉴델리의 현재 기온은 약 33°C입니다."
        },
        {
            "prompt": "상하이의 현재 기온은 어떻게 되나요?",
            "completion": "상하이의 현재 기온은 약 24°C입니다."
        },
        {
            "prompt": "모스크바의 현재 기온은 어떻게 되나요?",
            "completion": "모스크바의 현재 기온은 약 21°C입니다."
        },
        {
            "prompt": "멜버른의 현재 기온은 어떻게 되나요?",
            "completion": "멜버른의 현재 기온은 약 10°C입니다."
        },
        {
            "prompt": "토론토의 현재 기온은 어떻게 되나요?",
            "completion": "토론토의 현재 기온은 약 20°C입니다."
        },
        {
            "prompt": "로스앤젤레스의 현재 기온은 어떻게 되나요?",
            "completion": "로스앤젤레스의 현재 기온은 약 25°C입니다."
        },
        {
            "prompt": "파리의 현재 기온은 어떻게 되나요?",
            "completion": "파리의 현재 기온은 약 23°C입니다."
        },
        {
            "prompt": "리우데자네이루의 현재 기온은 어떻게 되나요?",
            "completion": "리우데자네이루의 현재 기온은 약 24°C입니다."
        },
        {
            "prompt": "방콕의 현재 기온은 어떻게 되나요?",
            "completion": "방콕의 현재 기온은 약 30°C입니다."
        },
        {
            "prompt": "시카고의 현재 기온은 어떻게 되나요?",
            "completion": "시카고의 현재 기온은 약 27°C입니다."
        },
        {
            "prompt": "마이애미의 현재 기온은 어떻게 되나요?",
            "completion": "마이애미의 현재 기온은 약 32°C입니다."
        },
        {
            "prompt": "몬트리올의 현재 기온은 어떻게 되나요?",
            "completion": "몬트리올의 현재 기온은 약 22°C입니다."
        },
        {
            "prompt": "런던의 현재 기온은 어떻게 되나요?",
            "completion": "런던의 현재 기온은 약 21°C입니다."
        },
        {
            "prompt": "이스탄불의 현재 기온은 어떻게 되나요?",
            "completion": "이스탄불의 현재 기온은 약 27°C입니다."
        },
        {
            "prompt": "두바이의 현재 기온은 어떻게 되나요?",
            "completion": "두바이의 현재 기온은 약 33°C입니다."
        },
        {
            "prompt": "나이로비의 현재 기온은 어떻게 되나요?",
            "completion": "나이로비의 현재 기온은 약 20°C입니다."
        },
        {
            "prompt": "부에노스아이레스의 현재 기온은 어떻게 되나요?",
            "completion": "부에노스아이레스의 현재 기온은 약 12°C입니다."
        },
        {
            "prompt": "멕시코시티의 현재 기온은 어떻게 되나요?",
            "completion": "멕시코시티의 현재 기온은 약 19°C입니다."
        }
    ]
}

# 학습 데이터 생성
list_message = []
num_data = len(dataset["train"])  # 데이터셋의 길이를 사용

for i in range(num_data):
    prompt = dataset["train"][i]["prompt"]
    completion = dataset["train"][i]["completion"]
    print("질문:", prompt)
    print("답변:", completion)
    message = [
        {"role": "user", "content": prompt},
        {"role": "assistant", "content": completion},
    ]
    list_message.append(message)

with open("completion1.jsonl", "w") as file:
    for messages in list_message:
        json_line = json.dumps({"messages": messages})
        file.write(json_line + '\n')