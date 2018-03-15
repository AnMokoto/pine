$(document).ready(function () {
    var menustate = false

    $('.article-details-nav-box div').hover(function () {
        $(this).children().each(function () {
            $(this).css({
                'background-color': 'orange'
            })
        })
    }, function () {
        $(this).children().each(function () {
            $(this).css({
                'background-color': ''
            })
        })
    }).click(function () {

        $('.article-details-toc').css({
            transform: menustate ? 'translateX(-100%)' : 'translateX(0)'
        })
        $(this).children().each(function (index, view) {
            switch (index) {
                case 0:
                    $(this).css({
                        'transform': menustate ? 'rotate(0deg)' : 'rotate(45deg)',
                    })
                    break;
                case 1:
                    $(this).css({
                        'opacity': menustate ? 1 : 0,
                    })
                    break;
                case 2:
                    $(this).css({
                        'transform': menustate ? 'rotate(0deg)' : 'rotate(-45deg)',
                    })

            }
        })

        $('.article-details-nav-box').css({
            position: menustate ? 'absolute' : 'fixed'
        })

        menustate = !menustate

    })

    if ($('.toc ul li').length > 0)
        setTimeout("$('.article-details-nav-box div').click()", 500);


    $('img').css({
        'display': 'inline-block',
        'margin': '2px',
    })
})