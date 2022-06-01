(function(window, document, undefined){
window.onload = init;

function init(){
//setup before functions
let typingTimer;                //timer identifier
let doneTypingInterval = 5000;  //time in ms (5 seconds)
let myInput = document.getElementsByTagName('input');

//on keyup, start the countdown
for (let input of myInput) {
    input.addEventListener('keyup', () => {
    clearTimeout(typingTimer);
    if (input.value) {
        typingTimer = setTimeout(func, doneTypingInterval);
    }
});
}

function func() {
    document.getElementById("save").submit();
};
}
})(window, document, undefined);