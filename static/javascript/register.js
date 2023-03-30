let x = document.getElementById("login");
let y = document.getElementById("register");
let z = document.getElementById("btn");


$(document).ready(function () {
    $("#register-btn").click(function () {
        x.style.left = "-400px";
        y.style.left = "50px";
        z.style.left = "110px";
    });
    $("#login-btn").click(function () {
        x.style.left = "50px";
        y.style.left = "450px";
        z.style.left = "0";
    });
    $("#forgot").click(function () {
        window.location.href = '/forgot';
    })
    $('#submit-login-form').click(async function () {
        let response = await (await fetch("/api/login_pass", {
            method: "POST",
            headers: {
                'Accept': 'application/json'
            },
            body: JSON.stringify({
                "username": document.getElementById("login-email").value,
                "password": document.getElementById("login-password").value
            })
        })).json()
        if (response.correct) {
            console.log("login successfully")
            sessionStorage.setItem("user_id", response.id)
            window.location.href = "/main";

        }


    })
    $('#submit-register-form').click(async function () {
        let response = await (await fetch("/api/register", {
            method: "POST",
            headers: {
                'Accept': 'application/json'
            },
            body: JSON.stringify({
                "username": document.getElementById("register-email").value,
                "password": document.getElementById("register-password").value
            })
        })).json()
        console.log(response)
        if (response.id) {
            sessionStorage.setItem("user_id", response.id)
            window.location.href = "/main"

        }


    })

    $('#submit-register-form').click(async function () {
        let response = await (await fetch("/api/register", {
            method: "POST",
            headers: {
                'Accept': 'application/json'
            },
            body: JSON.stringify({
                "username": document.getElementById("register-email").value,
                "password": document.getElementById("register-password").value
            })
        })).json()
        console.log(response)
        if (response.id) {
            sessionStorage.setItem("user_id", response.id)
            window.location.href = "/main"

        }


    })

});








