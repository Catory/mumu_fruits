
onload = function () {
    setTimeout("window.location=('/axf/mine/')",2000);
    initSwiperMustbuy()
};

function initSwiperMustbuy() {

    var swiper = new Swiper('#swiperMustbuy', {
        slidesPerView: 1,
        loop: true,
        autoplay: 2000
    });
}
