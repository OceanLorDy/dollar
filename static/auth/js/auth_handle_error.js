$(document).ready(function () {
    if ($('#auth_login_error').val() === 'True') {
        iziToast.error({
            position: 'topRight',
            // title: body['priority'],
            message: 'Kullanıcı adı veya şifre hatalı!'
        });
    }

    if ($('#auth_is_active_error').val() === 'True') {
        iziToast.error({
            position: 'topRight',
            // title: body['priority'],
            message: 'Kullanıcı Aktif Değil!'
        });
    }
});
