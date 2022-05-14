var profile_name = document.getElementById('profile-name')
var editname_input = document.getElementById('editname-input')
var editname_btn = document.getElementById('editname-btn')
var settings = document.getElementById('settings')
var settings_body = document.getElementById('settings-body')
var name_edit_container = document.getElementById('name-edit-container')

var IsNameEdit = true;
var IsSettingsOpen = false

function EditName(){
    if(IsNameEdit){
        editname_input.style.visibility = 'hidden';

        name_edit_container.style.visibility = 'hidden';
        name_edit_container.style.width = '0';

        profile_name.style.visibility = 'visible';
        profile_name.style.width = 'initial';
        editname_btn.getElementsByClassName('btn-img').item(0).style.visibility = 'visible';
        editname_btn.getElementsByClassName('btn-img').item(0).style.height= '30px';
        editname_btn.getElementsByClassName('btn-img').item(1).style.visibility = 'hidden';
        IsNameEdit = false;
    }
    else{
        editname_input.style.visibility = 'visible';

        name_edit_container.style.visibility = 'visible';
        name_edit_container.style.width = 'initial';

        profile_name.style.visibility = 'hidden';
        profile_name.style.width = 0;
        editname_btn.getElementsByClassName('btn-img').item(1).style.visibility = 'visible';
        editname_btn.getElementsByClassName('btn-img').item(0).style.visibility = 'hidden';
        editname_btn.getElementsByClassName('btn-img').item(0).style.height= '0';
        IsNameEdit = true;
    }
    console.log('IN')
}

function closeUpSettings(btn){
    if(IsSettingsOpen){
        settings_body.style.height= 0;
        settings.style.height = '50vh';
        IsSettingsOpen = false;
    }
    else {
        settings_body.style.height = 'var(--settings-body-height)';
        settings.style.height = 'var(--settings-height)';
        IsSettingsOpen = true;
    }
}

closeUpSettings();
EditName();
