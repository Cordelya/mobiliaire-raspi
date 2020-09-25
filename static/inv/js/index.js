

$(document).ready( function () {

 $('table').DataTable( {
   dom: 'Bfrtip',
   buttons: ['excel', 'csv', 'print', 'pdf']
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
