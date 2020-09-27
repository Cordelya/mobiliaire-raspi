

$(document).ready( function () {

 $('table').DataTable( {
   "dom": '<"top"l<"br">f<"clear">>rt<"bottom"i<"br">Bp<"clear">>',
   "buttons": ['excel', 'csv', 'print', 'pdf'],
   "lengthMenu": [ [10, 25, 50, -1], [10, 25, 50, "All"] ]

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
