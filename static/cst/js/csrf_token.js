//   {#添加这个防止被csrf注入伪造#}
$.ajaxSetup({
    data: {csrfmiddlewaretoken: '{% csrf_token %}'},
});
