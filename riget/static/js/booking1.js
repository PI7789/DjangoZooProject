function update_cost(){
        let arrive = document.getElementById('id_hotel_booking_date_arrive').value
        let leave = document.getElementById('id_hotel_booking_date_leave').value

        arrive = new Date(arrive)
        leave = new Date(leave)
        diff = leave.getTime() - arrive.getTime();
        days = Math.round((diff/(1000*60*60*24)));
        if (days < 0) {
            let price = document.getElementById('hotel_output')
            price.innerHTML = "Hotel cost: Date is invalid."
            return
        }

        else if(String(days) == "NaN"){
            let price = document.getElementById('hotel_output')
            price.innerHTML = "Hotel cost: Dates Not Chosen"

        }else{


            let total = parseInt(adults.value) * 65
            + parseInt(children.value) * 35
            + parseInt(oaps.value) * 45


            total = total * days


            let price = document.getElementById('hotel_output')
            price.innerHTML = "Hotel cost: £" + String(total)

        }

}

let adults = document.getElementById("id_hotel_booking_adults");
adults.addEventListener("change", update_cost)
let children = document.getElementById("id_hotel_booking_children");
children.addEventListener("change", update_cost)
let oaps = document.getElementById("id_hotel_booking_oap");
oaps.addEventListener("change", update_cost)