document.addEventListener('DOMContentLoaded', (EventDOMLoaded) => {
    document.querySelectorAll('.nav-list').forEach(list => {
        list.querySelectorAll('.nav-slot').forEach( (call, i , a) => {
            list.style.height = call.scrollHeight + 86 + 'px';
            if(call === a.item(a.length - 1) ) {
                call.style.borderRadius = '0 0 20px 20px';
                call.style.height = call.childElementCount * 50 + 'px';
            }
        })
    })
})

document.querySelectorAll('.nav-button').forEach(button => {
    button.addEventListener('click', (event) => {
        if(button.classList.contains("nav-button-selected")){
            button.classList.remove("nav-button-selected");
            button.querySelectorAll('img').forEach(img => { img.style.transform = 'rotate(0deg)';})
            button.querySelectorAll('svg').forEach(svg => { svg.style.transform = 'rotate(0deg)';})
            button.parentElement.querySelectorAll('.nav-slot').forEach(slot => {
                slot.style.opacity = '0%';
                slot.style.visibility = 'hidden';
            })
        }
        else{
            button.classList.add("nav-button-selected");
            button.querySelectorAll('img').forEach(img => { img.style.transform = 'rotate(180deg)';})
            button.querySelectorAll('svg').forEach(svg => { svg.style.transform = 'rotate(180deg)';})
            button.parentElement.querySelectorAll('.nav-slot').forEach(slot => {
            slot.style.visibility = 'visible';
            slot.style.opacity = '100%';
            })
        }
    })
})

document.querySelectorAll('.nav-list').forEach(list => {
    list.addEventListener('mouseleave', (event) => {
        list.querySelector('.nav-button').classList.remove("nav-button-selected");
        list.querySelector('.nav-button').querySelectorAll('img').forEach(img => { img.style.transform = 'rotate(0deg)';})
        list.querySelector('.nav-button').querySelectorAll('svg').forEach(svg => { svg.style.transform = 'rotate(0deg)';})
        list.querySelectorAll('.nav-slot').forEach(slot => {
            slot.style.opacity = '0%';
            slot.style.visibility = 'hidden';
        })
    })
})

window.onload = function() {
    // need adaptive system to dark theme 
    var logo = document.getElementById('logo');
    var doc = logo.contentDocument;
    var svgElementOne = doc.getElementsByClassName("svg0");
    var svgAnimationOffset = doc.getElementsByClassName("anim-offset");
    var svgAnimationOpacity = doc.getElementsByClassName("anim-opacity");
   
    document.querySelector('.logo').addEventListener('mouseover', (event) =>{
        svgElementOne[0].setAttribute("fill", "url(#Gradient1)");
        svgAnimationOffset[0].beginElement();
        svgAnimationOpacity[0].beginElement();
        svgElementOne[0].setAttribute("fill-opacity", "1");
    })
};
