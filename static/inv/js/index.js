

$(document).ready( function () {

 $('table').DataTable( {
   "dom": '<"row m-1" <"col-md-12" B>><"row m-1" <"col-md-4 pt-2" l><"col-md-4 pb-2" i><"col-md-4 pt-2" f>><t>p',
   "buttons": ['excel', 'csv', 'print', 'pdf'],
   "lengthMenu": [ [10, 25, 50, -1], [10, 25, 50, "All"] ],
   "order": []
} );

} );

function hiderows() {
  var panels = document.getElementsByClassName("full");
  for(var i = 0; i < panels.length; i++) {
    var panel = panels[i];
    if( panel.style.display == 'none') {
      panel.style.display = ''; }
    else { panel.style.display = 'none';}
  }
}
