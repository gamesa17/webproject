var lightState = true;
const root = document.querySelector(':root'); 
const rootStyle = getComputedStyle(root);

function themeChange(){ 
if(lightState === true){
    root.style.setProperty('--active-bg', rootStyle.getPropertyValue('--d-theme-bg'));
    root.style.setProperty('--active-main-text', rootStyle.getPropertyValue('--uni-white'));
    root.style.setProperty('--active-secondary-text', rootStyle.getPropertyValue('--uni-grey-light'));
    root.style.setProperty('--active-shadow', rootStyle.getPropertyValue('--d-theme-shadow'));
    lightState = false;
}
else{
    root.style.setProperty('--active-bg', rootStyle.getPropertyValue('--uni-white'));
    root.style.setProperty('--active-main-text', rootStyle.getPropertyValue('--uni-graphite'));
    root.style.setProperty('--active-secondary-text', rootStyle.getPropertyValue('--uni-text-grey'));
    root.style.setProperty('--active-shadow', rootStyle.getPropertyValue('--l-theme-shadow'));
    lightState = true
}
}