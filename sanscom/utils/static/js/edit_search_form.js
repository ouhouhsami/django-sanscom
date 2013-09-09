$(document).ready(function(){
	if(!$('#id_public').is(':checked')){
		$('.description').hide();
	}
	$('#id_public').change(function(evt){
		if($(this).is(':checked')){
			$('.description').show();
		}else {
			$('.description').hide();
		}
	});
});