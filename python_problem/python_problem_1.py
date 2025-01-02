import random 

num = 0
end = False

# brGame 함수 정의
def brGame(player, num):
    if player == "computer":
        cnt = random.randint(1,3)

    else:
        while True:
            user_input = input(f"{player} 부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")
        
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
        print(f"{player} : {num}")
        if num == 31:
            return num, True  # num과 게임 종료 상태 반환
    
    return num, False  # num과 게임 미종료 상태 반환

# 메인 게임 루프
while not end:
    # computer의 차례
    num, end = brGame("computer", num)
    if end:
        print("player win!")
        break

    # Player의 차례
    num, end = brGame("player", num)
    if end:
        print("computer win!")
        break
