// $('.side .sidebar').on('click', function () {
//     $('.edaf').toggleClass('fade');
// })



// window.onclick = function (event) {
//     if (event.target == $('.side')) {
//         alert("Aai")
//         $('.sidebar').removeClass('mobile');
//         $('.container').removeClass('fade');
//     }
// }
// Change content

$('li').on('click', function () {

    var $to_who = $(this).attr('value');

    if ($to_who == "d-table") {
        if ($('.col-13').hasClass('show_data')) {
            $('.col-15').removeClass('show_data')
            $('.col-14').removeClass('show_data')
            $('.col-17').removeClass('show_data')
            $('.col-13').removeClass('show_data')
            $('.col-16').removeClass('show_data')
            $('.col-12').removeClass('show_data')
        }
        else {
            $('.col-14').removeClass('show_data')
            $('.col-17').removeClass('show_data')
            $('.col-15').removeClass('show_data')
            $('.col-12').removeClass('show_data')
            $('.col-16').removeClass('show_data')
            $('.col-13').addClass('show_data')
        }
        var spin = $('.fa-gear').css("animation-name")
        if (spin == "spin") {
            $('.fa-gear').css("animation-name", "")
        }
    }
    else if ($to_who == "o-table") {
        if ($('.col-12').hasClass('show_data')) {
            $('.col-14').removeClass('show_data')
            $('.col-17').removeClass('show_data')
            $('.col-13').removeClass('show_data')
            $('.col-12').removeClass('show_data')
            $('.col-16').removeClass('show_data')
            $('.col-15').removeClass('show_data')
        }
        else {
            $('.col-14').removeClass('show_data')
            $('.col-13').removeClass('show_data')
            $('.col-15').removeClass('show_data')
            $('.col-17').removeClass('show_data')
            $('.col-16').removeClass('show_data')
            $('.col-12').addClass('show_data')
        }
        var spin = $('.fa-gear').css("animation-name")
        if (spin == "spin") {
            $('.fa-gear').css("animation-name", "")
        }
    }
    else if ($to_who == "pop-up") {

        if ($('.col-15').hasClass('show_data')) {

            $('.col-14').removeClass('show_data')
            $('.col-13').removeClass('show_data')
            $('.col-12').removeClass('show_data')
            $('.col-17').removeClass('show_data')
            $('.col-16').removeClass('show_data')
            $('.col-15').removeClass('show_data')
        }
        else {

            $('.col-14').removeClass('show_data')
            $('.col-17').removeClass('show_data')
            $('.col-13').removeClass('show_data')
            $('.col-16').removeClass('show_data')
            $('.col-12').removeClass('show_data')
            $('.col-15').addClass('show_data')
        }

        var spin = $('.fa-gear').css("animation-name")
        if (spin == "spin") {
            $('.fa-gear').css("animation-name", "")
        }
    }

    else if ($to_who == "setting-") {

        if ($('.col-14').hasClass('show_data')) {
            $('.col-14').removeClass('show_data')
            $('.col-15').removeClass('show_data')
            $('.col-13').removeClass('show_data')
            $('.col-17').removeClass('show_data')
            $('.col-16').removeClass('show_data')
            $('.col-12').removeClass('show_data')
        }
        else {
            $('.col-13').removeClass('show_data')
            $('.col-15').removeClass('show_data')
            $('.col-17').removeClass('show_data')
            $('.col-12').removeClass('show_data')
            $('.col-16').removeClass('show_data')
            $('.col-14').addClass('show_data')
        }

        var spin = $('.fa-gear').css("animation-name")
        if (spin == "spin") {
            $('.fa-gear').css("animation-name", "")
        }
        else {
            $('.fa-gear').css("animation-name", "spin")
        }
    }

    else if ($to_who == "contact-bb") {

        if ($('.col-16').hasClass('show_data')) {
            $('.col-16').removeClass('show_data')
            $('.col-14').removeClass('show_data')
            $('.col-13').removeClass('show_data')
            $('.col-12').removeClass('show_data')
            $('.col-17').removeClass('show_data')
            $('.col-15').removeClass('show_data')
        }
        else {
            $('.col-14').removeClass('show_data')
            $('.col-13').removeClass('show_data')
            $('.col-12').removeClass('show_data')
            $('.col-15').removeClass('show_data')
            $('.col-17').removeClass('show_data')
            $('.col-16').addClass('show_data')
        }

        var spin = $('.fa-gear').css("animation-name")
        if (spin == "spin") {
            $('.fa-gear').css("animation-name", "")
        }
    }
    else if ($to_who == "e-leaving-form") {

        if ($('.col-17').hasClass('show_data')) {
            $('.col-17').removeClass('show_data')
            $('.col-14').removeClass('show_data')
            $('.col-15').removeClass('show_data')
            $('.col-13').removeClass('show_data')
            $('.col-16').removeClass('show_data')
            $('.col-12').removeClass('show_data')
        }
        else {
            $('.col-13').removeClass('show_data')
            $('.col-15').removeClass('show_data')
            $('.col-12').removeClass('show_data')
            $('.col-16').removeClass('show_data')
            $('.col-14').removeClass('show_data')
            $('.col-17').addClass('show_data')
        }

        var spin = $('.fa-gear').css("animation-name")
        if (spin == "spin") {
            $('.fa-gear').css("animation-name", "")
        }
    }



    if ($('.col-13').hasClass('show_data')) {

        $('.overview-boxes').addClass('hide_me')
        $('.sales-boxes').addClass('hide_me')
        $('.container').addClass('handel_this')
    }
    else if ($('.col-12').hasClass('show_data')) {

        $('.overview-boxes').addClass('hide_me')
        $('.sales-boxes').addClass('hide_me')
        $('.container').removeClass('handel_this')
    }
    else if ($('.col-14').hasClass('show_data')) {

        $('.overview-boxes').addClass('hide_me')
        $('.sales-boxes').addClass('hide_me')
        $('.container').removeClass('handel_this')
    }
    else if ($('.col-15').hasClass('show_data')) {

        $('.overview-boxes').addClass('hide_me')
        $('.sales-boxes').addClass('hide_me')
        $('.container').removeClass('handel_this')
    }
    else if ($('.col-16').hasClass('show_data')) {

        $('.overview-boxes').addClass('hide_me')
        $('.sales-boxes').addClass('hide_me')
        $('.container').removeClass('handel_this')
    }
    else if ($('.col-17').hasClass('show_data')) {

        $('.overview-boxes').addClass('hide_me')
        $('.sales-boxes').addClass('hide_me')
        $('.container').removeClass('handel_this')
    }
    else {
        $('.overview-boxes').removeClass('hide_me')
        $('.sales-boxes').removeClass('hide_me')
        // $('.col-12').removeClass('hide_me')
        $('.container').removeClass('handel_this')
    }
});


