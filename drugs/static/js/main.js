$(document).ready(function() {
    console.log('Hello Worlds')

    $("input#n").autocomplete({
        source: "/entitylookup/",
        minLength: 0,
        // On select - conditional Ajax calls
        select: function( event, ui ) {
          ui.item.entityType ?
            // For mechanism lookup if entity type is mechanism
            $.ajax({
              method: "GET",
              url: '/mechanisms/',
              datatype: 'jsonp',
              data: {'id':ui.item.id},
              success: function(response){
                  // clear previous record and add new record
                  $('#drug').empty()
                  $('#drug').append(response)
              }
            }):
            // Drug lookup if entity type is drug
            $.ajax({
              method: "GET",
              url: '/drugs/',
              datatype: 'jsonp',
              data: {'id':ui.item.id},
              success: function(response){
                // clear previous record and add new record
                  $('#drug').empty()
                  $('#drug').append(response)
              }
            })

        },

        open: function() {
            $( this ).removeClass( "ui-corner-all" ).addClass( "ui-corner-top" );
        },
        close: function() {
            $( this ).removeClass( "ui-corner-top" ).addClass( "ui-corner-all" );
        }
    })

})
