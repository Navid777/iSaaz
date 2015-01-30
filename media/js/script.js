
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




    $(document).mouseup(function (e)
    {

        var login = $("#loginForm");
        var offer = $("#offerForm");
        if (!login.is(e.target)&& login.has(e.target).length === 0)
        {
            login.hide();
            $("#black_cover").hide();
        }
        if (!offer.is(e.target)&& offer.has(e.target).length === 0)
        {
            offer.hide();

        }
    });

    $("#is_offer").change(function() {
        if(this.checked) {
            $("#price_input").prop('disabled', false);
        }
    });

});





function popUpLoginSell(){
    document.getElementById('black_cover_sell').style.display = 'block';
    document.getElementById('loginFormSell').style.display = 'block';
}

function popUpLogin(){
    document.getElementById('black_cover').style.display = 'block';
    document.getElementById('loginForm').style.display = 'block';
}

function display(id){
    if(id == 'login'){
        document.getElementById('login').style.display = 'block';
        document.getElementById('register').style.display = 'none';
        }
    else{
        document.getElementById('login').style.display = 'none';
        document.getElementById('register').style.display = 'block';
        }
}


function popUp(url) {
    new_window=window.open(url,'ورود','height=200,width=150');
    if (window.focus) {new_window.focus()}
    return false;
}

function addLoadEvent(func) {
  var oldonload = window.onload;
  if (typeof window.onload != 'function') {
    window.onload = func;
  } else {
    window.onload = function() {
      if (oldonload) {
        oldonload();
      }
      func();
    }
  }
}



addLoadEvent(function() {
});





