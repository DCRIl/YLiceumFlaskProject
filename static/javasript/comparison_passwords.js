var p1 = document.getElementById("password-input1");
var p2 = document.getElementById("password-input2");
var er = document.getElementById("err");
var but = document.getElementById("peg");
setInterval(() => {
    er = document.getElementById("err");
    but = document.getElementById("peg");
    if (er.textContent === "Пароли совпадают") {
        but.disabled = false;
    } else {
        but.disabled = true;
    }
}, 1);

function passwords() {
    p1 = document.getElementById("password-input1");
    p2 = document.getElementById("password-input2");
    er = document.getElementById("err");
    if (p1.value === p2.value && p1.value != "" && p2.value != "") {
        er.textContent = "Пароли совпадают";
        er.style.color = "#00FF00";
    } else if (p1.value != p2.value && p1.value != "" && p2.value != "") {
        er.textContent = "Пароли не совпадают";
        er.style.color = "#FF0000";
    } else {
        er.textContent = "Придумайте пароль";
        er.style.color = "#555555";
    }
}