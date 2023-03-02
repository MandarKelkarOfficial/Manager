console.clear();

const loginBtn = document.getElementById('login');
const signupBtn = document.getElementById('signup');

loginBtn.addEventListener('click', (e) => {
    let parent = e.target.parentNode.parentNode;
    Array.from(e.target.parentNode.parentNode.classList).find((element) => {
        if (element !== "slide-up") {
            parent.classList.add('slide-up')
        } else {
            signupBtn.parentNode.classList.add('slide-up')
            parent.classList.remove('slide-up')
        }
    });
});

signupBtn.addEventListener('click', (e) => {
    let parent = e.target.parentNode;
    Array.from(e.target.parentNode.classList).find((element) => {
        if (element !== "slide-up") {
            parent.classList.add('slide-up')
        } else {
            loginBtn.parentNode.parentNode.classList.add('slide-up')
            parent.classList.remove('slide-up')
        }
    });
});

$('.submit-btn').on('click', function (e) {
    if ($(this).hasClass('signup-user')) {
        alert('Signup')
    }
    else if ($(this).hasClass('login-user')) {
        var name = $('.u-name-in').val();
        var pass = $('.u-pass-in').val();
        if (name == 'dnabb' && pass == '@dnabb07') {
            alert('Welcome master')
            location.replace('http://127.0.0.1:5503/manager/index.html#')
        }
        else {
            alert('Please enter valid password and u-name')
            return false;
        }
    }
})