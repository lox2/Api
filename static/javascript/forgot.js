$("#submit-forgot-form").click(async function restore_pass() {
    if (document.getElementById("password").value === document.getElementById("passwordConfirm").value) {
        let response = await (await fetch("/api/change_password", {
            method: "POST",
            headers: {
                'Accept': 'application/json'
            },
            body: JSON.stringify({
                "username": document.getElementById("email").value,
                "password": document.getElementById("password").value
            })
        })).json()
        if (response.ok) {
            console.log("password reset successfully")
            window.location.href = "/";
        }
    }

})