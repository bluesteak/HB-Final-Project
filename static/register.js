(function(){
	$('button').click(function(){
		var user = $('#email').val();
		var pass = $('#password').val();
		$.ajax({
			url: '/signup',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});


