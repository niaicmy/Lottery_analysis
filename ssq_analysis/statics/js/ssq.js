let red_status = [];
let blue_status = [];

$(function () {
    // alert("ssq.html js is ok !");
    // $("#pagination>li").on("click", function () {
    //     // alert("click li");
    // });

    html_load();
    check_num(red_status, 'red');
    check_num(blue_status, 'blue');

    // 离开页面事件处理
    // todo: 离开页面事件没作用
    $(window).unload(function () {
        // Cookies.set("red", red_status);
        // Cookies.set("blue", blue_status);
        // window.sessionStorage.setItem("red", red_status);
        window.sessionStorage.red = red_status;
        window.sessionStorage.blue = blue_status;
    });

});

// 进入页面事件处理
function html_load() {
    // 读取cookie 加载数据
    // red_status = Cookies.get("red");
    // blue_status = Cookies.get("blue");
    red_status = window.sessionStorage.getItem("red");
    blue_status = window.sessionStorage.getItem("blue");
    alert(red_status);
    alert(blue_status);
}


// checkbox 状态设置
function check_num(check_status, who) {
    $("input[name= who]".replace("who", who)).on("change", function () {
        // alert($(this).val());
        // alert(check_status);
        // alert($.inArray($(this).val(), check_status));
        if ($.inArray($(this).val(), check_status) < 0) {
            // alert($(this).val());
            check_status.push($(this).val());
            // alert("in push");
            // alert(check_status)
        }
        else {
            check_status.remove($(this).val());
            // alert("in remove");
            // alert(check_status)
        }
        // alert(who +":" + check_status)
        // alert("checkbox click. ")
    });
}

Array.prototype.remove = function (val) {
    if (this.length <= 0 || this === undefined) {
        return false
    }
    else {
        // 删除一个点击存在的数据
        this.splice(this.indexOf(val), 1)
    }
};

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

// function initTableCheckbox() {
//
//     var $thr = $('table thead tr');
//
//     var $checkAllTh = $('<th><input type="checkbox" id="checkAll" name="checkAll" /></th>');
//
//     /*将全选/反选复选框添加到表头最前，即增加一列*/
//
//     $thr.prepend($checkAllTh);
//
//     /*“全选/反选”复选框*/
//
//     var $checkAll = $thr.find('input');
//
//     $checkAll.click(function (event) {
//
//         /*将所有行的选中状态设成全选框的选中状态*/
//
//         $tbr.find('input').prop('checked', $(this).prop('checked'));
//
//         /*并调整所有选中行的CSS样式*/
//
//         if ($(this).prop('checked')) {
//
//             $tbr.find('input').parent().parent().addClass('warning');
//
//         } else {
//
//             $tbr.find('input').parent().parent().removeClass('warning');
//
//         }
//
//         /*阻止向上冒泡，以防再次触发点击操作*/
//
//         event.stopPropagation();
//
//     });
//
//     /*点击全选框所在单元格时也触发全选框的点击操作*/
//
//     $checkAllTh.click(function () {
//
//         $(this).find('input').click();
//
//     });
//
//     var $tbr = $('table tbody tr');
//
//     var $checkItemTd = $('<td><input type="checkbox" name="checkItem" /></td>');
//
//     /*每一行都在最前面插入一个选中复选框的单元格*/
//
//     $tbr.prepend($checkItemTd);
//
//     /*点击每一行的选中复选框时*/
//
//     $tbr.find('input').click(function (event) {
//
//         /*调整选中行的CSS样式*/
//
//         $(this).parent().parent().toggleClass('warning');
//
//         /*如果已经被选中行的行数等于表格的数据行数，将全选框设为选中状态，否则设为未选中状态*/
//
//         $checkAll.prop('checked', $tbr.find('input:checked').length == $tbr.length ? true : false);
//
//         /*阻止向上冒泡，以防再次触发点击操作*/
//
//         event.stopPropagation();
//
//     });
//
//     /*点击每一行时也触发该行的选中操作*/
//
//     $tbr.click(function () {
//
//         $(this).find('input').click();
//
//     });
// }