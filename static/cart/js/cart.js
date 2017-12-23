$(function () {
    var span_buy = $('#span_buy_button');

    span_buy.click(function () {

        var url = 'http://127.0.0.1:8000/axf/chageorderflag/';
        $.get(url);
        window.location.href = 'http://127.0.0.1:8000/axf/payment/';

    });

});