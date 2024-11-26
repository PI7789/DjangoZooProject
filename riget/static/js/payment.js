function pointpayment(){        
    var totalcost = 0 
    if (update.checked){
        
    
    if (points > cost) {
        totalcost = 0
    } else {
        totalcost = cost - points
    }
} else{
    totalcost = cost
}
output = document.getElementById("hotel_output")    
output.innerHTML = "Hotel cost : £" + totalcost

}

update = document.getElementById("use_points")
update.addEventListener("change", pointpayment)