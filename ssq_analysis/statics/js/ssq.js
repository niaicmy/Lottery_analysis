let red_status = [];
// console.log(typeof red_status);
let blue_status = [];

// 和值的范围
let s_sum = 0;
let m_sum = 0;

// cookies 官网:  https://github.com/js-cookie/js-cookie
$(function () {

    my_loda();
    check_num(red_status, 'red');
    check_num(blue_status, 'blue');

    $("input[name='ssum']").blur(function () {
        // alert("ssum blur.")
        s_sum = parseInt($(this).val());
        if (s_sum < 22 || s_sum >= 199) {
            alert("输入值不在和值范围内.");
            // $(this).focus()
        }
        // console.log("ssum blur.")
        // console.log(typeof s_sum);
        // console.log(s_sum)
    });

    $("input[name='msum']").blur(function () {
        // alert("msum blur.")
        m_sum = parseInt($(this).val());
        if (m_sum < 22 || m_sum > 199) {
            alert("输入值不在和值范围内.");
            // $(this).focus()
        }
        // console.log("msum blur.")
        // console.log(typeof m_sum);
        // console.log(m_sum)
    });

});

// 加载页面事件处理数据
// $(window).on("load", function () {
//     let cook = Cookies.getJSON("num_cookies");
//     // alert(JSON.parse(cook))
//     // console.log(typeof cook);
//     // 第一次加载 cook 是无状态的,直接返回,下一次正常执行
//     if (cook === undefined) {
//         return
//     }
//
//     red_status = cook.red;
//     blue_status = cook.blue;
//     console.log("red_status is" + red_status);
//     console.log("blue_status is" + blue_status);
//
//     s_sum = cook.ssum;
//     m_sum = cook.msum;
//
//     // 判断 red_status blue_status 状态 决定是否重置
//     // 还原选择的状态
//     if (red_status === undefined) {
//         red_status = []
//     }
//     else {
//         $("input[name='red']").each(function () {
//             for (let i in red_status) {
//                 if ($(this).val() === red_status[i]) {
//                     $(this).prop("checked", true)
//                 }
//             }
//         })
//     }
//
//     if (blue_status === undefined) {
//         blue_status = []
//     } else {
//         $("input[name='blue']").each(function () {
//             for (let i in blue_status) {
//                 if ($(this).val() === blue_status[i]) {
//                     $(this).prop("checked", true)
//                 }
//             }
//         })
//     }
//
//     if (s_sum === undefined) {
//         s_sum = 0
//     }
//     else {
//         $("input[name='ssum']").val(s_sum)
//     }
//
//     if (m_sum === undefined) {
//         m_sum = 0
//     }
//     else {
//         $("input[name='msum']").val(m_sum)
//     }
//
//     // console.log(red_status);
//     // console.log(blue_status);
// });

function my_loda() {
    let cook = Cookies.getJSON("num_cookies");
    // alert(JSON.parse(cook))
    // console.log(typeof cook);
    // 第一次加载 cook 是无状态的,直接返回,下一次正常执行
    if (cook === undefined) {
        return
    }

    red_status = cook.red;
    blue_status = cook.blue;
    // console.log("red_status is " + red_status);
    // console.log("blue_status is " + blue_status);

    s_sum = cook.ssum;
    m_sum = cook.msum;

    // 判断 red_status blue_status 状态 决定是否重置
    // 还原选择的状态
    if (red_status === undefined) {
        red_status = []
    }
    else {
        $("input[name='red']").each(function () {
            for (let i in red_status) {
                if ($(this).val() === red_status[i]) {
                    $(this).prop("checked", true)
                }
            }
        })
    }

    if (blue_status === undefined) {
        blue_status = []
    } else {
        $("input[name='blue']").each(function () {
            for (let i in blue_status) {
                if ($(this).val() === blue_status[i]) {
                    $(this).prop("checked", true)
                }
            }
        })
    }

    if (s_sum === undefined) {
        s_sum = 0
    }
    else {
        $("input[name='ssum']").val(s_sum)
    }

    if (m_sum === undefined) {
        m_sum = 0
    }
    else {
        $("input[name='msum']").val(m_sum)
    }

    // console.log(red_status);
    // console.log(blue_status);
}


// 离开页面事件处理
$(window).on("beforeunload", function () {
    // console.log("beforeunload ...");
    // console.log(red_status);
    // console.log(blue_status);

    // 直接使用json 对象, 不用转换对象类型
    let num_cookies = {"red": red_status, "blue": blue_status, "ssum": s_sum, "msum": m_sum};
    // Cookies.set("num_cookies", num_cookies, {expires: 1});
    // Cookies.set("num_cookies", num_cookies, {expires: 2, domain: "127.0.0.1", path: '/'});
    Cookies.set("num_cookies", num_cookies, {expires: 2, domain: "", path: '/'});

    // window.sessionStorage.setItem("red", red_status);
    // window.sessionStorage.red = red_status;
    // window.sessionStorage.blue = blue_status;
    // return ' ';
});

// //数组转json串
// var arr = [1,2,3, { a : 1 } ];
// JSON.stringify( arr );
//
// //json字符串转数组
// var jsonStr = '[1,2,3,{"a":1}]';
// JSON.parse( jsonStr );
//
// // json字符串转化成json对象
// // jquery的方法
// var jsonObj = $.parseJSON(jsonStr)
// //js 的方法
// var jsonObj =  JSON.parse(jsonStr)
// json对象转化成json字符串
// //js方法
// var jsonStr1 = JSON.stringify(jsonObj)


// 进入页面事件处理
// function html_load() {
//     // 读取cookie 加载数据
//     // red_status = Cookies.get("red");
//     // blue_status = Cookies.get("blue");
//     red_status = window.sessionStorage.getItem("red");
//     blue_status = window.sessionStorage.getItem("blue");
//     alert(red_status);
//     alert(blue_status);
// }


// checkbox 状态设置
function check_num(check_status, who) {
    // console.log(check_status);
    $("input[name=who]".replace("who", who)).on("change", function () {
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

        // console.log(check_status)
        // alert(who +":" + check_status)
        // alert("checkbox click. ")
    });
}

// 给数组添加一个 remove 方法
Array.prototype.remove = function (val) {
    if (this.length <= 0 || this === undefined) {
        return false
    }
    else {
        // 删除一个点击存在的数据
        this.splice(this.indexOf(val), 1)
    }
};

function my_submit() {
    // 判断 数组长度是不是符合标准
    // alert(red_status);
    // alert(blue_status);
    if (red_status.length < 6 && blue_status.length < 1) {
        alert("数据长度出错! 请重新选择后提交...");
        return false
    }

    if (s_sum < 22 || s_sum > 199 || m_sum < 22 || m_sum > 199) {
        alert("和值输入错误 请重新输入后提交...");
        return false
    }
}

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