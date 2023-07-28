function mesajGizleme(){
    let mesaj = document.getElementById('mesaj')
    if(mesaj){
        mesaj.style.display = "none";
    }
}

setTimeout(mesajGizleme,2000)