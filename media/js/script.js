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


function setShahrs() {
  ostanSel = document.getElementById('ostan');
  shahrList = shahrs[ostanSel.value];
  changeSelect('shahr', shahrList, shahrList);
  setMahale();
}

function setMahale() {
  ostanSel = document.getElementById('ostan');
  shahrSel = document.getElementById('shahr');
  mahaleList = mahales[ostanSel.value][shahrSel.value];
  changeSelect('mahale', mahaleList, mahaleList);
}

function changeSelect(fieldID, newOptions, newValues) {
  selectField = document.getElementById(fieldID);
  selectField.disabled = false;
  selectField.options.length = 0;
  for (i=0; i<newOptions.length; i++) {
    selectField.options[selectField.length] = new Option(newOptions[i], newValues[i]);
  }
}

function popitup(url) {
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

window.onload = function() {
    placeDivs();
    }


addLoadEvent(function() {
  setShahrs();
});
addLoadEvent(function() {
  placeDivs();
});


function placeDivs(){
    cont = document.getElementById('ad_container');
    divs = cont.childNodes;
    for(i = 0; i<divs.length ; i++){
    if (i % 3 == 0){
        divs[i].style.left = "0px";
    }else if (i % 3 == 2){
        divs[i].style.right = "0px";
    }
    }


}

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

function setcat2() {
  cat1Sel = document.getElementById('cat1');
  cat2List = cat2[cat1Sel.value];
  changeSelect('cat2', cat2List, cat2List);
  setMahale();
}
function setcat3() {
  cat1Sel = document.getElementById('cat1');
  cat2Sel = document.getElementById('cat2');
  cat3List = cat3[cat1Sel.value][cat2Sel.value];
  changeSelect('cat3', cat3List, cat3List);
}
function setcat4() {
  cat1Sel = document.getElementById('cat1');
  cat2Sel = document.getElementById('cat2');
  cat3Sel = document.getElementById('cat3');
  cat4List = cat4[cat1Sel.value][cat2Sel.value][cat3Sel.value];
  changeSelect('cat4', cat4List, cat4List);
}











function setCat2() {
  cat2List = cat2[document.querySelector('input[name="sub1"]:checked').value];
  changeList('sub2', 'setCat3()', cat2List, cat2List);
}

function setCat3() {
  cat3List = cat3[document.querySelector('input[name="sub1"]:checked').value][document.querySelector('input[name="sub2"]:checked').value];
  changeList('sub3', 'setCat4()', cat3List, cat3List);
}

function setCat4() {
  cat4List = cat4[document.querySelector('input[name="sub1"]:checked').value][document.querySelector('input[name="sub2"]:checked').value][document.querySelector('input[name="sub3"]:checked').value];
  changeList('sub4', '' , cat4List, cat4List);
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





