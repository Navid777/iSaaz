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

$('#likes').click(function(){
            alert("here");
            var articleid;
            articleid = $(this).attr("data_artid");
             $.get('/like_article/', {article_id: articleid}, function(data){
                       $('#like_count').html(data);
                       $('#likes').hide();
                   });
        });


// Shahr lists
var shahrs = new Array();

shahrs['تهران'] = new Array('تهران','پرند');
shahrs['فارس'] = new Array('شیراز','آباده','فسا');
shahrs['مازندران'] = new Array('ساری','قائم شهر','رامسر');


// Mahalle lists
var mahales = new Array();

mahales['تهران'] = new Array();
mahales['تهران']['تهران']          = new Array('ونک','طرشت');
mahales['تهران']['پرند']          = new Array('شمال','جنوب');

mahales['فارس'] = new Array();
mahales['فارس']['شیراز'] = new Array('ستارخان','ارم');
mahales['فارس']['آباده']       = new Array('شمال','جنوب');
mahales['فارس']['فسا']         = new Array('شرق','غرب');

mahales['مازندران'] = new Array();
mahales['مازندران']['ساری'] = new Array('اینجا','اونجا');
mahales['مازندران']['قائم شهر']    = new Array('شمال','جنوب');
mahales['مازندران']['رامسر']   = new Array('شرق','غرب');


function setShahrs(x) {
  ostanSel = document.getElementById(x+'ostan');
  shahrList = shahrs[ostanSel.value];
  changeSelect(x+'shahr', shahrList, shahrList);
  setMahale(x);
}

function setMahale(x) {
  ostanSel = document.getElementById(x+'ostan');
  shahrSel = document.getElementById(x+'shahr');
  mahaleList = mahales[ostanSel.value][shahrSel.value];
  changeSelect(x+'mahale', mahaleList, mahaleList);
}

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

function changeSelect(fieldID, newOptions, newValues) {
  selectField = document.getElementById(fieldID);
  selectField.disabled = false;
  selectField.options.length = 0;
  for (i=0; i<newOptions.length; i++) {
    selectField.options[selectField.length] = new Option(newOptions[i], newValues[i]);
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


 ///////////////
 ///////////////
 /////saaaz/////
 ///////////////
 ///////////////
//cat1 = country
//cat2 = state
//cat3 = city
//cat4

//Cat2  lists
var cat2 = new Array();
cat2['سنتی'] = new Array('زهی','کوبه ای','بادی');
cat2['کلاسیک'] = new Array();



// Cat3 lists
var cat3 = new Array();

cat3['سنتی'] = new Array();
cat3['سنتی']['زهی']          = new Array('کمانه ای','زخمه ای','ضربه ای');
cat3['سنتی']['کوبه ای'] = new Array('ضربه ای');
cat3['سنتی']['بادی']          = new Array('باز','مجرایی');

var cat4 = new Array();

cat4['سنتی']= new Array();
cat4['سنتی']['زهی']          = new Array();
cat4['سنتی']['کوبه ای'] = new Array();
cat4['سنتی']['بادی']          = new Array();

cat4['سنتی']['زهی']['کمانه ای'] = new Array('کمانچه','رباب')

function setcat2(x) {
  cat1Sel = document.getElementById(x+'cat1');
  cat2List = cat2[cat1Sel.value];
  changeSelect(x+'cat2', cat2List, cat2List);
  setcat3(x);
}
function setcat3(x) {
  cat1Sel = document.getElementById(x+'cat1');
  cat2Sel = document.getElementById(x+'cat2');
  cat3List = cat3[cat1Sel.value][cat2Sel.value];
  changeSelect(x+'cat3', cat3List, cat3List);
  setcat4(x);
}
function setcat4() {
  cat1Sel = document.getElementById(x+'cat1');
  cat2Sel = document.getElementById(x+'cat2');
  cat3Sel = document.getElementById(x+'cat3');
  cat4List = cat4[cat1Sel.value][cat2Sel.value][cat3Sel.value];
  changeSelect(x+'cat4', cat4List, cat4List);
}

  $(function() {
    var instruments = [
      "گیتار",
      "پیانو",
      "سه تار",
      "تار",
      "فلوت",
      "نی",
      "آکاردئون",
      "ویولن",
      "کمانچه",
      "باران",
      "تنبک",
    ];
    $( "#saaz" ).autocomplete({
      source: instruments
    });
  });









function setCat2(x) {
  cat2List = cat2[document.querySelector('input[name="'+x+'sub1"]:checked').value];
  changeList(x+'sub2', 'setCat3("'+ x +'")', cat2List, cat2List);
  setCat3(x);
}

function setCat3(x) {
  cat3List = cat3[document.querySelector('input[name="'+x+'sub1"]:checked').value][document.querySelector('input[name="'+x+'sub2"]:checked').value];
  changeList(x+'sub3', 'setCat4("'+ x +'")', cat3List, cat3List);
  setCat4(x);
}

function setCat4(x) {
  cat4List = cat4[document.querySelector('input[name="'+x+'sub1"]:checked').value][document.querySelector('input[name="'+x+'sub2"]:checked').value][document.querySelector('input[name="'+x+'sub3"]:checked').value];
  changeList(x+'sub4', '' , cat4List, cat4List);
}

function changeList(fieldID, func, newOptions, newValues){
    var ul = document.getElementById(fieldID);
    nodes = ul.childNodes;
    for( i= nodes.length-1; i>1; i--){
        ul.removeChild(nodes[i]);
    }
    for (i=0; i<newOptions.length; i++) {
        li = document.createElement("li");
        li.innerHTML = "<a><i class='icon-cog'></i><input type='radio' onclick=" + func + " name='" + fieldID + "' value ='"  + newValues[i] + "'>" + newValues[i] + "</a>";
        ul.appendChild(li);
    }
}





