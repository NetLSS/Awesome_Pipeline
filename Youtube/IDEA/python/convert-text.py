import os
import textwrap  # 추가

def transform_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # 문자열 변환
        content = content.replace('...', '')     # "..." → ""
        content = content.replace(', ', ',\n')   # ", " → ",\n"
        content = content.replace('. ', '.\n')   # ". " → ".\n"
        content = content.replace('" ', '"\n')   # '" ' → '"\n'

        # 각 줄의 글자가 30글자 수가 넘어 가면, 30글자 근처 공백 기준으로 개행
        wrapped_lines = []
        for line in content.splitlines():
            if len(line) <= 30:
                wrapped_lines.append(line)
            else:
                wrapped = textwrap.fill(line, width=30, break_long_words=False, break_on_hyphens=False)
                wrapped_lines.append(wrapped)
        content = '\n'.join(wrapped_lines)

        # 새 파일 이름 생성
        base, ext = os.path.splitext(file_path)
        new_file_path = f"{base}_converted{ext}"

        # 변환된 내용 저장
        with open(new_file_path, 'w', encoding='utf-8') as file:
            file.write(content)

        print(f"변환이 완료되었습니다. 새 파일: {new_file_path}")

    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {file_path}")
    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    path = input("변환할 텍스트 파일의 경로를 입력하세요: ").strip()
    transform_text_file(path)
