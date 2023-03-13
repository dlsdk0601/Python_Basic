def app():
    # Tuple
    # List 와 아주 비슷함
    days = ("Mon", "Tue", "Wed") # 절대 불변할 데이터 이기 때문에 상황 봐서 list, Tuple 선택해서 쓰기
    days.count()  # 3
    # 이외에는 메서드가 없음
    print(days[0]) # "Mon"
    print(days[-1]) # "Wed"


if __name__ == '__main__':
    app()
