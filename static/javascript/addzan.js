$(document).ready(function(){
    $("#addzan-btn").click(async function(){
        let name_time = [document.getElementById("zan").value, document.getElementById("time").value]
        let response = await (await fetch("/api/add_train", {
            method: "POST",
            headers: {
                'Accept': 'application/json'
            },
            body: JSON.stringify({
                "id": sessionStorage.getItem("user_id"),
                "train": name_time,
                "date": sessionStorage.getItem("date")
            })
        })).json()
        console.log(response)
        if (response.ok){
            window.location.href = "/main";
        }
    });
})