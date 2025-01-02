// 전역 변수 미리 설정
let answer = []; // 정답 숫자 배열
let attempts = 9; // 시도 가능 횟수

// 게임 초기화 함수
function initializeGame() {
    // 시도 횟수 설정
    attempts = 9;
    // 중복되지 않는 3개의 랜덤 숫자 생성
    answer = [];
    while (answer.length < 3) {
        const randomNum = Math.floor(Math.random() * 10); // 0~9 랜덤 숫자
        if (!answer.includes(randomNum)) {
            answer.push(randomNum);
        }
    }

    // HTML 업데이트
    document.getElementById("attempts").textContent = attempts;
    document.getElementById("number1").value = "";
    document.getElementById("number2").value = "";
    document.getElementById("number3").value = "";
    document.getElementById("results").innerHTML = "";
    document.getElementById("game-result-img").src = "";
    document.querySelector(".submit-button").disabled = false;
}

// 숫자 확인 함수
function check_numbers() {
    // 입력 값 가져오기
    const input1 = document.getElementById("number1").value;
    const input2 = document.getElementById("number2").value;
    const input3 = document.getElementById("number3").value;

    // 입력값 검증
    if (input1 === "" || input2 === "" || input3 === "") {
        alert("모든 칸에 숫자를 입력하세요!");
        return;
    }

    // 입력값 배열로 저장
    const inputs = [parseInt(input1), parseInt(input2), parseInt(input3)];
    
    // 중복 확인 과정
    const sameInputs = new Set(inputs); // inputs를 집합으로 만들어서 길이로 비교 예정
    if (sameInputs.size !== inputs.length) {
        document.getElementById("number1").value = "";
        document.getElementById("number2").value = "";
        document.getElementById("number3").value = "";
        return;
    }


    // 스트라이크와 볼 카운트 계산
    let strikes = 0;
    let balls = 0;

    inputs.forEach((num, idx) => {
        if (answer.includes(num)) {
            if (answer[idx] === num) {
                strikes++; // 숫자와 위치가 모두 맞음
            } else {
                balls++; // 숫자는 맞지만 위치가 틀림
            }
        }
    });

    // 결과 생성
    let result;
    if (strikes === 0 && balls === 0) {
        result = "O"; // 아웃
    } else {
        result = `${strikes}S ${balls}B`;
    }

    // 결과 출력
    const resultsDiv = document.getElementById("results");
    const resultItem = document.createElement("div");
    resultItem.innerHTML = `<span>${inputs.join(" ")}</span> : <span class="strike">${strikes}S</span> <span class="ball">${balls}B</span>`;
    if (result === "O") {
        resultItem.innerHTML = `<span>${inputs.join(" ")}</span> : <span class="out">O</span>`;
    }
    resultsDiv.appendChild(resultItem);

    // 시도 횟수 감소 및 업데이트
    attempts--;
    document.getElementById("attempts").textContent = attempts;

    // 게임 종료 체크
    if (strikes === 3) {
        // 승리
        document.getElementById("game-result-img").src = "success.png";
        document.querySelector(".submit-button").disabled = true;
    } else if (attempts === 0) {
        // 패배
        document.getElementById("game-result-img").src = "fail.png";
        document.querySelector(".submit-button").disabled = true;
    }

    // 입력창 초기화
    document.getElementById("number1").value = "";
    document.getElementById("number2").value = "";
    document.getElementById("number3").value = "";
}

// 게임 시작 시 초기화
initializeGame();
