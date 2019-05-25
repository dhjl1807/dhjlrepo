var delay = 60
        var interval_id = 0

        function getCode(btn) {
            if(delay != 60) return

            phonenum = $('#phonenum').val()
            url = '/myapp/code/?phonenum=' + phonenum
            $.getJSON(url, function (data) {
                if (data.code == 200) {
                    $(btn).removeClass('btn-info')
                    $(btn).addClass('disabled')
                    interval_id = setInterval(function () {
                        btn.innerHTML = delay + '秒'
                        delay--
                        if (delay == 0) {
                            clearInterval(interval_id)
                            $(btn).removeClass('disabled')
                            $(btn).addClass('btn-info')
                            delay = 60;
                             btn.innerHTML = '验证码'
                        }
                    }, 1000)
                }
                else if (data.code !== 200){
                    alert(data.data)
                }
            })

        }