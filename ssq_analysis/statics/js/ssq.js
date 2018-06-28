$(function () {
    // alert("ssq.html js is ok !");
    $("#pagination>li").on("click", function () {
        alert("click li");
    })
});
/*
// 分页插件： http://www.php.cn/js-tutorial-348268.html
function f1() {
    // 后台分页：发送多次ajax，每次获取指定页数的数据（万条数据以上）
    $('#id').bootstrapPaginator({
        bootstrapMajorVersion: 3,//bootstrap版本
        currentPage: 1,//当前页码
        totalPages: data.cn,//总页数（后台传过来的数据）
        numberOfPages: 5,//一页显示几个按钮
        itemTexts: function (type, page, current) {
            switch (type) {
                case "first":
                    return "首页";
                case "prev":
                    return "上一页";
                case "next":
                    return "下一页";
                case "last":
                    return "末页";
                case "page":
                    return page;
            }
        },//改写分页按钮字样
        onPageClicked: function (event, originalEvent, type, page) {
            $.ajax({
                url: '../../interface/xw_zxdt_list.php',
                type: 'post',
                data: {page: page},
                dataType: 'json',
                success: function (data) {
                    tplData(data);//处理成功返回的数据
                }
            });
        }
    });
}

function f2() {
    // 前台分页：ajax一次请求获取全部数据，适合少量数据（万条数据以下）
    $.ajax({
        type: "GET",
        url: "",//后台接口地址
        dataType: "json",
        success: function (msg) {
            let pages = Math.ceil(msg.data / 5);//data是数据总量
            let element = $('#id');//对应ul的id
            element.bootstrapPaginator({
                bootstrapMajorVersion: 3,//bootstrap版本
                currentPage: page,//当前页面
                numberOfPages: 5,//一页显示几个按钮（在ul里面生成5个li）
                totalPages: pages //总页数
            });
        }
    });
}
*/