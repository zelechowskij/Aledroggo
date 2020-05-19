        $(document).ready(function () {

    $('.phraseButton').on('click', function () {

        var phrase = $('#phraseInput').val();
        alert(phrase);
        req = $.ajax(
                    { url : '/phrase',
                      type : 'POST',
                      data : {'phrase' : phrase}}
                );
        $('#phraseJumbotron').fadeOut(1000);

    });
        });



