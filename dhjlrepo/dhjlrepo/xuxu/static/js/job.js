

function func(btn) {
     var info = $("input[name='info']").val();
     if (info == null || info == ''){
         alert('请输入查询信息');
         return false;
     }else{
         return true;
     }
}

function func1(btn) {
    alert('请输选择查找网站');
    return false;
}