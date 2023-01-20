var socket = io();
socket.on('connect', function() {
    let stat = document.getElementById('status')
    stat.innerText = 'Connected'
})

window.onload = () => {
    let uname = window.location.href
    .split('?')
    .pop()
    .split('=')
    .pop()

    socket.emit('join', {uname: uname})
}
socket.on('join-res',function(data){
    let room = document.getElementById('room-id')
    let uname = document.getElementById('username')
    let counterView = document.getElementById("counter")
    room.innerText = "Room Id: " + data.room
    uname.innerText = "Username: " + data.uname
    counterView.innerText = data.count
})
socket.on('updated-counter',function (counter){
    const counterView = document.getElementById("counter")
    counterView.innerText = counter
})
const emitClick = () => {
    let roomIdElement = document.getElementById('room-id')
    let roomId = roomIdElement.innerText.split(" ").pop()
    socket.emit('increment',{'room':roomId})
}
const button = document.getElementById("big-button")
button.onclick = emitClick