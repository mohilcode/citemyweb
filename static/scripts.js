$(document).ready(function() {
    var chosenStyle = localStorage.getItem('chosenStyle');
    var chosenStyleName = localStorage.getItem('chosenStyleName');
    if (chosenStyle && chosenStyleName) {
        $('#dropdownMenuButton').text(chosenStyleName);
        $('#style').val(chosenStyle);
    }

    $('.dropdown-item').click(function(e) {
        e.preventDefault();
        $('#dropdownMenuButton').text($(this).text());
        $('#style').val($(this).data('value'));

        localStorage.setItem('chosenStyle', $(this).data('value'));
        localStorage.setItem('chosenStyleName', $(this).text());
    });

    $('.copy-button').click(function() {
        var citation = $(this).data('citation');

        var $temp = $('<input>');
        $('body').append($temp);
        $temp.val(citation).select();
        document.execCommand('copy');
        $temp.remove();

        $('.toast').toast('show');
    });

    $('.toast').on('hidden.bs.toast', function() {
        $(this).removeClass('show');
    });
});
