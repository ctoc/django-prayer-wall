$('#submit').click(function(){
    var name;
    var email;
    var request;
    name = $(this).attr("data-name");
    email = $(this).attr("data-email");
    request = $(this).attr("data-request");
    $.post('/new-request/', {prayer_name: name, prayer_email: email, prayer_request: request});
});