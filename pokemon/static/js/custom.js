$(document).ready(function() {

    // send ajax
    $.ajax({
        url: '/pokemon', // url where to submit the request
        type: "GET", // type of action POST || GET
        dataType: 'json', // data type
        success: function(data) {
            console.log('working'),
                populate_page(data),
                populate_table(data)
            // you can see the result from the console
            // tab of the developer tools

        },
        error: function(xhr, resp, text) {
            console.log(xhr, resp, text);
        }

    });


});

function populate_page(data) {


    $('.pokemon_hp').html(
        $('<p class="pokemon_result_hp">hp:' + data.pokemon.hp + '</p>')
    );
    $('.pokemon_name').html(
        $('<p>' + data.pokemon.name + ' has appeared!  </p>')

    );


    $('.opponent_hp').html(
        $('<p class="opponent_result_hp"> hp:' + data.opponent.hp + '</p>')
    );
    $('.opponent_name').html(
        $('<p>' + data.opponent.name + ' has appeared! </p>')
    );


};

function populate_table(data) {


    $.each(data.pokemon.moves, function(index, value) {
            $.each(value, function(key, api_address) {


              var move_id = api_address.split('/')[4]

                    var $tr = $('<tr class="moves-list">').append(
                        $('<td class="move"> ').html("<button id='" + move_id + "' class='pokemon pokemon-move move-button' >" + key + "</button>")
                      ).appendTo('#pokemon_moves');

                    });
            });

        $.each(data.opponent.moves, function(index, value) {
            $.each(value, function(key, api_address) {

                var move_id = api_address.split('/')[4]

                var $tr = $('<tr class="moves-list">').append(
                    $('<td class="move"> ').html("<button id='" + move_id + "' class='opponent opponent-move move-button' >" + key + "</button>")
                ).appendTo('#opponent_moves');

            });
        });


        $('.move-button').click(function() {



            var name = $(this).attr('class').split(' ')[0]
            // send ajax
            $.ajax({
                url: '/move/', // url where to submit the request
                type: "GET", // type of action POST || GET
                dataType: 'json', // data type
                contentType: "application/json",
                data: {
                    'move_id': $(this).attr('id'),
                    'name': name
                }, // post data || get data
                success: function(data) {
                    // you can see the result from the console
                    // tab of the developer tools
                    populate_page(data)

                    console.log(data)

                },
                error: function(xhr, resp, text) {
                    console.log(xhr, resp, text);
                }
            });


        });

    }
