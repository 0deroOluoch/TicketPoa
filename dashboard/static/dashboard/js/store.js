
$(document).ready(function(){


$('#add_ticket').click(function(){


	let type = $('#type').val();
	let quantity = $('#quantity').val();
	let price = $('#price').val();

	if (type != '' && quantity != '' && price != ''){
		$('#ticket-table').prepend(`<tr><td>${type}</td><td>${quantity}</td><td>${price}</td></tr>`);
		$('#ticket-form').prepend(`<input type="hidden" name="ticket" value="${type},${quantity},${price}">`)
		$('#type').val('');
		$('#quantity').val('');
		$('#price').val('');

	}

})

$('#save').click(function(){

	$('#ticket-form').submit();

})

});