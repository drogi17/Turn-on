function make(){
    var text = document.getElementById("text").value;
    if (text != ""){
        window.location.href = "/make_by_text/" + text;
    }
}
