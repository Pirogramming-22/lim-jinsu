num = 0
end = False

while not end:
    while True:
        user_input = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")

        # 정수인지 검사
        if not user_input.isdigit():
            print("정수를 입력하세요")
            continue

        # 정수로 변환
        cnt = int(user_input)
        
        # 1, 2, 3 중 하나인지 검사
        if cnt not in [1, 2, 3]:
            print("1, 2, 3 중 하나를 입력하세요")
            continue

        # 검사를 통과하면 루프 종료
        break

    for i in range(cnt):
        num += 1
        print(f"playerA : {num}")
        if num == 31:
            print("playerB win!")
            end = True
            break

    if end == True:
        break

    while True:
        user_input = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")

        # 정수인지 검사
        if not user_input.isdigit():
            print("정수를 입력하세요")
            continue

        # 정수로 변환
        cnt = int(user_input)
        
        # 1, 2, 3 중 하나인지 검사
        if cnt not in [1, 2, 3]:
            print("1, 2, 3 중 하나를 입력하세요")
            continue

        # 검사를 통과하면 루프 종료
        break

    # player B's turn
    for i in range(cnt):
        num += 1
        print(f"playerB : {num}")
        if num == 31:
            print("playerA win!")
            end = True
            break