
createComments(getComments("Neutral"));
document.addEventListener('click', e=>{
    const isDropdownButton = e.target.matches("[data-dropdown-button]")
    if(!isDropdownButton && e.target.closest('[data-dropdown]') != null) return

    let currentDropdown
    if(isDropdownButton){
        currentDropdown = e.target.closest('[data-dropdown]')
        currentDropdown.classList.toggle('active')

    }
    document.querySelectorAll("[data-dropdown].active").forEach(dropdown =>{
        if(dropdown == currentDropdown) return
        dropdown.classList.remove('active')
    })
})  

const btn = document.querySelectorAll('.option');
for(var i =0; i < btn.length;i++){
    createEvent(btn[i]);
}

function createEvent(btn){
    btn.addEventListener('click', function(event){
        var txt = btn.textContent || btn.innerText;
        dropDown = document.querySelector(".dropdown")
        dropDown.classList.remove('active')
        document.querySelector(".link").textContent = txt;
        removeAllComments();
        var comments = getComments(txt);
        createComments(comments)
        
        
    });
}

function removeAllComments(){
    elem = document.querySelector(".comments");
    elem.innerHTML = '';
}

function createComments(comments){
    for(var i = 0;i < comments.length;i++){
        createComment(comments[i]);
    }
}

function createComment(text){
    elem = document.querySelector(".comments");

    elem.innerHTML += `<div class=\"comment\">${text}</div>`;
}

function getComments(cat){
    cat = cat.trim();
    if(cat == "Neutral"){
        return ["n1","n2","n3"];
    }
    else if(cat == "Positive"){
        return ["p1","p2","p3"];
    }
    else if(cat = "Negative"){
        return ["neg1","neg2","neg3"];
    }
}

