var auth_window = document.getElementById('auth-window');
var auth_switcher = auth_window.getElementsByClassName('auth_type__switcher');
var login_btn = document.getElementById('login-btn');
var reg_btn = document.getElementById('reg-btn');
var loginfield = document.getElementById('loginfield');
var namefield = document.getElementById('namefield');
var passfield = document.getElementById('passfield');
var passrepeatfield = document.getElementById('passrepeatfield');

var login_form = document.getElementById('login-form')
var reg_form = document.getElementById('reg-form')

var LogIn = true;

function AuthSwitchLogIn() {
    auth_switcher.item(0).style.backgroundColor = 'var(--color-blue-embient)';
    auth_switcher.item(1).style.backgroundColor = 'var(--color-first)';
    auth_switcher.item(1).style.color = 'var(--color-secondary)';
    auth_switcher.item(0).style.color = 'white';

    login_form.style.visibility='visible';
    login_form.style.height = '90%';

    reg_form.style.visibility='hidden';
    reg_form.style.height = '0';

    reg_btn.style.visibility = 'hidden';
    login_btn.style.opacity = 1;
    reg_btn.style.height = 0;
    reg_btn.style.opacity = 0;
    login_btn.style.height = 'calc(var(--index-scale) * 3)';

       LogIn = true;
}

function AuthSwitchReg() {
    auth_switcher.item(1).style.backgroundColor = 'var(--color-blue-embient)';
    auth_switcher.item(0).style.backgroundColor = 'var(--color-first)';
    auth_switcher.item(0).style.color = 'var(--color-secondary)';
    auth_switcher.item(1).style.color = 'white';

    login_form.style.visibility='hidden';
    login_form.style.height = '0';

    reg_form.style.visibility='visible';
    reg_form.style.height = '90%'

    reg_btn.style.visibility = 'visible';
    reg_btn.style.height = 'calc(var(--index-scale) * 3)';
    reg_btn.style.opacity = 1;
    login_btn.style.height = 0;
    login_btn.style.opacity = 0;
    LogIn = false;
}

AuthSwitchLogIn();