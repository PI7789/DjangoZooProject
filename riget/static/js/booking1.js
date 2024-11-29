function update_cost(){
        document.getElementById("booking_button").disabled = false;

        // get the dates
        let arrive = document.getElementById('id_hotel_booking_date_arrive').value
        let leave = document.getElementById('id_hotel_booking_date_leave').value

        arrive = new Date(arrive)
        leave = new Date(leave)
        diff = leave.getTime() - arrive.getTime();
        days = Math.round((diff/(1000*60*60*24)));
        if (days < 0) {
            let price = document.getElementById('hotel_output')
            price.innerHTML = "Hotel cost: Date is invalid."

            document.getElementById("booking_button").disabled = true;
        
        }else if(String(days) == "NaN"){
            let price = document.getElementById('hotel_output')
            price.innerHTML = "Hotel cost: Dates Not Chosen"
            document.getElementById("booking_button").disabled = true;

        }else{
            // if the dates are ok

            let total = parseInt(adults.value) * 65
            + parseInt(children.value) * 35
            + parseInt(oaps.value) * 45


            total = total * days
            let output1 = document.getElementById('hotel_output')

            if (total <= 0 ){
                
                output1.innerHTML = "Hotel cost: Choose the amount of People."
                document.getElementById("booking_button").disabled = true;
            } else{
        
                output1.innerHTML = "Hotel cost: £" + String(total)
                document.getElementById("booking_button").disabled = false;
            }
            



        }

      

}

let adults = document.getElementById("id_hotel_booking_adults");
adults.addEventListener("change", update_cost)
let children = document.getElementById("id_hotel_booking_children");
children.addEventListener("change", update_cost)
let oaps = document.getElementById("id_hotel_booking_oap");
oaps.addEventListener("change", update_cost)
// dates
let arrive1 = document.getElementById("id_hotel_booking_date_arrive");
arrive1.addEventListener("change", update_cost)
let leave1 = document.getElementById("id_hotel_booking_date_leave");
leave1.addEventListener("change", update_cost)