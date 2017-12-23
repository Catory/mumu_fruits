$(function () {
    $('.img_sub').hide();
    $('.span_goods_num').hide();

    $('.img_add').click(function () {
        $(this).parent().find('img').show();
        $(this).parent().find('span').show();
        var goods_num = $(this).parent().find('span').eq(0).text();
        goods_num = parseInt(goods_num)+1;
        $(this).parent().find('span').html(goods_num);
        $('.span_goods_sum').show();
        goods_sum = parseInt($('.span_goods_sum').text());
        goods_sum++;
        // $.cookie('goods_sum',goods_sum);
        $('.span_goods_sum').html(goods_sum);

        productid = this.getAttribute('ga');
        var url = 'http://127.0.0.1:8000/axf/carthandle/0/';
        $.get(url,{'productid':productid},function (result) {
            if(result.status === 'usernone'){
                window.location.href = "http://127.0.0.1:8000/axf/loadlogin/"
            }
        });

    });
    $('.img_sub').click(function () {
        var goods_num = $(this).parent().find('span').eq(0).text();
        goods_num = parseInt(goods_num)-1;
        if(goods_num===0){
            $(this).hide();
            $(this).parent().find('span').hide();
        }
        $(this).parent().find('span').html(goods_num);
        // var goods_sum = parseInt($('.span_goods_sum').text());
        goods_sum--;
        // $.cookie('goods_sum',goods_sum);
        $('.span_goods_sum').html(goods_sum);

        productid = this.getAttribute('ga');
        var url = 'http://127.0.0.1:8000/axf/carthandle/1/';
        $.get(url,{'productid':productid});

        if(goods_sum===0){
            $('.span_goods_sum').hide();
        }
    });


});