$(document).ready(function () {
    if (sessionStorage.getItem("date")){
        document.getElementById("calendar").value = sessionStorage.getItem("date")
    }


    $("#addzan-btn").click(function () {
        let date = document.getElementById("calendar").value
        if (date) {
            sessionStorage.setItem("date", date)
            window.location.href = "/add_train";
        }

    });
    $("#addfood-btn").click(function () {
        let date = document.getElementById("calendar").value
        if (date) {
            sessionStorage.setItem("date", date)
            window.location.href = "/add_food";
        }

    });
    $("#forgot").click(function () {
        window.location.href = '/forgot';
    })

    $('#show-btn').click(async function () {
        console.log(document.getElementById("calendar").value)
        if (document.getElementById("calendar").value) {
            let food_response = await (await fetch("/api/get_food", {
                method: "POST",
                headers: {
                    'Accept': 'application/json'
                },
                body: JSON.stringify({
                    "id": sessionStorage.getItem("user_id"),
                    "date": document.getElementById("calendar").value
                })
            })).json()
            let train_response = await (await fetch("/api/get_trains", {
                method: "POST",
                headers: {
                    'Accept': 'application/json'
                },
                body: JSON.stringify({
                    "id": sessionStorage.getItem("user_id"),
                    "date": document.getElementById("calendar").value
                })
            })).json()

            let food_table = document.getElementById('food-table')
            let sum_kkal = 0
            let sum_j = 0
            let sum_b = 0
            let sum_u = 0
            for (let i = 0; i < train_response.length; i++) {
                let div = document.createElement("div")
                div.classList.add("info-block")
                div.textContent = train_response[i][0].toString() + " " + train_response[i][1].toString()
                food_table.appendChild(div)
            }
            let train_table = document.getElementById('train-table')
            for (let i = 0; i < food_response.length; i++) {
                let line = food_response[i]
                let div = document.createElement("div")
                div.classList.add("info-block")
                sum_b += Number(line[1])
                sum_j += Number(line[2])
                sum_u += Number(line[3])
                sum_kkal += Number(line[4])
                div.textContent = line[0].toString() + " b: " + line[1].toString() + " j: " +
                    line[2].toString() + " u: " + line[3].toString() + " kkal: " + line[4].toString()
                train_table.appendChild(div)
            }
            let last_kkal = food_response[food_response.length-1][4].toString()

            $("#summ-b").text("b: " + sum_b.toString())
            $("#summ-j").text("j: " + sum_j.toString())
            $("#summ-u").text("u: " + sum_u.toString())
            $("#sum-kkal").text("total kkal: " + sum_kkal.toString())
            $("#last-kkal").text("last kkal: " + last_kkal.toString())




            //
            // console.log(food_response)
            // console.log(train_response)
        }

    })

})
