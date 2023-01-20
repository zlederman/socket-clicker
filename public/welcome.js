
const submitUname = () => {
    let textField = document.getElementById('uname');
    let username = textField.value
    console.log(username)
    if(username === "" || username === "username"){
        alert("please enter username!");
        return;
    }
    else{
        uri = window.location.href.split("?").at(0)
        uri += `clicker?uname=${username}`
        window.location.assign(uri)
    }
    return false
}
const submitButton = document.getElementById('submit')
submitButton.onclick = submitUname
