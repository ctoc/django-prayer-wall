$('#requestForm').submit(function( event ){
  console.log("test");
// Stop form from submitting normally
  event.preventDefault();
 
  // Get some values from elements on the page:
  var $form = $( this ),
    name = $form.find( "input[name='prayer-name']" ).val(),
    email = $form.find( "input[name='prayer-email']" ).val(),
    request = $form.find( "input[name='prayer-request']" ).val(),
    url = $form.attr( "new-request/" );
 

  // Send the data using post
  var posting = $.post( url, {'prayer_name': name, 'prayer_email': email, 'prayer_request': request});

  // Put the results in a div
  posting.done(function( data ) {  
    console.log("test1");
    var content = $( data ).find( "#content" );
    $( "#result" ).empty().append( content );
  });
});
