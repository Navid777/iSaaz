$(document).ready(function(){
	$(".carousel").carousel();
	$('.carousel').carousel({
		auto: true,
		period: 3000,
		duration: 2000,
		markers: {
			type: "square"
		}
	});	
});
