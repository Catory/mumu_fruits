$(function () {
    if (document.cookie.length > 0){
        $('#p_login').hide();
        $('#p_regedit').hide();
    }
    else {
        $('#p_login').show();
        $('#p_regedit').show();
    }
});
