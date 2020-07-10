function letters() {
    let box = document.getElementsByTagName("input")[0];
    let word = box.value;
    let letter = word.substr(-1, 1);
    if (parseInt(letter)) {
        box.value = word.substring(0, word.length - 1);
    }
}