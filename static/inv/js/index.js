

$(document).ready( function () {

 $('table').DataTable( {
   "dom": '<"row m-1" <"col-md-12" B>><"row m-1" <"col-md-4 pt-2" l><"col-md-4 pb-2" i><"col-md-4 pt-2" f>><t>p',
   "buttons": [
      {extend: 'excel',
      exportOptions: {header: 'true',}
      },
      'csv',
      {extend: 'print',
      exportOptions: {header: 'true',}
      },
      {extend: 'pdf',
      exportOptions: {header: true,}
    }
    ],
   "lengthMenu": [ [10, 25, 50, -1], [10, 25, 50, "All"] ],
   "order": []
} );

} );

$("li.kw").click(function() {
var keyword = $(this).attr("class").split(" ");
keyword = keyword.filter(function(value, index, arr){ return value != "on";});
keyword = keyword.filter(function(value, index, arr){ return value != "off";});
keyword = keyword.filter(function(value, index, arr){ return value != "kw";});
keyword = keyword.filter(function(value, index, arr){ return value != "neutral";});

$("li." + keyword).addClass("on");
$("li." + keyword).removeClass("neutral");
$("li." + keyword).removeClass("off");

$("li.neutral").each(function() {
$(this).addClass("off");
$(this).removeClass("neutral");
$(this).removeClass("on");
});

$('div.item').not("." + keyword).each(function()
{
  $(this).hide();
});
});

$("p.remove").click(function() {
  $("li.on").each(function() {
$(this).addClass("neutral");
$(this).removeClass("on");
$(this).removeClass("off");
});

$("li.off").each(function() {
$(this).addClass("neutral");
$(this).removeClass("off");
$(this).removeClass("on");
});

$("div.item").each(function() {
  $(this).show();
});
});

function hiderows() {
  var panels = document.getElementsByClassName("full");
  for(var i = 0; i < panels.length; i++) {
    var panel = panels[i];
    if( panel.style.display == 'none') {
      panel.style.display = ''; }
    else { panel.style.display = 'none';}
  }
}
