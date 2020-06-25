// //Exercise #1
// function checkDriverAge(age) { 

// if (Number(age) < 18) {
//     alert("Sorry, you are too young to drive this car. Powering off");
// } else if (Number(age) > 18) {
//     alert("Powering On. Enjoy the ride!");
// } else if (Number(age) === 18) {
//     alert("Congratulations on your first year of driving. Enjoy the ride!");
// }
// } 

// checkDriverAge(19)  


//Exercise 3
// function changeSum (change) { 
//             let sum = "" 
//             finalsum = 0
//             change[0] = change[0] * .25
//             change[1] = change[1] * .10 
//             change[2] = change[2] * .05 
//             change[3] = change[3] * .01 
//             for ( i of change) { 
//                    let sum = i 
//                    finalsum = finalsum + sum
//             }
            
//     return finalsum

// } 

// function changeEnough(change, cost) { 

//         if (changeSum(change) < cost ) { 

//             console.log("False") 
//         } 

//         else { 
//             console.log("True")
//         }


// }  

//Exercise #5

function hotel_price (days) {
        finalhotel = days * 140
    return finalhotel
    
}

function plane_ride_cost (place) { 
    if (place == 'London' ) { 
       return 183 
    }
    
    else if (place == 'Paris') {
        return 220
    }
    else {
        return 300
    }

}  
 

function rental_car_cost (days) {

    cost = days * 40
    if (days > 10) 
        return days * 40 - cost * .05
    else { 
        return cost
    }
}


function total_vacation_cost (hoteldays, place, cardays) { 
    console.log( "$" + (hotel_price(hoteldays) + plane_ride_cost(place) + rental_car_cost(cardays)))
}
