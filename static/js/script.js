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
    else if ($to_who == "my-home") {

        if ($('.col-12').hasClass('show_data') || $('.col-13').hasClass('show_data') || $('.col-17').hasClass('show_data') || $('.col-14').hasClass('show_data') || $('.col-16').hasClass('show_data')) {

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
            $('.col-12').removeClass('show_data')
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
$('#pro_settings').on('click', function (e) {
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
})

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

})
$('.log_out').on('click', function (e) {
    var ye_n = confirm('Are you sure?')
    if (ye_n == true) {
        window.location.replace('/login')
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
    else {
        $("#leaving-submit").prop("disabled", false);
    }
})
$('.autho-close-button').on('click', function () {
    const leavingError = $('#enroll-error');
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
        if (username.length > 11) {
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
        }
    });

    const enrollInput = $('#enroll-number');
    const leavingError = $('#enroll-error');
    enrollInput.on('input', async () => {
        const enroll = enrollInput.val();
        if (enroll.length > 11) {
            if (!enroll) {
                leavingError.html('Username is required');
            } else {
                const response = await fetch(`/check-enroll/${enroll}`);
                const data = await response.json();
                if (data.exists) {
                    // alert('God 1')
                    // usernameError.html('Already exists');
                    leavingError.addClass('error-translateY')
                    $("#regenerating").prop("checked", false);
                    $("#leaving-submit").prop("disabled", true);
                } else {
                    leavingError.removeClass('error-translateY')
                    $("#leaving-submit").prop("disabled", false);
                    $("#regenerating").prop("checked", false);
                    // usernameError.html('');
                }
            }
        }
    });
});

let currentDate = dayjs();
let daysInMonth = dayjs().daysInMonth();
let firstDayPosition = dayjs().startOf("month").day();
let monthNames = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
];
let weekNames = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];
let dateElement = document.querySelector("#calendar .calendar-dates");
let calendarTitle = document.querySelector(".calendar-title-text");
let nextMonthButton = document.querySelector("#nextMonth");
let prevMonthButton = document.querySelector("#prevMonth");
let dayNamesElement = document.querySelector(".calendar-day-name");
let todayButton = document.querySelector("#today");
let dateItems = null;
let newMonth = null;

weekNames.forEach(function (item) {
    dayNamesElement.innerHTML += `<div>${item}</div>`;
});

function plotDays() {
    let count = 1;
    dateElement.innerHTML = "";

    let prevMonthLastDate = currentDate.subtract(1, "month").endOf("month").$D;
    let prevMonthDateArray = [];

    //plot prev month array
    for (let p = 1; p < firstDayPosition; p++) {
        prevMonthDateArray.push(prevMonthLastDate--);
    }
    prevMonthDateArray.reverse().forEach(function (day) {
        dateElement.innerHTML += `<button class="calendar-dates-day-empty">${day}</button>`;
    });

    //plot current month dates
    for (let i = 0; i < daysInMonth; i++) {
        dateElement.innerHTML += `<button class="calendar-dates-day">${count++}</button>`;
    }

    //next month dates
    let diff =
        42 - Number(document.querySelector(".calendar-dates").children.length);
    let nextMonthDates = 1;
    for (let d = 0; d < diff; d++) {
        document.querySelector(
            ".calendar-dates"
        ).innerHTML += `<button class="calendar-dates-day-empty">${nextMonthDates++}</button>`;
    }

    //month name and year
    calendarTitle.innerHTML = `${monthNames[currentDate.month()]
        } - ${currentDate.year()}`;
}

//highlight current date
function highlightCurrentDate() {
    dateItems = document.querySelectorAll(".calendar-dates-day");
    if (dateElement && dateItems[currentDate.$D - 1]) {
        dateItems[currentDate.$D - 1].classList.add("today-date");
    }
}

//next month button event
nextMonthButton.addEventListener("click", function () {
    newMonth = currentDate.add(1, "month").startOf("month");
    setSelectedMonth();
});

//prev month button event
prevMonthButton.addEventListener("click", function () {
    newMonth = currentDate.subtract(1, "month").startOf("month");
    setSelectedMonth();
});

//today button event
todayButton.addEventListener("click", function () {
    newMonth = dayjs();
    setSelectedMonth();
    setTimeout(function () {
        highlightCurrentDate();
    }, 50);
});

//set next and prev month
function setSelectedMonth() {
    daysInMonth = newMonth.daysInMonth();
    firstDayPosition = newMonth.startOf("month").day();
    currentDate = newMonth;
    plotDays();
}

//init
plotDays();
setTimeout(function () {
    highlightCurrentDate();
}, 50);

// <input type='radio' value='show' name='shower'>