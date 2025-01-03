let startTime = 0;
let elapsedTime = 0;
let timerInterval;
const timeDisplay = document.querySelector(".time-display");

const recordBox = document.querySelector(".record-box");
const deleteButton = document.getElementById("delete-records");
const selectAllCheckbox = document.getElementById("select-all");

// 시간 포맷 (초와 소수점 단위)
function timeToString(time) {
    const seconds = (time / 1000).toFixed(1);
    return `${seconds}`;
}

// 화면에 시간 출력
function printTime() {
    timeDisplay.innerText = timeToString(elapsedTime);
}

// 시작 버튼
function start() {
    if (!timerInterval) {
        startTime = Date.now() - elapsedTime;
        timerInterval = setInterval(() => {
            elapsedTime = Date.now() - startTime;
            printTime();
        }, 100);
    }
}

// 정지 버튼
function stop() {
    clearInterval(timerInterval);
    timerInterval = null;
    // 정지 시 기록 추가
    const record = document.createElement("div");
    record.className = "record";
    record.innerHTML = `
        <input type="checkbox" class="record-checkbox">
        <span>기록: ${timeToString(elapsedTime)}초</span>
    `;
    recordBox.appendChild(record);
}

// 초기화 버튼
function reset() {
    clearInterval(timerInterval);
    timerInterval = null;
    elapsedTime = 0;
    printTime();
    // 기록 초기화
    recordBox.innerHTML = `
        <div class="record-header">
            <label>
                <input type="checkbox" id="select-all"> 전체 선택
            </label>
            <button id="delete-records">삭제</button>
        </div>
    `;
    attachEventListeners(); // 초기화 후 이벤트 리스너 재설정
}

// 체크된 항목 삭제
function deleteRecords() {
    const checkboxes = document.querySelectorAll(".record-checkbox");
    checkboxes.forEach(checkbox => {
        if (checkbox.checked) {
            checkbox.parentElement.remove();
        }
    });
}

// 전체 선택 토글
function toggleSelectAll() {
    const checkboxes = document.querySelectorAll(".record-checkbox");
    checkboxes.forEach(checkbox => {
        checkbox.checked = selectAllCheckbox.checked;
    });
}

// 이벤트 리스너 연결
function attachEventListeners() {
    deleteButton.addEventListener("click", deleteRecords);
    selectAllCheckbox.addEventListener("change", toggleSelectAll);
}

document.getElementById("start").addEventListener("click", start);
document.getElementById("stop").addEventListener("click", stop);
document.getElementById("reset").addEventListener("click", reset);

// 초기 이벤트 리스너 설정
attachEventListeners();
