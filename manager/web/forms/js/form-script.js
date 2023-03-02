// Event Listeners
$('.form-btn').on('click', function (e) {
    // var $which_form = $(this).attr('value'); // This to get the value of any atribute in html
    if ($(this).hasClass('bb-form1')) {
        $('.dff1').addClass('show');
    }
    else if ($(this).hasClass('bb-form2')) {
        $('.dff2').addClass('show');
    }
    else if ($(this).hasClass('bb-form3')) {
        $('.dff3').addClass('show');
    }
    else if ($(this).hasClass('bb-form4')) {
        $('.dff4').addClass('show');
    }
    else if ($(this).hasClass('bb-form5')) {
        $('.dff5').addClass('show');
    }
    else if ($(this).hasClass('bb-form6')) {
        $('.dff6').addClass('show');
    }
})

$('.close_bbtn').on('click', function (e) {
    if ($(this).hasClass('a-form1')) {
        $('.dff1').removeClass('show');
    }
    else if ($(this).hasClass('a-form2')) {
        $('.dff2').removeClass('show');
    }
    else if ($(this).hasClass('a-form3')) {
        $('.dff3').removeClass('show');
    }
    else if ($(this).hasClass('a-form4')) {
        $('.dff4').removeClass('show');
    }
    else if ($(this).hasClass('a-form5')) {
        $('.dff5').removeClass('show');
    }
    else if ($(this).hasClass('a-form6')) {
        $('.dff6').removeClass('show');
    }
})

$('.overlay').on('click', function () {
    $('.popup').removeClass('show');
})