

$(document).ready( function () {

 $('table.t1').DataTable( {
   "dom": '<"row" <"col-md-12" B>><"row" <"col-md-4 pt-2" l><"col-md-4 offset-3 pt-2" f>><t><"row" <"col-md-4 pb-2" i><"col-md-4 offset-4" p>>',
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

$('table.t2').DataTable( {
  "dom": '<"border border-primary mb-3" Q><"row" <"col-md-12" B>><"row" <"col-md-4 pt-2" l><"col-md-4 offset-3 pt-2" f>><t><"row" <"col-md-4 pb-2" i><"col-md-4 offset-4" p>>',
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





$("button.kw").click(function() {
var keyword = $(this).attr("class").split(" ");
keyword = keyword.filter(function(value, index, arr){ return value != "on";});
keyword = keyword.filter(function(value, index, arr){ return value != "off";});
keyword = keyword.filter(function(value, index, arr){ return value != "kw";});
keyword = keyword.filter(function(value, index, arr){ return value != "list-group-item";});
keyword = keyword.filter(function(value, index, arr){ return value != "list-group-item-primary";});
keyword = keyword.filter(function(value, index, arr){ return value != "py-1";});
keyword = keyword.filter(function(value, index, arr){ return value != "neutral";});

$("button." + keyword).addClass("on");
$("button." + keyword).removeClass("neutral");
$("button." + keyword).removeClass("off");

$("button.neutral").each(function() {
$(this).addClass("off");
$(this).removeClass("neutral");
$(this).removeClass("on");
});

$('div.item').not("." + keyword).each(function()
{
  $(this).hide();
});
});

$("button.remove").click(function() {
  $("button.on").each(function() {
$(this).addClass("neutral");
$(this).removeClass("on");
$(this).removeClass("off");
});

$("button.off").each(function() {
$(this).addClass("neutral");
$(this).removeClass("off");
$(this).removeClass("on");
});

$("div.item").each(function() {
  $(this).show();
});
});
