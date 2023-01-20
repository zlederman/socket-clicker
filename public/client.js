var socket = io();
socket.on('connect', function() {
    socket.emit('message', {data: 'I\'m connected!'});
});

socket.on('updated-counter',function (counter){
    const counterView = document.getElementById("counter")
    counterView.innerText = counter
})
const emitClick = () => {
    socket.emit('increment')
}

const button = document.getElementById("big-button")
button.onclick = emitClick