let offset = 0

function Move() {
    setInterval(function () {
        if (offset == 350) {
            Move2()
        } else {
            offset++
        }
        document.getElementById("animate").style.left = offset + "px"
    }, 50)
}

function myMove2() {
    setInterval(function () {
        if (offset == 0) {
            myMove()
        } else {
            offset--
        }
        document.getElementById("animate").style.right = "0"

    }, 50)
}