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
        $('.container').addClass('handel_this')
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


function RemoveClass() {
    if ($('.serve-user').hasClass('unwrap-plate')) {
        $('.serve-user').toggleClass('unwrap-plate')
    }
}
$('.bx-dots-vertical-rounded').on('click', function () {
    $('.serve-user').toggleClass('unwrap-plate')
    setTimeout(RemoveClass, 3000);
})
$('.link-bb').on('click', function () {
    $('.serve-user').toggleClass('unwrap-plate')
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

document.getElementById('mobile-num').addEventListener('input', function (e) {
    var x = e.target.value.replace(/\D/g, '').match(/(\d{0,3})(\d{0,3})(\d{0,4})/);
    e.target.value = !x[2] ? x[1] : '(' + x[1] + ') ' + x[2] + (x[3] ? '-' + x[3] : '');
});
document.getElementById('enroll-number').addEventListener('input', function (e) {
    var x = e.target.value.replace(/\D/g, '').match(/(\d{0,3})(\d{0,3})(\d{0,4})/);
    e.target.value = !x[2] ? x[1] : x[1] + ' ' + x[2] + (x[3] ? ' ' + x[3] : '');
});