/* Storing user's device details in a variable*/
let details = navigator.userAgent;

/* Creating a regular expression
containing some mobile devices keywords
to search it in details string*/
let regexp = /android|iphone|kindle|ipad/i;

/* Using test() method to search regexp in details
it returns boolean value*/
let isMobileDevice = regexp.test(details);

if (isMobileDevice) {
    $('.home-section').addClass('it_is_mobile')
    $('.sidebar').addClass('it_is_mobile')

} else {
    $('.home-section').removeClass('it_is_mobile')
}
$('.sidebarBtn').on('click', function () {
    if ($('.sidebar').hasClass('it_is_mobile')) {
        $('.overlay').addClass('my-overlay')
    }
    if ($('.sidebar').hasClass('active')) {
        $('.overlay').removeClass('my-overlay')
    }
})

function RemoveClass() {
    if ($('.serve-user').hasClass('unwrap-plate')) {
        $('.serve-user').hasClass('unwrap-plate')
        if ($('.serve-user').hasClass('unwrap-plate')) {
            $('.serve-user').removeClass('unwrap-plate')
        }
        if (!$('.serve-user').hasClass('unwrap-plate')) {
            $('.overlay').removeClass('my-overlay')
        }
        // $('.overlay').toggleClass('my-overlay')
        // if ($('.overlay').hasClass('my-overlay')) {
        //     $('.overlay').removeClass('my-overlay')
        // }
        // else {

        // }
    }
}
$('.bx-dots-vertical-rounded').on('click', function () {
    $('.serve-user').toggleClass('unwrap-plate')
    // $('.overlay').toggleClass('my-overlay')
    if ($('.overlay').hasClass('my-overlay')) {
        $('.overlay').addClass('my-overlay')
    }
    // else if ($('.serve-user').hasClass('unwrap-plate')) {
    //     $('.overlay').addClass('my-overlay')
    //     alert('God')
    // }
    if ($('.serve-user').hasClass('unwrap-plate')) {
        $('.overlay').addClass('my-overlay')
    }
    if (!$('.serve-user').hasClass('unwrap-plate')) {
        $('.overlay').removeClass('my-overlay')
    }

    setTimeout(RemoveClass, 3000);
})
$('.link-bb').on('click', function () {
    $('.serve-user').toggleClass('unwrap-plate')
    $('.overlay').removeClass('my-overlay')
})



