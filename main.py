def app():
    days_of_week = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    print(days_of_week)
    print(days_of_week[1])  # tue
    days_of_week.count("wed")  # wed 와 같은 값은 몇개 있는지
    days_of_week.clear()  # []
    days_of_week.reverse()  # 반대로 순서 변경
    days_of_week.append("ddd")  # ddd 값 추가
    days_of_week.remove("mon")  # mon 삭제


if __name__ == '__main__':
    app()
