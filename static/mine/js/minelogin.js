$(function () {

    initSwiperMustbuy()

   $('.input_name').change(function () {

        var name = $(this).val();
        var url = 'http://127.0.0.1:8000/axf/checkloginname/';
        $.get(url,{'username':name},function (result) {
            $('#span_name').html(result.status);

        });
   });

});


function initSwiperMustbuy() {

    var swiper = new Swiper('#swiperMustbuy', {
        slidesPerView: 1,
        loop: true,
        autoplay: 2000,
    });
}







