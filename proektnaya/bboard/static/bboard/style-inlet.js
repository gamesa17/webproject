const html = document.documentElement;

var button_switcher_press = document.getElementById('button-switcher-press');
var condition_non_active = document.getElementById('condition-non-active');
var condition_active = document.getElementById('condition-active');
var _root = document.querySelector(':root');


var IsDarkThemem = true;


function ThemeSwitch() {
    if(IsDarkThemem == false){
    _root.style.setProperty('--color-first', 'black');
    _root.style.setProperty('--color-secondary', 'white');
    _root.style.setProperty('--color-rigid', 'var(--color-black-embient)');
    IsDarkThemem = true;
    condition_non_active.style.opacity = 1;
    condition_active.style.opacity = 0;
    }
    else{
        _root.style.setProperty('--color-first', 'white');
        _root.style.setProperty('--color-secondary', 'black');
        _root.style.setProperty('--color-rigid', 'var(--color-grey-embient)');
        IsDarkThemem = false;
        condition_non_active.style.opacity = 0;
        condition_active.style.opacity = 1;
    }
}

document.querySelectorAll('.scaleable__image').forEach(imageDiv => {
    imageDiv.addEventListener('click', (event) => {

      if(event.target.classList.contains("scaleable__image-selected")){
        document.querySelectorAll('.scaleable__image').forEach(imageDiv => imageDiv.classList.remove("scaleable__image-selected"))

        }else{
            document.querySelectorAll('.scaleable__image').forEach(imageDiv => imageDiv.classList.remove("scaleable__image-selected"))
            event.target.classList.add("scaleable__image-selected")
        }

    })
})

 function imageScaleOnClick(image){
    if(image.style.alignSelf == 'center'){
        image.style.alignSelf = 'baseline';
        image.style.justifySelf = 'baseline';
        image.style.position ='static';

    }
    else {
        image.style.alignSelf = 'center';
        image.style.justifySelf = 'center';
        image.style.position ='absolute';
    }
 }


ThemeSwitch();