$('.here-box').on('click', function (e) {
    if ($(this).hasClass('light-dark-mode')) {
        $('.sidebar').toggleClass('darker');
    }
    // else if ($(this).hasClass('a-form2')) {
    //     $('.dff2').removeClass('show');
    // }
    // else if ($(this).hasClass('a-form3')) {
    //     $('.dff3').removeClass('show');
    // }
    // else if ($(this).hasClass('a-form4')) {
    //     $('.dff4').removeClass('show');
    // }
})
$('.log_out').on('click', function (e) {
    var ye_n = confirm('Are you sure?')
    if (ye_n == true) {
        window.location.replace('http://127.0.0.1:5503/manager/login/loginfom.html')
    }
})

$('#mobile-num').on('input', function (e) {
    var x = e.target.value.replace(/\D/g, '').match(/(\d{0,3})(\d{0,3})(\d{0,4})/);
    e.target.value = !x[2] ? x[1] : '(' + x[1] + ') ' + x[2] + (x[3] ? '-' + x[3] : '');
});


$('#enroll-number').on('input', function (e) {
    var x = e.target.value.replace(/\D/g, '').match(/(\d{0,3})(\d{0,3})(\d{0,4})/);
    e.target.value = !x[2] ? x[1] : x[1] + ' ' + x[2] + (x[3] ? ' ' + x[3] : '');
});


$('#mobile-num-2').on('input', function (e) {
    var x = e.target.value.replace(/\D/g, '').match(/(\d{0,3})(\d{0,3})(\d{0,4})/);
    e.target.value = !x[2] ? x[1] : x[1] + ' ' + x[2] + (x[3] ? ' ' + x[3] : '');
});


$('#enroll-number-2').on('input', function (e) {
    var x = e.target.value.replace(/\D/g, '').match(/(\d{0,3})(\d{0,3})(\d{0,4})/);
    e.target.value = !x[2] ? x[1] : x[1] + ' ' + x[2] + (x[3] ? ' ' + x[3] : '');
});
$('#post-number-2').on('input', function (e) {
    var x = e.target.value.replace(/\D/g, '').match(/(\d{0,3})(\d{0,3})/);
    e.target.value = !x[2] ? x[1] : x[1] + ' ' + x[2] + (x[3] ? ' ' + x[3] : '');
});

const authorize = $('.authorize')

$('#regenerating').on('change', function () {
    if ($(this).is(":checked")) {
        $('#re-autho').addClass('authorize')
        $("#leaving-submit").prop("disabled", true);
    }
})
$('.autho-close-button').on('click', function () {
    if ($('#re-by-m').val() == 're@1025') {
        $('#re-by-m').val("")
        $('#re-autho').removeClass('authorize')
        leavingError.removeClass('error-translateY')
        $("#leaving-submit").prop("disabled", false);
    }
    else {
        $('#re-by-m').text("")
        $('#re-autho').removeClass('authorize')
        $("#regenerating").prop("checked", false);
        $("#leaving-submit").prop("disabled", true);
    }
})

$(document).ready(function () {
    const usernameInput = $('#enroll-number-2');
    const usernameError = $('#username-error');

    usernameInput.on('input', async () => {
        const username = usernameInput.val();
        if (!username) {
            usernameError.html('Username is required');
        } else {
            const response = await fetch(`/check-username/${username}`);
            const data = await response.json();
            if (data.exists) {
                // alert('God 1')
                // usernameError.html('Already exists');
                usernameError.addClass('error-translateY')
            } else {
                usernameError.removeClass('error-translateY')
                // usernameError.html('');
            }
        }
    });

    const enrollInput = $('#enroll-number');
    const leavingError = $('#enroll-error');
    enrollInput.on('input', async () => {
        const enroll = enrollInput.val();
        if (!enroll) {
            leavingError.html('Username is required');
        } else {
            const response = await fetch(`/check-enroll/${enroll}`);
            const data = await response.json();
            if (data.exists) {
                // alert('God 1')
                // usernameError.html('Already exists');
                leavingError.addClass('error-translateY')
                $("#leaving-submit").prop("disabled", true);
            } else {
                leavingError.removeClass('error-translateY')
                $("#leaving-submit").prop("disabled", false);
                // usernameError.html('');
            }
        }
    });
});
