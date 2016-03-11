(function($) {
    var loadedImages = 0,
        handler = $('#tiles li');
    var options = {
        autoResize: true,
        container: $('#main'),
        offset: 5,
        outerOffset: 10,
        itemWidth: 210
    };
    var curimg=''
    $('#tiles').imagesLoaded(function() {
        handler.wookmark(options);
    });

    $("button.dlbtn").bind("click", function(event) {
        event.stopPropagation();
    });
    $("button.delbtn").bind("click", function(event) {
        var fileName=$('p',this).attr('file');
        $.ajax({
            url:'/del/'+fileName,
            success:function(e){
                location.reload();
            }
        });
        event.stopPropagation();
    });
    $("button.sharebtn").bind("click", function(event) {
        $('#myModal').modal('toggle');
        curimg=$('p',this).attr('file');
        $.ajax({
            url:'/pic/'+curimg,
            data:{},
            success:function(data){
                if(data=='yes'){
                    setshareBtn(false);
                    $("#IVText").html('点击下方按钮停止分享');
                }
                else{
                    setshareBtn(true);
                    $("#IVText").html('点击下方按钮开始分享');

                }
            }
        });
        event.stopPropagation();
    });

    function setshareBtn(e){
        if(e){
            $("#stopshare").hide();
            $("#startshare").show();
        }else{
            $("#stopshare").show();
            $("#startshare").hide();
        }
    }

    $("#startshare").bind("click", function(event) {
        $.ajax({
            url:'/getIV/'+curimg,
            success:function(data){
                if(data==''){
                    $("#IVText").html('您没有权限查看！');
                }
                else if(data){
                    $("#IVText").html('提取码为   '+data);
                    setshareBtn(false);
                }
            }
        });
    });

    $("#stopshare").bind("click", function(event) {
        $.ajax({
            url:'/getIV/'+curimg,
            data:{},
            success:function(data){
                if(data==''){
                    $("#IVText").html('操作失败！');
                }
                else{
                    $("#IVText").html('已经关闭分享!');
                    setshareBtn(true);
                }
            }
        });
    });

    handler.click(function() {
        if ($(this).height() - $('img', this).height() < 2) {
            var newHeight = $('img', this).height() + 40;
            $('.pics').each(function () {
                var newHeight = $('img', this).height();
                $(this).css('height', newHeight + 'px');
                $('div', this).css('display','none');
            });
            $('div', this).css('display', '');
        }
        else {
            var newHeight = $('img', this).height();
            $('div', this).css('display', 'none');
        }
        $(this).css('height', newHeight + 'px');
        handler.wookmark(options);
    });
    $('input[id=lefile]').change(function() {
        $('#photoCover').val($(this).val());
    });
})(jQuery);