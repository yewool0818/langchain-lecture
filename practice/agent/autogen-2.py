# from utils import get_openai_api_key
# OPENAI_API_KEY = get_openai_api_key()
from autogen import ConversableAgent

llm_config = {"model": "gpt-3.5-turbo"}

# cathy와 joe의 대화 -> 둘은 코미디언이라고 가정
# 코미디언의 만담
cathy = ConversableAgent(
    name="야옹님",
    system_message=
    "당신의 이름은 야옹님이고 당신은 짧은 재미난 이야기를 잘 만드는 코미디언입니다",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

joe = ConversableAgent(
    name="멍멍님",
    system_message=
    "당신의 이름은 멍멍님이고 당신은 짧은 재미난 이야기를 잘 만드는 코미디언입니다"
    "이전 대화의 내용을 이어서 다음 재미난 이야기를 시작하세요.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

# joe부터 시작
chat_result = joe.initiate_chat(
    recipient=cathy,
    message="나는 야옹님이야, 우리 재미난 이야기를 이어서 나가 볼까?",
    max_turns=2, # 둘의 대화는 2번 반복
)
