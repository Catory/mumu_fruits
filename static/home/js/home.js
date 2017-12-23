$(function () {
    initSwiperWheel();
    initSwiperMustbuy();
});
function initSwiperWheel() {

var swiper = new Swiper('#topNav', {
    pagination: '.swiper-pagination',
    paginationClickable: true,
    spaceBetween: 30,
    centeredSlides: true,
    autoplay: 2000,
    loop:true,
        });
}
function initSwiperMustbuy() {

var swiper = new Swiper('#swiperMustbuy', {
    slidesPerView: 3,
    loop:true,
        });
}



