$(document).ready(function(){
    $("#addfood-btn").click(async function(){
        let properties = [document.getElementById("food").value,
            document.getElementById("b").value,
            document.getElementById("j").value,
            document.getElementById("u").value,
            document.getElementById("kkal").value
        ]
        console.log(properties)
        let response = await (await fetch("/api/add_food", {
            method: "POST",
            headers: {
                'Accept': 'application/json'
            },
            body: JSON.stringify({
                "id": sessionStorage.getItem("user_id"),
                "food": properties,
                "date": sessionStorage.getItem("date")
            })
        })).json()
        console.log(response)
        if (response.ok){
            window.location.href = "/main";
        }
    });
})